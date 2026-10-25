# Twelve week coding and DSA study plan

The working budget is **five weekday hours plus four weekend hours = nine hours per week**, or **108 hours over 12 weeks**. Treat this as a starting plan for someone who can already program fluently; interview readiness depends on initial skill and demonstrated performance.

## Weekly schedule

| Session | Time | Work |
| --- | ---: | --- |
| Monday–Thursday | 60 minutes each | One focused problem session per day |
| Friday | 60 minutes | Re-solve two older problems without notes; update weaknesses |
| Saturday | 120 minutes | One new problem session; 60 minutes revising difficult problems or concepts |
| Sunday | 120 minutes | 90 minutes for reciprocal peer mock and feedback; 30 minutes for review, planning and GitHub sync |
| Total | 540 minutes | 9 hours |

During weeks one and two, use Sunday's mock time for a baseline attempt, explanation aloud, and foundational practice. Start peer sessions in week three. If free mock credits run out or a partner is unavailable, swap practice with a colleague or record a timed attempt and review it against the mock rubric.

### A sixty minute problem session

- **0–5 minutes:** reconstruct one recent insight or invariant from memory.
- **5–30 minutes:** clarify the problem, state a simple solution, then attempt an improved solution without help.
- **30–40 minutes:** if stuck, take one hint or read the reasoning. If already solved, examine a variation or alternative.
- **40–55 minutes:** close the explanation, implement or repair the solution, test edge cases, and state complexity.
- **55–60 minutes:** save your code, record the main mistake and insight, and set the next review date.

When a difficult problem needs more time, continue it in the next slot and remove another new problem from the week. An honest slow solve is more useful than copying code to keep a schedule intact.

## Topic sequence

| Week | Focus | New problems | End-of-week check |
| --- | --- | ---: | --- |
| 1 | Arrays, hashing, complexity and language fluency | 5 | Explain hash-map/set operations and implement simple solutions independently |
| 2 | Two pointers and sliding windows | 5 | Explain why pointer movements preserve correctness |
| 3 | Binary search and stacks | 5 | State search bounds and avoid off-by-one errors; first peer mock |
| 4 | Linked lists and pointer manipulation | 5 | Trace pointer updates and handle empty/single-node cases |
| 5 | Tree DFS, BFS and recursion | 5 | Choose traversal order and account for recursion space |
| 6 | BSTs and heaps | 5 | Compare sorting, selection and heap approaches |
| 7 | Graph traversal and dependencies | 5 | Use visited state correctly and distinguish cycle detection from traversal |
| 8 | Backtracking and tries | 5 | Define state, base case, choices and undo step |
| 9 | Intervals and greedy reasoning | 5 | Justify the greedy choice instead of relying on recognition |
| 10 | Dynamic programming | 5 | Define state, recurrence, base cases and evaluation order |
| 11 | Mixed unfamiliar problems and weakest patterns | 0–5 | Solve without being told the topic |
| 12 | Interview simulations, targeted revision and optional company practice | 0–5 | Repeat good performance across several mock sessions |

The [tracker](TRACKER.md) contains the 50 core problems. It is a selected queue, not a claim to reproduce NeetCode 150 or Grind 75. Use NeetCode or another chosen resource for explanations when available. Do not add 150 more problems as a second requirement.

## Revision and durable recall

Use **2, 7 and 21 days after the first attempt** as practical review targets, then adjust to available time. These intervals are a scheduling heuristic, not a scientifically optimized prescription. If a review fails, schedule another attempt in roughly two days. After several successful reviews, widen the interval.

For each re-solve, hide the solution and topic label, derive the approach, code it and check complexity. If you merely recognize the code after opening the file, record it as a guided attempt rather than mastery.

Prefer **50–60 distinct problems with meaningful repetitions and mocks** to rushing through 150. This is an achievable planning target, not a minimum needed to pass. If review backlog exceeds your Friday/Saturday slots, reduce new problems to three that week.

## Adjustments for your starting point

- **New to DSA:** spend an extra two to four weeks on complexity, arrays, maps, recursion and tree traversal. Favor a 16-week horizon and fewer problems. Do not assume a subscription compresses the learning time.
- **Experienced but rusty:** follow the 12-week plan and skip only topics you can demonstrate independently.
- **Already comfortable with medium questions:** use an eight-week version with two weeks diagnosing gaps, four weeks of mixed practice and two weeks of mocks/targeting. Spend less time watching lessons.
- **Only two weekend hours available:** use a seven-hour week, reduce new work to three or four problems, and stretch the plan toward 16 weeks.

Use your strongest existing language. Switching languages during a short prep window creates another skill to practice. Build a small personal syntax reference for collections, sorting, heaps, queues and common boundary cases in that language.

## Practical readiness checks

These are working targets, not employer hiring criteria:

- On several separate days, solve an unfamiliar medium problem in about 30–40 minutes with no substantive hints, leaving time to explain and test it.
- Derive a straightforward solution and explain why a faster approach is valid.
- Test empty or minimal input, duplicates, boundaries and a representative larger case.
- Explain time and auxiliary space, including recursion depth and data-structure costs.
- Complete at least three recent mock sessions without repeating the same major reasoning, communication or implementation failure.
- Handle a changed constraint or follow-up instead of recalling one fixed answer.

Adapt timing to the real interview format supplied by the recruiter. If these checks are weak, use the next week for targeted repair rather than increasing the question count.

## Use AI deliberately

During learning, ask for the smallest useful hint or for a counterexample to your reasoning. After solving, ask for edge cases and alternative complexity tradeoffs, then verify them yourself. During independent benchmarks and mocks, disable solution-generating assistance. Mark any assisted attempt honestly in the tracker.

## First two weeks

Week one establishes your baseline and daily habit. Week two tests whether your chosen explanations help you generalize. At the end, use the purchase rule in [the comparison](PLATFORMS.md): pay only for a demonstrated gap. Keep the curriculum stable long enough to assess it.
