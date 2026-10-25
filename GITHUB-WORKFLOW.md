# Keeping interview notes in GitHub

Use a portable Markdown folder and your own solution files. This keeps research, reasoning and revision history available after any course subscription ends.

## Suggested layout

```text
interview-prep-dsa-coding/
  README.md
  PLATFORMS.md
  STUDY-PLAN.md
  TRACKER.md
  GITHUB-WORKFLOW.md
  templates/
    problem.md
    weekly-review.md
    mock-interview.md
  problems/                  # Create as you work
    0001-two-sum/
      problem-description.md # Problem, examples, constraints and source URL
      my-solution.md         # Your Python code imported from LeetCode
      leetcode-solution.md   # Reference solution from LeetCode
  patterns/                  # Your own reusable explanations
    sliding-window.md
  weekly/                    # Short weekly retrospectives
  mocks/                     # Feedback and next actions
```

Keep folders flat enough to find a problem by number or title. Record patterns in the tracker because one problem can teach several patterns.

## Files for each problem

- **`problem-description.md`**: the problem description, examples, constraints and original LeetCode problem URL.
- **`my-solution.md`**: the Python code you wrote on LeetCode, imported into a fenced `python` code block. Keep your submitted code as written, along with the submission date, result, approach, time/space complexity and any mistakes or lessons. Record revisions separately so your original attempt remains identifiable.
- **`leetcode-solution.md`**: the reference solution from LeetCode, including its explanation and code in a fenced code block. Include the exact source URL and identify whether it is an official editorial or a community solution; credit the author when provided. Keep this separate from your own solution so you can compare the approaches.

## Five minutes after each problem

1. Create the problem folder and fill in `problem-description.md` with the problem details and source URL.
2. Import your LeetCode code into `my-solution.md`, recording the actual submission result even if it was not accepted. Use `templates/problem.md` as a checklist for the accompanying learning notes.
3. After your attempt, add the LeetCode reference solution to `leetcode-solution.md` with its source attribution. If it is not available yet, leave it pending rather than inventing a reference solution.
4. In `my-solution.md`, note the key difference from the reference, the main mistake and time/space complexity. Three useful sentences are sufficient.
5. Update outcome, last attempt and next review in the tracker. Mark attempts that used the reference solution as guided.

Write a longer explanation only when it teaches something you expect to forget. For reference material that cannot be reproduced, keep its source link and a summary in your own words.

## Working repository

The local clone is `~/interview-prep-dsa-coding`, with origin [FabG/interview-prep-dsa-coding](https://github.com/FabG/interview-prep-dsa-coding). All future research, notes and solutions belong here. The reference files live at the repository root.

For ongoing work, a single weekly commit is enough. The tracker carries attempt dates; Git commits need not become a daily streak requirement. Review the changes before committing and pushing:

```bash
cd ~/interview-prep-dsa-coding
git status --short
git add README.md PLATFORMS.md STUDY-PLAN.md TRACKER.md GITHUB-WORKFLOW.md templates AGENTS.md .gitignore
git diff --cached
git commit -m "Add coding interview research and study plan"
git push -u origin HEAD
```

Add future problem, pattern, weekly-review and mock files explicitly as they are created. The ZIP is a convenience snapshot; the Markdown files are authoritative.

## Optional automatic solution syncing

[LeetSync](https://github.com/LeetSync/LeetSync) is an open-source Chrome extension whose project describes syncing LeetCode submissions to a chosen GitHub repository. It can reduce copying, but it does not capture why you were stuck or whether you can solve a problem again.

I recommend beginning with manual capture for two weeks. If copying becomes a recurring nuisance, inspect the official project's current extension link, requested access and recent issue reports before choosing it. Sync compatibility has not been tested here, and no extension has been installed or authorized.

Use a dedicated solution folder or repository when configuring a sync tool and check one uploaded solution before depending on it. If a sync tool exports standalone code files, import your Python code into `my-solution.md` and retain the three-file layout above. Keep the same short notes and revision workflow even if code transfer becomes automatic.

## Long-term reference

Once a month, distill recurring lessons into a small pattern note: when to use it, the invariant, a minimal template in your language, common mistakes and two representative problem links. Keep the detailed problem notes for context and use the pattern notes for later refreshers.

Refresh pricing only when considering another purchase. The comparison is a dated reference, not a promise that today's promotion will remain available.
