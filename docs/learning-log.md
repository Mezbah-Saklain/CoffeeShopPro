# Learning Log — CoffeeShopPro

## Day 1 — [DATE]

**08:00–09:00** — Wrote requirements. Struggled to distinguish functional from 
non-functional at first; re-read Pressman chapter 5, then realized NFRs are 
"how well" (performance, portability) vs FRs "what" (features).

**09:00–10:30** — Rewrote decorator module. Initially had duplicate cost logic 
in each decorator class; extracted `BeverageDecorator` base class and used a 
class-level `COST` constant. Cleaner, easier to test.

**10:30–12:00** — Added SQLite persistence. Hit `sqlite3.OperationalError: no 
such table` on first run because `_init_schema()` wasn't called from `__init__`. 
Fixed after reading the Python sqlite3 docs.

**13:00–14:00** — Set up GitHub Actions. First run failed silently because I 
hadn't committed the `docs/` folder yet; second run failed on a YAML indentation 
error (a tab instead of spaces). Fixed by copying the example from the GitHub 
Actions documentation verbatim.

**14:00–15:30** — Wrote tests. Discovered that `MagicMock()` returns a mock for 
**any** method call — so `mock_db.save_order.assert_called_once()` worked, but 
`mock_db.save_order.call_args` needed `.call_args` (an attribute, not a method). 
Small but important distinction.

**15:30–16:30** — Practiced resolving a merge conflict. Learned that Git 
sometimes auto-resolves trivial conflicts and sometimes doesn't; the case that 
conflicted was the same `print()` line edited in two branches.

**17:00–18:00** — Evaluated learning resources:
- **Official Python docs** — clear, accurate, but verbose.
- **GitHub Actions official docs** — very good; the "Quickstart" walkthrough was 
  the single most helpful page.
- **A YouTube tutorial** — outdated (used `actions/setup-python@v2` while v5 is 
  current). Had to correct it manually.
- **Stack Overflow** — useful for the `no such table` error.

## What I Learned

1. Testing with mocks is not "extra work" — it's what allows refactoring with 
   confidence. Tests that touch the real database break unpredictably.
2. TDD feels slow at first but prevents rework. The two bugs I caught (a 
   rounding issue and an off-by-one in promo application) were caught *before* 
   they hit `main`.
3. CI is a tiny amount of YAML that provides huge value. It is worth the 30 
   minutes to set up.