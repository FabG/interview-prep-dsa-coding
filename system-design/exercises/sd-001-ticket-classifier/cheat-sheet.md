# My cheat sheet — Classification and model evaluation

## 1. One-vs-rest evaluation

For a multi-class classifier, evaluate each queue separately: treat that queue
as the positive class and all other queues as the negative class. This evaluates
the existing classifier; it does not require training separate binary models.

For **Billing**:

- **Precision:** Of tickets predicted as Billing, how many actually belong there?
- **Recall:** Of all actual Billing tickets, how many did we identify?

## 2. My recall mnemonic

**RecAll → A → Actual**

Of **all actual Billing tickets**, how many did we identify?

Precision starts with the **predicted** Billing tickets; recall starts with the
**actual** Billing tickets.

## 3. Formulas

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

## 4. Training, validation and test splits

**Train = learn. Validation = choose. Test = check the final choice.**

| Dataset | Purpose | What I do with it |
| --- | --- | --- |
| Training | Learn model parameters | Fit the classifier and any learned preprocessing |
| Validation | Make development decisions | Choose model type, hyperparameters, early stopping, calibration and routing thresholds |
| Test | Estimate performance after choices are frozen | Evaluate the final model/policy on unseen examples; do not tune against the results |

An illustrative split is **70% training / 15% validation / 15% test**. These
percentages are a starting point, not a rule. Each evaluation set needs enough
examples of rare classes to support useful conclusions.

### 4.1 How I would split support tickets

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

### 4.2 Development workflow

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

### 4.3 Holdout versus validation

**Holdout describes separation; validation describes a purpose.**

- A **holdout set** is data deliberately set aside from model fitting.
- A **validation set** is often one such holdout, used to guide development.
- A **held-out test set** is kept separate from both fitting and development
  decisions until final evaluation.

People sometimes say “holdout” when they mean the final test set. Clarify:
**“Do you mean a validation holdout for tuning, or an untouched test holdout?”**

A held-out validation set is unseen by parameter fitting but still influences
model selection. It is therefore not an independent final test.

### 4.4 Where cross-validation fits

Cross-validation uses several training/validation folds to compare choices
more robustly. Keep a separate final test set. For tickets evolving over time,
use forward-looking folds: train on earlier data and validate on later data,
without training on the future. Cross-validation complements a final holdout;
it does not automatically replace it.

## 5. SMOTE and imbalanced datasets

**SMOTE = Synthetic Minority Over-sampling Technique.** It creates synthetic
feature vectors by interpolating between nearby examples of the same class:

`synthetic = x + alpha * (neighbor - x)`, where `0 <= alpha <= 1`.

It changes the training data; one-vs-rest metrics evaluate predictions.

### 5.1 Techniques to recognize

| Technique | Idea | Tradeoff |
| --- | --- | --- |
| SMOTE | Interpolate same-class neighbors | Can create overlap or amplify noisy examples |
| Borderline-SMOTE | Focus on boundary examples | Emphasizes difficult cases, potentially including noise |
| KMeans-SMOTE | Cluster before interpolation | Adds clustering choices and computation |
| SMOTENC | Handle mixed numerical/categorical features | Requires identifying categorical columns |
| SMOTEN | Handle categorical-only features | Not the method for dense text embeddings |
| ADASYN (related method) | Generate more samples in difficult neighborhoods | Can overemphasize outliers |

SMOTE provides variation beyond duplicating rows, but synthetic samples are not
new independently observed evidence. It can help minority recall without
guaranteeing better precision or overall performance.

