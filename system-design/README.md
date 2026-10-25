# System design: AI, ML and GenAI

Practice designing systems, explaining decisions, and handling follow-up constraints. This section supports engineers preparing for FAANG-style interviews and interviewers looking for discussion exercises.

- [Sources and course comparison](SOURCES.md)
- [Practice queue by difficulty and theme](TRACKER.md)
- [Answer template](templates/design.md)
- [Coding exercises](../README.md#coding-exercises)

The queue contains original practice scopes linked to relevant learning material. It is not a verified list of questions asked by specific companies. Local full solutions will be added as exercises are attempted; the source comparison identifies external worked guidance.

## Difficulty

These are repository-assigned levels, not source ratings or company hiring levels. The same product can become harder when its constraints change.

- **Foundation:** one bounded use case, a straightforward baseline, basic metrics and deployment.
- **Intermediate:** several stages, retrieval or personalization, freshness, measurable quality/latency tradeoffs.
- **Advanced:** strict permissions or latency, unreliable tools, high concurrency, cost controls, and difficult failure/recovery decisions.

Themes: classical ML, search/recommendation, GenAI/RAG, agents, multimodal, and AI infrastructure. GenAI and agents are subareas of AI; the tags distinguish practice emphasis.

## One-hour practice session

Spend 5 minutes clarifying requirements, 10 on a baseline and diagram, 15 on the key design decisions, 10 on estimates and evaluation, 10 on failure modes and follow-ups, and 10 comparing with a reference and recording gaps. A weekend session can add a timed mock and a revised design.

To fit the existing roughly nine-hour weekly budget, a possible split is four hours coding and five hours system design. This is an optional allocation, not extra work on top of the coding plan; reduce new coding problems if you adopt it. Start with one or two design cases per week and revisit them under changed constraints.

## Capture each exercise

Use stable IDs `SD-001`, `SD-002`, etc., and folders such as `system-design/exercises/sd-001-ticket-classifier/`. Theme and difficulty belong in the tracker so reclassifying a problem does not require moving it.

Each exercise uses:

- `problem-description.md`: original task, constraints, theme, difficulty and source links.
- `my-solution.md`: your own design, diagrams, estimates and reasoning.
- `agent-solution.md`: agent-written alternative with assumptions, tradeoffs, evaluation and follow-ups.

Use Mermaid diagrams where helpful. A reference is one defensible design, not an answer key. Keep your initial attempt before reading it. Track outcomes with N/G/I/R and a Yes/No review flag, as in the coding section. Do not infer successful completion from a filled-in document alone.
