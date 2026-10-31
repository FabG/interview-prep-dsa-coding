# SD-001 — Feedback on the 15-minute attempt

- Date: October 31, 2026
- Duration: 15 minutes, user-reported
- Basis: recorded conversation only, including interviewer probes and explanations
- Assessment: qualitative practice feedback, not an official FAANG rubric or hiring prediction

## Overall assessment

A promising first-pass design with good breadth across the ML lifecycle. The
strongest signals were separating offline training from serving and proposing
champion–challenger shadow testing. The design remained incomplete: the defining
human-fallback policy was not specified, and “performs well” and “scales horizontally”
were not backed by acceptance criteria or estimates.

For 15 minutes, the breadth is useful. As a complete senior-level system design
answer, this would need deeper decisions and validation. The unaddressed areas
were not demonstrated in this short attempt; that is not proof of inability.

## Evidence and comparison

| Area | What you demonstrated | What the reference adds |
| --- | --- | --- |
| Clarification | Asked about misrouting, reusable components and ticket fields; restated scope | Explicit error costs, automation target and human-capacity constraints |
| ML pipeline | Supervised learning, historical labels, train/validation/test split, model artifact | Label audit, time-based splits, duplicate grouping and prevention of future-data leakage |
| Representation | Body embeddings to capture meaning | Subject plus body, a cheaper baseline and measured model selection |
| Evaluation | Accuracy, precision/recall/F1; one-vs-rest after imbalance probe | Coverage versus error tradeoff, costly-class errors, calibration and explicit thresholds |
| Live architecture | Queue/worker/model/routing flow; horizontal scaling | Online serving selection, about 23 peak requests/second, latency budget and warm capacity |
| Human fallback | Confirmed it is needed | Concrete deferral conditions and monitoring of human backlog |
| Reliability | Raised active-passive/active-active regions | Duplicate-safe writes, bounded retries, stale results, manual overrides and simpler initial availability |
| Model updates | Periodic retraining and champion–challenger shadow comparison | Representative labels, uncertainty-aware promotion gates, canary and rollback |
| Ground truth | Independent reviewers, majority vote, review on disagreement | Domain expertise, affordable sampling, blinded review and bounded adjudication |

## Corrections worth remembering

- Labels are training targets, not prediction-time inputs. Your later description
  correctly chose ticket body text as input; the initial wording was imprecise.
- Fitting is training. Keeping the same classes does not make updates a separate
  concept from retraining.
- Batch Transform is intended for dataset/job inference. An online endpoint is
  the defensible starting choice for this two-second live path; see the AWS
  references in [the agent solution](Agent-Solution.md).
- A queue absorbs bursts but adds waiting time. Horizontal scalability needs
  throughput measurements, quotas and warm capacity; it is not unlimited.
- Multiple reviewers can share the same mistaken interpretation. Voting helps
  consistency but requires clear instructions and domain adjudication.

## Highest-value next practice

1. Define when the system auto-routes and when it abstains. Explain how error
   cost, confidence and manual capacity affect that choice.
2. Compute average and peak throughput, then choose one serving architecture
   and account for the two-second budget.
3. Specify a representative labeled evaluation set and measurable promotion
   gates rather than saying “if it performs.”
4. Explain duplicate processing, human overrides and failure recovery before
   adding multi-region infrastructure.

## Interview delivery

You covered the lifecycle coherently and proposed practical mechanisms. Several
follow-up questions remained open as you moved to another topic. In the next
attempt, close each probe with a decision and rationale before broadening scope.
A useful answer pattern is: “I choose X because of constraint Y; I will validate
it using Z; if that fails, we fall back to W.”

The reference is longer because it is a post-interview study artifact. You would
not need to recite every detail in 15 minutes. Prioritize the routing/fallback
policy, a justified baseline, key estimates and how you will know it works.