Source: [imbalanced-learn oversampling guide](https://imbalanced-learn.org/stable/over_sampling.html), checked October 31, 2026.

### 5.2 Avoid leakage

**Split first; resample training data only.** Keep validation and test sets at
their natural distributions. In cross-validation, run SMOTE separately inside
each training fold, preferably through an imbalanced-learn pipeline. Never
resample the full dataset before splitting: synthetic examples can incorporate
information from future validation/test records.

Tune the oversampling amount and neighbor count using validation results.
There must be enough same-class training examples for the chosen neighbors,
including within each fold. Full class balance is not automatically optimal.

Source: [imbalanced-learn leakage guidance](https://imbalanced-learn.org/stable/common_pitfalls.html), checked October 31, 2026.

### 5.3 My decision checklist for ticket classification

This is a design recommendation to validate experimentally:

- **Start with alternatives:** compare the original baseline, class-weighted
  training and random oversampling before adding synthetic interpolation.
  Class weights avoid creating extra rows; random oversampling preserves real
  examples but can overfit duplicates. Undersampling saves work but discards
  potentially useful majority-class examples.
- **Text caveat:** SMOTE acts on numerical features, not raw ticket text. A
  synthetic embedding between two tickets is not necessarily a meaningful
  ticket. Nearest-neighbor quality in high-dimensional representations must be
  checked; do not assume semantic interpolation is valid.
- **Quality first:** fix mislabeled examples before generating more around them.
  Interpolation cannot supply missing real-world diversity for a rare class.
- **Costs:** more rows mean additional training time and memory. This does not
  inherently increase inference cost for a fixed-size classifier, though the
  effect depends on the chosen model.
- **Routing impact:** altered training class proportions can affect probability
  calibration. Recheck confidence and human-triage thresholds on representative,
  unresampled validation data.
- **Success criterion:** compare per-class precision/recall, macro-F1, harmful
  misroutes and automatic coverage. A recall gain that causes too many harmful
  false positives may be unacceptable.

**Interview phrasing:** “I would compare class weighting with SMOTE on the
training partition, and keep it only if representative validation shows a useful
improvement in our error-versus-coverage tradeoff.”

## 6. Logistic regression for multiclass classification

Despite its name, logistic regression is a **classifier**. Binary logistic
regression turns a linear score into a probability using the sigmoid function.
With more than two classes, there are three common approaches.

Our example has **K = 4** mutually exclusive destinations: Billing, Account
Access, Technical Support and General Enquiries.

### 6.1 One-vs-Rest (OvR): each class versus everyone else

Train **K binary classifiers**. For our queues, train Billing vs non-Billing,
Account Access vs all others, Technical Support vs all others, and General
Enquiries vs all others. Choose the highest-scoring class for a single-label
prediction.

Advantages: modular, easy to inspect and parallelize. Tradeoffs: each binary
problem may be imbalanced, and independently produced probabilities need not
sum to one before normalization.

### 6.2 One-vs-One (OvO): every pair competes

Train **K(K − 1)/2 binary classifiers**, each using only its two classes.
Four queues require **6 classifiers**. Aggregate pairwise votes, with a
score-based rule for ties.

Advantages: smaller pairwise training problems. Tradeoffs: quadratically many
models as K grows; combining votes into meaningful multiclass probabilities
requires additional machinery.

**Mnemonic: OvR = everyone else; OvO = pairs.**

These are training strategies. **One-vs-rest evaluation** can assess any
multiclass model, including a multinomial model; it does not imply OvR training.

Source: [scikit-learn multiclass strategies](https://scikit-learn.org/stable/modules/multiclass.html), checked October 31, 2026.

### 6.3 Multinomial logistic regression: all classes learned jointly

Train **one joint model** with a score for each class, using multiclass
cross-entropy. Softmax converts those scores into probabilities:

`P(class = k | x) = exp(score_k) / sum_j exp(score_j)`

where `score_k = weights_k · x + bias_k`.

The probabilities sum to **1**. Choose the largest probability for the predicted
class. There are class-specific weights, even though this is one joint model.

Advantages: directly models mutually exclusive outcomes and produces one
normalized probability distribution. Tradeoffs: optimization couples the
classes; linear scores may miss complex feature relationships. Probabilities
summing to one does **not** guarantee they are calibrated.

Source: [scikit-learn logistic regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression), checked October 31, 2026.

### 6.4 My choice for the ticket exercise

I would start by testing **multinomial logistic regression** on TF-IDF features
or frozen embeddings: there are only four destinations, and we need one initial
queue per ticket. OvR is a reasonable comparison; OvO adds pairwise bookkeeping
that I would justify with measured gains before adopting it.

This is a proposed baseline, not a guarantee of better performance. Compare
per-class precision/recall and error-versus-coverage on validation data.
Regardless of method, retain human triage when the prediction is insufficiently
reliable. A model selecting one class does not mean the system must auto-route it.

## 7. Related notes

- [My interview solution](my-solution.md)
- [Problem description](problem-description.md)
