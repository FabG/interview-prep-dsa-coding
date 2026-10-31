# SD-001 — Ticket classifier with human fallback: my solution

- Theme: Classical ML
- Difficulty (repository-assigned): Foundation
- Author / provenance: user design; Codex records the interview and acts as interviewer
- Problem: [description](problem-description.md)
- Attempt date: 2026-10-31
- Status: interview ended; partial design captured
- Outcome: P — partial attempt (interviewer guidance recorded)
- To review again?: Yes
- Time spent: 15 minutes (user-reported; not independently timed)
- Assistance used: interview prompt, answer scaffold and interviewer clarification; record any solution hints separately

## Requirements and assumptions

Candidate confirmed the scope: classify incoming tickets, route to the appropriate
existing team queue and use human triage in selected cases. See the interview log
for requirements clarified with the interviewer.

## Success criteria

Candidate-proposed offline metrics: overall accuracy and per-class precision,
recall and F1. Under class imbalance, evaluate each queue one-vs-rest using
precision and recall rather than relying on aggregate accuracy. F1 aggregation,
metric priorities, deployment thresholds and online success criteria remain open.

## Baseline and architecture

Candidate proposal:
- Separate an offline classification/training pipeline from live classification.
- Train and evaluate on approximately one year of historical tickets.
- Produce a serialized trained model for use by the live classification component.
- Begin with a simple design and extend it as needed.
- Proposed live path: incoming ticket → message queue → inference worker →
  model prediction → result message → routing worker → destination team queue.
- Hosting candidates: SageMaker batch inference or ECS/EKS with a REST API;
  final serving choice and separation of input/result queues remain open.
- Use SQS buffering and horizontal compute scaling to handle traffic spikes;
  capacity and latency calculations remain pending.

## Data and models

Candidate proposal:
- Use historical tickets with human annotations or labels identifying the intended queue.
- Train a supervised classifier to predict that queue label.
- Split the historical data into training, validation and test sets.
- Evaluate the model before making it available for live classification.
- Use ticket body text embedded as a vector to represent semantic meaning.
- Embedding model, classifier choice and split strategy remain open.

Terminology to clarify: the candidate described “taking label as an input.”
Labels are available during supervised training as targets; confirm which ticket
fields would be inputs at prediction time.

## Estimates

Not quantified during this attempt; capacity and latency-budget probes remained unanswered.

## Deep dive and alternatives

Candidate named hosting and regional-resilience alternatives but did not select
and justify a final option during this attempt.

## Evaluation and rollout

Candidate proposal:
- Collect labels from tickets handled by human triage and use them for model updates.
- Split data for training/testing and re-evaluate precision/recall.
- Consider a weekly or monthly retraining schedule; cadence not yet selected.
- Retrain when adding a class; label-set and routing changes remain to be specified.

- Compare the current champion with a challenger using copies of incoming
  traffic in shadow mode. Promote the challenger only if its performance meets
  requirements; quantitative thresholds remain to be defined.

- Obtain ground-truth labels through data scientist/analyst review, with repeated
  passes or two to four parallel reviewers. Use majority vote and return
  unresolved tickets for further labeling.

Open decisions: representative sampling and labeling volume, reviewer guidelines,
resolution of persistent disagreement, treatment of delayed or incorrect labels,
validation strategy, promotion thresholds and duration, staged rollout and rollback.

## Failure handling and operations

Candidate proposed regional resilience using active-passive or active-active
infrastructure; final choice and justification remain open. Failure handling,
human fallback, retries, duplicate handling and monitoring are not yet designed.

## Follow-ups

Unanswered follow-ups at interview end: costly-class metric priority and triage
policy, peak throughput and latency budget, labeling sample selection, persistent
reviewer disagreement and quantitative promotion criteria.

## Review notes

Interview ended after 15 minutes, as reported by the user. See
[feedback](interview-feedback.md) and the [agent reference](Agent-Solution.md).
Original candidate statements below are preserved; the reference design is not
retroactively attributed to the candidate. Review again to complete the open decisions.

## Interview log — October 31, 2026

Questions and design choices attributed to the candidate are the user's own.
Interviewer answers define this fictional scenario's requirements and are
recorded separately. Interviewer clarifications and any technical guidance are recorded per exchange below.
Existing section prompts above are scaffolding, not completed design decisions.

### Opening prompt — interviewer

Design an ML-assisted system that routes incoming SaaS support tickets to
Billing, Account Access, Technical Support or General Enquiries, with human
triage for uncertain cases. The goal is to reduce manual routing work without
increasing harmful misrouting.

