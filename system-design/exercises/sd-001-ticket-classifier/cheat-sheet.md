# My cheat sheet — Classification and model evaluation

## One-vs-rest evaluation

For a multi-class classifier, evaluate each queue separately: treat that queue
as the positive class and all other queues as the negative class. This evaluates
the existing classifier; it does not require training separate binary models.

For **Billing**:

- **Precision:** Of tickets predicted as Billing, how many actually belong there?
- **Recall:** Of all actual Billing tickets, how many did we identify?

## My recall mnemonic

**RecAll → A → Actual**

Of **all actual Billing tickets**, how many did we identify?

Precision starts with the **predicted** Billing tickets; recall starts with the
**actual** Billing tickets.

## Formulas

- **TP:** Actual Billing ticket predicted as Billing.
- **FP:** Non-Billing ticket predicted as Billing.
- **FN:** Actual Billing ticket predicted as another queue.

**Precision = TP / (TP + FP)**

**Recall = TP / (TP + FN)**

Example: 100 tickets actually belong to Billing. We predict Billing for 80
tickets, of which 60 really belong there:

- Precision: 60 / 80 = **75%**.
- Recall: 60 / 100 = **60%**.

These definitions describe the classifier's predictions. When adding human
triage, define separately how deferred tickets count in end-to-end evaluation.

## Training, validation and test splits

**Train = learn. Validation = choose. Test = check the final choice.**

| Dataset | Purpose | What I do with it |
| --- | --- | --- |
| Training | Learn model parameters | Fit the classifier and any learned preprocessing |
| Validation | Make development decisions | Choose model type, hyperparameters, early stopping, calibration and routing thresholds |
| Test | Estimate performance after choices are frozen | Evaluate the final model/policy on unseen examples; do not tune against the results |

An illustrative split is **70% training / 15% validation / 15% test**. These
percentages are a starting point, not a rule. Each evaluation set needs enough
examples of rare classes to support useful conclusions.

### How I would split support tickets

Because we deploy on future tickets, use **chronological windows** rather than
randomly mixing past and future data. For example, with one year of history:

1. **January–August:** training.
2. **September–October:** validation.
3. **November–December:** final held-out test.

These are illustrative windows, not exact 70/15/15 proportions. Choose boundaries
using ticket counts, label availability and changes in the business.

Before fitting:

- Use the subject/body as they existed at arrival, not later replies or resolution details.
- Keep duplicate tickets and related conversation records out of different splits.
  For threads crossing a time boundary, exclude overlapping records from the later
  evaluation window or use a boundary gap; do not move future records into training.
- Use only labels available by the simulated training date. Allow evaluation
  labels time to mature before scoring predictions.
- Fit TF-IDF vocabulary, scaling, feature selection and other learned transforms
  on training data only, then apply the frozen transforms to validation/test data.
  A frozen pretrained encoder may encode every split; any task-specific fine-tuning
  must use training data, not the test set.

For independent examples with no time-related deployment concern, a random,
**stratified** split can preserve class proportions. Use a fixed random seed
for reproducibility. If examples share a patient, document or conversation,
consider group-based splits. For a chronological evaluation, retain the actual
later-period distribution rather than forcing it to match historical proportions.

### Development workflow

1. Set aside the test set before model development.
2. Train candidate models on training data.
3. Compare candidates and choose thresholds using validation data.
4. Freeze the chosen model, preprocessing and routing policy.
5. Evaluate on the test set and report overall and per-class metrics.

If test results lead me to redesign the model, that test set has influenced
selection: treat it as development data and obtain a fresh final holdout.
Repeatedly picking the winner on the same test set makes the reported result
optimistic.

For this exercise, keep the selected trained artifact for the first evaluation.
If I later refit on training + validation data, the model has changed; I must
plan separate calibration/threshold data and evaluate that actual final artifact.
Do not assume old confidence thresholds transfer unchanged.

### Holdout versus validation

**Holdout describes separation; validation describes a purpose.**

- A **holdout set** is data deliberately set aside from model fitting.
- A **validation set** is often one such holdout, used to guide development.
- A **held-out test set** is kept separate from both fitting and development
  decisions until final evaluation.

People sometimes say “holdout” when they mean the final test set. Clarify:
**“Do you mean a validation holdout for tuning, or an untouched test holdout?”**

A held-out validation set is unseen by parameter fitting but still influences
model selection. It is therefore not an independent final test.

### Where cross-validation fits

Cross-validation uses several training/validation folds to compare choices
more robustly. Keep a separate final test set. For tickets evolving over time,
use forward-looking folds: train on earlier data and validate on later data,
without training on the future. Cross-validation complements a final holdout;
it does not automatically replace it.

## Related notes

- [My interview solution](my-solution.md)
- [Problem description](problem-description.md)
