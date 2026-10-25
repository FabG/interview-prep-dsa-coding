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
      notes.md
      solution.py            # Or your preferred language
  patterns/                  # Your own reusable explanations
    sliding-window.md
  weekly/                    # Short weekly retrospectives
  mocks/                     # Feedback and next actions
```

Keep folders flat enough to find a problem by number or title. Record patterns in the tracker because one problem can teach several patterns.

## Five minutes after each problem

1. Copy your own accepted code into its problem folder.
2. Copy the problem template to `notes.md`.
3. Add the source URL, the key insight, the mistake you made and time/space complexity. Three useful sentences are sufficient.
4. Update outcome, last attempt and next review in the tracker.

Write a longer explanation only when it teaches something you expect to forget. Link to original problem statements and lessons; preserve your own reasoning and code rather than copying paid editorials, course pages or videos into the repo.

## Working repository

The local clone is `/Users/Fab/Git/interview-prep-dsa-coding`, with origin [FabG/interview-prep-dsa-coding](https://github.com/FabG/interview-prep-dsa-coding). All future research, notes and solutions belong here. The reference files live at the repository root.

For ongoing work, a single weekly commit is enough. The tracker carries attempt dates; Git commits need not become a daily streak requirement. Review the changes before committing and pushing:

```bash
cd /Users/Fab/Git/interview-prep-dsa-coding
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

Use a dedicated solution folder or repository when configuring a sync tool and check one uploaded solution before depending on it. Keep the same short notes and revision workflow even if code transfer becomes automatic.

## Long-term reference

Once a month, distill recurring lessons into a small pattern note: when to use it, the invariant, a minimal template in your language, common mistakes and two representative problem links. Keep the detailed problem notes for context and use the pattern notes for later refreshers.

Refresh pricing only when considering another purchase. The comparison is a dated reference, not a promise that today's promotion will remain available.