Assume 100,000 tickets per day, peaks at 20 times the daily average, and a target
of 95% of automated routing decisions within two seconds. Historical labels
are imperfect, and manual handling must remain available during outages.

Start by asking any questions you need to clarify the requirements.

### Clarification 1 — Misrouting examples

**Candidate:** What would be examples of misrouting?

**Interviewer:** Misrouting means assigning a ticket to a team that cannot
handle its main issue. Examples:

- Billing → Technical Support: “I was charged twice for my subscription.”
- Account Access → General Enquiries: “I’m locked out and cannot reset my password.”
- Technical Support → Billing: “My payment succeeded, but the application crashes when I open it.”

“I paid, but I still can’t access the service” is ambiguous: billing, account
permissions or a technical fault could be responsible. Human triage is an
acceptable outcome for this case and does not count as a misroute.

For this fictional exercise, a harmful misroute causes a material delay or
exposes sensitive ticket details to staff who should not see them. Errors
should be assessed by their consequences rather than weighted equally.
These are interviewer-provided requirements, not candidate design decisions.

### Clarification 2 — Existing components and implementation scope

**Candidate:** Do I need to build this routing layer from scratch, or are there
existing components I can reuse?

**Interviewer:** You may reuse existing components. For this fictional scenario,
assume the company already provides:

- Website/email ticket intake, persistent ticket storage and stable ticket IDs.
- A staff inbox with team queues, manual assignment and reassignment.
- Staff authentication and access controls.
- Historical ticket exports and logged human reroutes.
- Integration interfaces to read a ticket and update its assigned team; you may
  propose the interface for notifying your service about new tickets.

There is no existing automated classifier or trusted confidence-based routing
policy. Your scope is the classification and routing capability, its integration
with the existing product, and its operation and evaluation. You do not need to
rebuild the ticketing product or implement infrastructure primitives from scratch.

Standard libraries, pretrained models and managed infrastructure are allowed.
No vendor is required. Explain your choices and assumptions; any external
service receiving ticket content must satisfy the scenario's privacy constraints.
No working implementation is required for this interview.

These are interviewer-provided scope assumptions, not candidate design decisions.

### Clarification 3 — Ticket content and available fields

**Candidate:** What is the content of a ticket typically? What information and details does it have?

**Interviewer:** For this fictional scenario, a new ticket contains:

| Field | Description |
| --- | --- |
| ticket_id | Unique identifier assigned by the ticketing system |
| subject | Short customer-written summary |
| body | Free-text description, potentially including errors, attempted steps, order references or personal information |
| created_at | Submission timestamp |
| channel | Website or email |
| customer_account_id | Reference to the customer's account |

Only English text is in scope initially; attachments are excluded. Subject and
body together average 5 KB, but tickets can be short, vague or incomplete.
Customers are not required to supply a category, priority, error code or steps
to reproduce. Account ID is a reference, not a guarantee that billing or account
history is available in the ticket payload.

Example (invented):

```json
{
  "ticket_id": "T-10482",
  "subject": "Charged twice for October",
  "body": "I see two subscription charges for October. Can you check? My order reference is ORD-7821.",
  "created_at": "2026-10-31T14:20:00Z",
  "channel": "email",
  "customer_account_id": "A-204"
}
```

Historical records additionally contain initial/final team assignments and
assignment timestamps when available; human reroutes are logged. These are
historical outcomes, not fields whose final values are known when a new ticket
arrives. Labels may be missing or wrong.

These are interviewer-provided data assumptions, not candidate design decisions.

### Clarification 4 — Candidate requirements summary

**Candidate:** Let me make sure I understand the requirements. I need to build a classification capability that will classify and route tickets to the appropriate queue and send to human beings in certain cases. Is that correct?

**Interviewer:** Yes. Classify each incoming ticket into Billing, Account Access,
Technical Support or General Enquiries, then route it to the corresponding team
queue when automatic routing is appropriate. Otherwise, send it for human
triage. You will define and justify when human triage is needed. Manual handling
must also remain available if automated classification is unavailable.

The objective is to reduce manual routing work without increasing harmful
misrouting. The system routes tickets; it does not answer or resolve them.

### Design proposal 1 — Offline training and live classification

