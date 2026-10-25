# Coding exercises and AI system design

A growing bank of coding exercises, Python solutions, and system design practice covering classical ML, GenAI, agents, and AI infrastructure. Use it to practice a new technique, refresh your skills, prepare for an interview, or choose an exercise for a technical interview.

**For engineers:** pick a problem, try your own approach, run the examples locally, and compare your reasoning and complexity with the available solutions.

**For interviewers:** browse the problem queue by topic and difficulty, use the descriptions to frame an exercise, and consult the solutions to discuss approaches, tradeoffs, and edge cases.

## Choose a practice area

- [Coding exercises](#coding-exercises): DSA problems, runnable Python and agent solutions.
- [System design](#system-design): AI/ML and GenAI exercises organized by difficulty and theme, with learning sources and design guidance.

## Coding exercises

Start with the [problem queue and tracker](TRACKER.md). It contains **50 selected problems** across arrays, hashing, two pointers, binary search, stacks, linked lists, trees, heaps, graphs, backtracking, greedy algorithms, and dynamic programming, plus slots for additional practice.

The queue is broader than the implemented solution bank. Problem folders and solutions are added as exercises are attempted; reference solution files may still be pending. Outcome and review flags record the repository author's practice progress.

| Exercise | Difficulty | Description | Agent solution | My solution |
| --- | --- | --- | --- | --- |
| 1.1 Two Sum | Easy | [Problem](problems/week1/1-1-0001-two-sum/problem-description.md) | [Agent solution](problems/week1/1-1-0001-two-sum/agent-solution.md) | [My solution and examples](problems/week1/1-1-0001-two-sum/my-solution.py) |
| 1.2 Contains Duplicate | Easy | [Problem](problems/week1/1-2-0217-contains-duplicate/problem-description.md) | [Agent solution](problems/week1/1-2-0217-contains-duplicate/agent-solution.md) | [My solution and examples](problems/week1/1-2-0217-contains-duplicate/my-solution.py) |
| 1.3 Valid Anagram | Easy | [Problem](problems/week1/1-3-0242-valid-anagram/problem-description.md) | [Agent solution](problems/week1/1-3-0242-valid-anagram/agent-solution.md) | [My solution and examples](problems/week1/1-3-0242-valid-anagram/my-solution.py) |

### Try an exercise

1. Open its `problem-description.md` for the task, examples, constraints, and original source.
2. Attempt the problem before reading the solution. The existing `my-solution.py` contains implementation details and notes, so use a separate file if you want a fresh attempt.
3. Compare your approach with the saved Python solution and, where available, `agent-solution.md`.
4. Run the local examples and discuss correctness, edge cases, time complexity, and space usage.

With Python 3.9 or newer, run a saved solution from the repository root:

```bash
python3 problems/week1/1-1-0001-two-sum/my-solution.py
python3 problems/week1/1-2-0217-contains-duplicate/my-solution.py
```

The example runners report each result and continue after a failure. Run without `-O` so assertions remain enabled. These examples are a starting point; they do not cover the full LeetCode test suite.

### Repository layout

Exercises are grouped by study week for navigation. You can work through them in any order.

```text
problems/
  week1/
    1-1-0001-two-sum/
      problem-description.md
      my-solution.py
      agent-solution.md
    1-2-0217-contains-duplicate/
      ...
```

Folder names follow `<week>-<position>-<leetcode-id>-<slug>`, matching the stable problem references in the tracker. Each problem retains its source link; reference solutions include attribution details where available. See the [capture workflow](GITHUB-WORKFLOW.md) for adding exercises and recording solutions.

### Learning and interview preparation resources

For a structured route through the exercises, the optional study plan spans **12 weeks at about nine hours per week**. Python is the default language for this repository.

- [Python refresher](PYTHON-REFRESHER.md): syntax and standard-library tools for developers refreshing their Python skills.
- [Study plan and readiness checks](STUDY-PLAN.md): practice sessions, revision, and mock interviews.
- [Platform comparison and review evidence](PLATFORMS.md): free and paid preparation resources, researched October 25, 2026.
- [Problem note template](templates/problem.md): record reasoning, complexity, and lessons.
- [Weekly review template](templates/weekly-review.md): track practice and revisit difficult topics.
- [Mock interview template](templates/mock-interview.md): structure an interview practice session and feedback.

## System design

Explore [AI, ML and GenAI system design](system-design/README.md) for interview practice or architecture discussions. The starter queue includes 18 exercise scopes across classical ML, search/recommendation, RAG, agents, multimodal systems, and AI infrastructure.

- [Exercise queue by difficulty and theme](system-design/TRACKER.md)
- [Online sources: free and paid, worked answers, and review evidence](system-design/SOURCES.md)
- [Reusable design-answer template](system-design/templates/design.md)

Difficulty levels are our own Foundation / Intermediate / Advanced estimates. External resources provide worked guidance; local solutions will be added as exercises are attempted. Each future case will keep `problem-description.md`, `my-solution.md`, and `agent-solution.md` together.
