# Merge Conflict — Resolution Note

## What conflicted

Two feature branches modified the **same line** of `main.py` (the welcome
banner inside `print_menu()`):

- `feature/banner-a` — changed the banner to `"TO THE COFFEE SHOP"`. Merged first.
- `feature/banner-b-conflict` — changed the same banner line to
  `"WELCOME TO THE COFFEESHOP PRO"`. 

When attempting to merge `feature/banner-b-conflict` into `main`, Git could not 
determine which version to keep because both branches diverged from the same 
ancestor commit and modified the exact same line.

## How Git reported it

    CONFLICT (content): Merge conflict in main.py

## How I resolved it

I opened `main.py` in VS Code, which showed the conflict markers:

    <<<<<<< HEAD
        print("║         ☕  TO THE COFFEE SHOP  ☕       ║")
    =======
        print("║         ☕  WELCOME TO THE COFFEESHOP PRO  ☕       ║")
    >>>>>>> feature/banner-b-conflict

I resolved it by deleting the Git markers and keeping the incoming intent,
adjusting the spacing so the console box remained aligned:

        print("║         ☕  WELCOME TO COFFEESHOP PRO  ☕         ║")

Then I completed the merge:

    git add main.py
    git commit -m "Resolve merge conflict: combine banner changes"
    git push origin main

## Evidence

- `image-merge-conflict-cmd.png` — terminal showing the CONFLICT message
- `image-merge-conflict-vscode.png` — the conflict markers in the editor
- `image-merge-resolved.png` — the resolved file after push