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
    week1/
      1-1-0001-two-sum/
        problem-description.md # Problem, examples, constraints and source URL
        my-solution.py         # Your Python code and local example assertions
        agent-solution.md   # Agent explanation and reference code
      1-2-0217-contains-duplicate/
  patterns/                  # Your own reusable explanations
    sliding-window.md
  weekly/                    # Short weekly retrospectives
  mocks/                     # Feedback and next actions
```

Group problems under `problems/week1/`, `problems/week2/`, and so on. Name problem folders `<week>-<position>-<leetcode-id>-<slug>`, using the tracker reference and a four-digit LeetCode ID: for example, `1-1-0001-two-sum` and `1-2-0217-contains-duplicate`. Record patterns in the tracker because one problem can teach several patterns.

## Files for each problem

- **`problem-description.md`**: the problem description, examples, constraints and original LeetCode problem URL.
- **`my-solution.py`**: the Python code you wrote on LeetCode, saved as an executable file. Keep the LeetCode `Solution` class and signature, with learning notes and submission details in a module docstring or comments. Put local example assertions in a separate function called under `if __name__ == "__main__":` so importing the file does not run them. Keep revisions identifiable through Git history.
- **`agent-solution.md`**: the agent-prepared solution and explanation, with code in a fenced code block. Identify agent-written code explicitly. For supplied or imported code, preserve its provenance, include the exact source URL when available, and credit the author when provided. Keep this separate from your own solution so you can compare the approaches.

## Five minutes after each problem

1. Create the problem folder and fill in `problem-description.md` with the problem details and source URL.
2. Import your LeetCode code into `my-solution.py`, recording the actual submission result even if it was not accepted. Use `templates/problem.md` as a checklist for notes in the Python file’s docstring or comments. Run the local example assertions before updating the tracker.
3. After your attempt, add an agent-prepared solution to `agent-solution.md`, recording whether its code was written by the agent, supplied by the user, or imported from an attributed source. Leave the file pending until a solution has been added.
4. In the docstring or comments of `my-solution.py`, note the key difference from the reference, the main mistake and time/space complexity. Three useful sentences are sufficient.
5. Update outcome, last attempt and next review in the tracker. Mark attempts that used the reference solution as guided.

Write a longer explanation only when it teaches something you expect to forget. For reference material that cannot be reproduced, keep its source link and a summary in your own words.

## Run a solution locally

From the repository root, run:

```bash
python3 problems/week1/1-1-0001-two-sum/my-solution.py
```

For problem 1.1, fill in `Solution.twoSum` first. Until then, the scaffold raises `NotImplementedError`. The local checks use the three examples from the problem description and accept either ordering of the expected indices. A failed assertion shows the input, expected result and actual result. These examples are a starting check, not the full LeetCode test suite. Run Python normally, without `-O`, which disables assertions.

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

Use a dedicated solution folder or repository when configuring a sync tool and check one uploaded solution before depending on it. If a sync tool exports standalone code files, import your Python code into `my-solution.py` and retain the three-file layout above. Keep the same short notes and revision workflow even if code transfer becomes automatic.

## Long-term reference

Once a month, distill recurring lessons into a small pattern note: when to use it, the invariant, a minimal template in your language, common mistakes and two representative problem links. Keep the detailed problem notes for context and use the pattern notes for later refreshers.

Refresh pricing only when considering another purchase. The comparison is a dated reference, not a promise that today's promotion will remain available.
