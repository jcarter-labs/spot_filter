# groups.io Access Process

How this project reads groups.io content that requires an authenticated
(member) session — groups.io returns HTTP 402 Payment Required for
unauthenticated access to most group message archives, so a plain
`WebFetch` fails even on a publicly search-indexed thread. Implemented
as the `groupsio-fetch` skill (`groupsio-fetch.skill` in this repo:
`groupsio-fetch/SKILL.md` + `groupsio-fetch/scripts/groups_io_fetch.py`).

## Login mechanism

A Python script does a real session-cookie login, using `requests` +
stdlib `html.parser` (no `telnetlib`/`bs4` dependency):

1. `GET https://groups.io/login` — pull the page's CSRF token (scraped
   via regex from the login form's hidden `csrf` input).
2. `POST https://groups.io/login` with `email`, `password`, `csrf`,
   `timezone` — establishes an authenticated session cookie.
3. Reuse that session to `GET` any topic/message/search URL, stripping
   the returned HTML down to readable text (the actual message content
   sits past a large block of navigation/UI chrome — `#NNNNN <author>
   ... All Messages By This Member <body text>`).

The CSRF-token regex was confirmed live against groups.io's actual
login form on 2026-08-30. If groups.io changes that form, the regex in
`groups_io_fetch.py` needs a small update.

## Credentials — never stored in the repo, never repeated in chat

- **Email is fixed**: `jcfrgmn@gmail.com` — assumed, not re-asked.
- **Password is never stored in the repo or written into any script.**
  It's asked for once per session, then written to a local file,
  `.groupsio_creds` (two lines: email, password), living **outside any
  git repo** — in the scratchpad temp directory. The script checks this
  file first, falling back to `GROUPSIO_EMAIL`/`GROUPSIO_PASSWORD` env
  vars if the file is absent.
- **Why a file instead of an exported env var**: `export` doesn't
  persist across separate `!`-prefixed commands — each one spawns a
  fresh shell, so an export in one command is gone by the next. A file
  is the only thing that survives between invocations without
  re-pasting the password every time.
- The creds file should be deleted once groups.io work for the session
  is done (`rm .groupsio_creds`).

## Execution split — the credential never touches the assistant's own commands

Claude Code's auto-mode safety classifier blocks any Bash invocation
that contains a live password literal, so the assistant does not run
the credentialed command itself. The pattern instead:

1. The user creates the creds file once, via a single `!`-prefixed
   command (the one time the password is typed).
2. The assistant gives the user the exact fetch command to run via `!`
   (no credentials appear in it — the script reads the creds file).
3. The user runs it and pastes the output back.

## Scope limit

Only works for groups.io groups the authenticated account is actually
a member of. Confirmed working for `N1MMLoggerPlus` and `RBN-OPS`.
`CC-User` was explicitly out of scope per instruction during this
project's cluster research — VE7CC-specific threads living there were
never fetched directly; VE7CC's status was corroborated through
`N1MMLoggerPlus` instead. A group the account isn't a member of will
likely still return 402, or an access-denied page, even after a
successful login.

## Known fragility

- The CSRF-token scrape depends on groups.io's current login-form HTML
  structure.
- No pagination handling — a topic returns whatever groups.io renders
  on one page load; very long threads may be truncated by groups.io
  itself, not by this script.
- Search results and topic pages can surface old threads (sometimes
  years old, e.g. a 2019/2020 thread showing up for a "cluster" search
  in 2026) without making the age obvious in a snippet — always check
  the actual post date in the fetched content before treating it as
  current.