**Candidate (verbatim):** I will start with a simple design, and we can complexify over time. For this to work, we first need to have a classification data pipeline. As an input, it will take historical tickets from, let's say, the previous year, with human annotation or labels. The labels correspond to the queue the ticket needs to be assigned to. The output would be the label. To run that classifier, we would go through a supervised machine learning technique, taking label as an input, feeding the data over the model, and then testing it. We will need to do a split of the training data with a test and validation set to evaluate the model. And once we are happy with the model, the output of that pipeline is the serialized object or model, which we will then use in the second part of the solution, which is now running live classification on live data.

**Interviewer:** You have separated offline training from live prediction. The
training pipeline produces a model artifact; the deployed classifier predicts
a queue for each incoming ticket. One terminology clarification: labels are
training targets, not inputs available to the classifier for a new ticket.

Before moving to serving, which ticket fields would you use as model inputs,
and what metric or acceptance criterion would make you comfortable deploying
this first model?

**Assistance record:** Interviewer clarified the distinction between training
labels and prediction inputs. No model choice, split strategy or metric was
provided; final attempt outcome remains pending.

### Design proposal 2 — Input representation and evaluation metrics

**Candidate (verbatim):** For model inputs, I would use the text from the body of the tickets and embed it as a vector so that we can capture the semantic meaning of the text. The metric I would use to evaluate the model performance would be a multi-class classifier evaluation metric. We would look at—we could look at accuracy, and eventually we could then look at, for each class, recall or precision, or the blended F1 score.

**Candidate decisions:** Use ticket body text, represented as an embedding
vector, as classifier input. Consider overall accuracy and per-class precision,
recall and F1. The embedding model, classifier, F1 aggregation and deployment
acceptance thresholds have not yet been specified.

**Interviewer:** Suppose 80% of historical tickets belong to Technical Support.
A classifier that sends every ticket there achieves 80% accuracy. Would that be
acceptable? Given our goal of avoiding harmful misrouting, how would you use
your proposed per-class metrics to decide whether the model is ready?

The 80% class distribution is a hypothetical interviewer probe, not a measured
property of the provided dataset. No metric choice or threshold was supplied.

### Design proposal 3 — Evaluation under class imbalance

**Candidate (verbatim):** We need to address potentially imbalanced data. In this case, 80% go to technical support, shows a lot of data for that particular class. To address that, we can instead look at binary classification evaluation metric for each class and see within each class if we got it right or wrong, and again use recall or precision.

**Candidate decision:** Evaluate each class separately using a one-vs-rest
view, with per-class precision and recall, so aggregate accuracy does not hide
poor results on minority classes. This is an evaluation approach; no change to
the training algorithm or class sampling has been proposed. The 80% figure
remains a hypothetical interviewer scenario.

**Interviewer:** Yes—evaluate each queue against all the other queues. Consider
Billing: precision measures how often tickets predicted as Billing truly belong
there; recall measures how many actual Billing tickets are identified.

Suppose an actual Billing ticket sent elsewhere is especially costly. Which
metric would you prioritize for Billing, and how would human triage fit into
that decision?

**Assistance record:** Interviewer confirmed the one-vs-rest interpretation and
clarified precision versus recall. The candidate has not yet chosen a priority,
an acceptance threshold or a human-triage policy.

### Design proposal 4 — Live inference, buffering and resilience

**Candidate (verbatim):** As for the second live pipeline for live inference, we could use a cloud-based infrastructure like AWS, host the classifier in SageMaker batch inference, or in some other compute like ECS or EKS with a REST API on top. And as tickets come in, a message could be dropped in a queue, and then we have a polling mechanism pulling from the queue with SQS, calling the model, getting back the class, dropping that back into the queue, and we could have then another poller that reads the ticket ID and the class and then writes it to the appropriate queue. The queue allows us to handle spikes of traffic without overwhelming the downstream compute. As for the downstream compute, it can massively scale horizontally, so that should not be an issue. As for the rest of non-functional requirement, we can look at resiliency across regions, active-passive or active-active setup.

**Candidate proposal:**
- AWS-based model hosting: SageMaker batch inference or ECS/EKS behind a REST API; final choice pending.
- Incoming ticket → message queue → inference worker → model prediction → result message → routing worker → destination team queue.
- Result messages contain ticket ID and predicted class.
- Use SQS polling and buffering to absorb traffic spikes and protect downstream compute.
- Horizontally scale serving compute; sufficient scaling capacity is currently an assumption, not yet supported by estimates.
- Consider active-passive or active-active regional resilience; no selection made yet.

Whether prediction results use a separate queue from incoming work has not yet
been clarified. Human triage criteria, retries and duplicate handling remain open.

