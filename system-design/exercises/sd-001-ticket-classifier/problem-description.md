# SD-001 — Ticket classifier with human fallback

- Theme: Classical ML
- Difficulty: Foundation (repository-assigned)
- Author: Codex; original practice scenario, not a reported company question
- Created: October 25, 2026
- Related learning: [AIMLInterviews design framework](https://github.com/alirezadir/AIMLInterviews/blob/main/src/MLSD/ml-system-design.md), reviewed October 25, 2026. The scenario and numbers below are invented for this exercise, not taken from that source.
- Timebox: 45 minutes designing, 15 minutes reviewing

## Interview prompt

A SaaS company receives customer support tickets through its website and email.
Today, a support team reads each ticket and assigns it to the right department.
Design an ML-assisted system that routes tickets automatically when appropriate
and sends uncertain cases to a human for triage.

The goal is to reduce manual routing work without increasing harmful misrouting.
Explain the complete system, from receiving a ticket to measuring whether the
routing decision was useful. No implementation is required.

## Scenario facts

These are exercise assumptions you may challenge explicitly.

| Area | Starting constraint |
| --- | --- |
| Routing categories | Billing, account access, technical support, and general enquiries |
| Scope | Assign one initial destination; humans can correct it |
| Inputs | Ticket ID, subject, body, timestamp, channel and customer account ID |
| Language | English initially; attachments excluded |
| Traffic | 100,000 tickets per day; peak arrival rate 20 times the daily average |
| Payload | Average subject and body size combined: 5 KB |
| Responsiveness | Target: 95% of automated routing decisions within 2 seconds of receipt |
| Training data | 12 months of historical tickets with initial and final team assignments and timestamps; some labels are missing or wrong |
| Feedback | Human reroutes are logged, but the eventual correct team may be known only after resolution |
| Privacy | Ticket bodies may contain personal information; only authorized support staff may view them |
| Reliability | Tickets must remain available for manual handling when automated classification is unavailable |

The existing ticketing product already handles ticket submission and the staff
inbox. Your design adds classification and routing to that product. You may
propose changes to its integration interfaces.

Out of scope: generating replies, resolving tickets, building a general-purpose
chatbot, and training a foundation model from scratch. A model choice is yours
to justify; no particular technique or vendor is required.

## Questions to clarify first

Before drawing the architecture, identify the missing requirements you would
ask the interviewer about. For example, clarify what counts as a harmful
misroute and what tradeoff the business accepts between automation and review.
Write assumptions explicitly when an answer is unavailable.

## Expected design deliverables

1. Scope and measurable success criteria.
2. A high-level diagram showing online decisions and offline model updates.
3. The data and labels you would use, plus a justified first model or baseline.
4. The rule for automatic routing versus human review.
5. Rough traffic and data-volume estimates with units.
6. Evaluation, rollout, monitoring and behavior during failures.
7. At least one alternative and why you would choose or reject it.

## Optional interviewer follow-ups

Try these after completing the initial design:

- Billing tickets are rare, but misrouting one is much more costly than other mistakes. What changes?
- A new product creates a fifth category with almost no labeled examples.
- The model is unavailable for 30 minutes during peak traffic.
- Human corrections arrive days later. How do you assess a new model today?
- The business asks for multilingual tickets without increasing the latency target.

## Workspace

- [My solution](my-solution.md)
- [Agent solution](Agent-Solution.md)
- [System design tracker](../../TRACKER.md)

Start with your clarification questions, then your assumptions and success criteria.