**Interviewer:** Your proposed flow separates intake, inference and routing.
Let's examine the two-second target before adding regional complexity. At
100,000 tickets per day and a peak of 20 times the average, what peak arrival
rate do you expect? How would you allocate the two-second budget across queue
waiting, model inference and the routing update? Given that budget, would you
choose batch inference or an online model endpoint, and why?

**Assistance record:** Interviewer requested capacity estimates and justification
of the serving choice against the existing latency requirement. No throughput
calculation, serving choice or scaling policy was supplied.

### Design proposal 5 — Feedback loop and periodic retraining

**Candidate (verbatim):** Let's now talk about the feedback loop, or the tickets that were sent to human beings. We can use that dataset to refit the model with that new data, doing again the split between training data and test data, and again evaluate on the same precision or recall metric how the classifier performs with that additional data. And this can become a weekly or monthly type of refitting job to keep the model performing as new tickets come in. If a new class needs to be added, that will go through a training job, but if we keep the same classes and just the data change, that's fitting.

**Candidate proposal:** Use human-triaged tickets and their resulting labels as
additional data for model updates. Split data for training and testing, evaluate
precision/recall again, and run updates weekly or monthly. Adding a new class
requires updating the model. The exact schedule, dataset composition, validation
split and release criteria remain undecided.

**Interviewer clarification:** Fitting is the process of training a model on
data. Updating it with new data for the same classes is still retraining or
refitting; adding a class changes the label set and may also require changes to
the classifier and downstream routing. The terms do not distinguish those two
scenarios. Whether an update starts from scratch or continues from an existing
model is a separate choice.

**Interviewer probe:** Human-triaged tickets may be disproportionately ambiguous
or difficult. If your new evaluation set consists only of those tickets, how
would you know the updated model improves performance on all incoming tickets,
including those routed automatically? How would you compare the current and
candidate models before replacing the current one?

**Assistance record:** Interviewer clarified fitting/training terminology and
highlighted possible selection bias in human-triage data. Candidate evaluation
and release strategy is pending. Earlier latency/capacity questions remain open.

### Design proposal 6 — Champion–challenger shadow evaluation

**Candidate (verbatim):** To evaluate a new model against an existing, we can follow the champion challenger model and send a copy of the incoming tickets in shadow to the new model and evaluate both and only promote from challenger to champion the new model if it performs.

**Candidate decision:** Keep the current model as champion and send copies of
incoming tickets to the challenger in shadow. Compare their performance and
promote the challenger only if it meets the performance requirements. Exact
promotion thresholds and evaluation duration have not yet been defined.

**Interviewer:** In this setup, the champion controls live routing while the
challenger records predictions without changing ticket assignments. Running
both on the same traffic gives you comparable predictions, but those predictions
alone do not establish which model is correct.

How would you obtain trustworthy ground-truth labels for this comparison,
particularly for automatically routed tickets that nobody reassigns? What
specific evidence would you require before promoting the challenger?

**Assistance record:** Interviewer clarified shadow-mode behavior and the need
for ground truth. Label collection and promotion criteria remain candidate
choices; no specific implementation was supplied.

### Design proposal 7 — Ground-truth labeling and reviewer agreement

**Candidate (verbatim):** Ground truth data would be obtained by running these tickets through data scientists or data analysts, and we can do that through two or three passes to double check that the label is as correct as possible. We could feed the same ticket to two or three or four labelers in parallel and do a blended review and assign labels that have the majority vote, and those that don't go back to the labeling queue.

**Candidate proposal:** Have data scientists or analysts independently review
tickets, using repeated passes or two to four parallel labelers. Assign a
majority-vote label and return tickets without agreement to the labeling queue.
The number of reviewers, sampling volume, labeling instructions and final
resolution process remain to be defined. Majority agreement improves confidence
but has not been established as proof of correctness.

**Interviewer probe:** At 100,000 tickets per day, reviewing every ticket several
times could be expensive. What subset would you send for labeling so the
champion–challenger comparison remains representative and affordable? If a
ticket repeatedly fails to get a majority, who makes the final decision—or
how would you represent it if no single queue is clearly correct?

**Assistance record:** Interviewer requested a sampling strategy and a bounded
resolution process for persistent disagreement. No sampling method or
adjudication policy was supplied.

### Session end

The candidate ended the interview and reported spending **15 minutes**. A worked
agent solution and a comparison were requested after the attempt. This is recorded
as a partial attempt, not a completed independent or guided solve.
