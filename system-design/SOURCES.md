# AI system design preparation sources

Research checked October 25, 2026. Recommendations are an editorial assessment of publicly accessible material, not a claim that every paid lesson was reviewed. Company-style exercises are not verified past FAANG questions unless a source explicitly establishes that provenance.

## Recommended starting combination

Start free with AI Interview Hub for applied GenAI cases, Hello Interview for interview delivery, and AIMLInterviews for classical ML coverage. Use the local [practice queue](TRACKER.md) to order exercises by theme and difficulty. Add one paid resource only after a sample addresses a specific gap.

System design has multiple defensible answers. Look for assumptions, alternatives, calculations, evaluation criteria, and failure handling rather than one supposedly correct architecture.

## Comparison

| Source | Access | Exercises and guidance | Organization and best use | Limits |
| --- | --- | --- | --- | --- |
| [AI Interview Hub / Awesome Generative AI Guide](https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/interview_prep/README.md) | Free | 10 worked design cases; includes engineer writeups, follow-ups and linked code | Grouped by application; useful for RAG, agents, document workflows, voice and coding assistants | No uniform Easy/Medium/Hard ladder; linked code was not executed in this review |
| [Hello Interview: ML System Design](https://www.hellointerview.com/learn/ml-system-design/in-a-hurry/introduction) | Free core; premium depth | Framework, concepts and visible breakdowns for harmful content, bots and video recommendations | Best concise starting point for interview structure and applied ML | ML guide is marked early access; not a large GenAI question bank |
| [AIMLInterviews](https://github.com/alirezadir/AIMLInterviews/blob/main/src/MLSD/ml-system-design.md) | Free | Nine-step framework, topic-grouped prompts and references | Useful coverage checklist across recommendations, search, ML and GenAI | A prompt/reference collection does not mean every question has a complete worked answer; no consistent difficulty ranking |
| [ByteByteGo: Generative AI System Design Interview](https://blog.bytebytego.com/p/our-new-book-generative-ai-system) | Paid book/course; sample content available | 10 in-depth cases and diagrams, including RAG, ChatGPT, translation and image/video generation | Best book-style deep dives; pair with its classical ML material if that is a target | Includes substantial model-development content; less focused on everyday LLM application architecture than some engineers need |
| [Design Gurus: Grokking the AI System Design Interview](https://www.designgurus.io/course/grokking-the-ai-system-design-interview) | Paid; free previews and [companion index](https://github.com/design-gurus/grokking-ai-system-design) | 70 lessons, capstones and worked case studies covering ML, RAG, inference, GenAI products and agents | Broad topic progression; advertised study time 20 hours | Lesson/assessment counts are not unique design-question counts. Free companion explicitly points to the paid course for full worked designs |
| [Educative: Grokking the Generative AI System Design](https://www.educative.io/courses/generative-ai-system-design) | Paid; public syllabus | 39 lessons, 23 quizzes, five modality-oriented systems and four advertised AI mock interviews | Structured foundations and framework; text, image, speech and video coverage | Smaller case selection; not a large ranked exercise bank. These Grokking courses are separate products from Design Gurus |

## Cost and review evidence

- **Free-first:** the three free resources above are enough to begin deliberate practice. GitHub popularity is a discovery signal, not proof of correctness or interview success.
- **ByteByteGo:** the [pricing page](https://bytebytego.com/pricing) shows yearly and lifetime options; a reliable numeric price was not exposed in the fetched page. For a short preparation period, compare the individual book price with the online plan. [Goodreads](https://www.goodreads.com/en/book/show/221577013-generative-ai-system-design-interview) showed 3.92/5 from 36 ratings: readers praise the framework but some find cases repetitive or too high-level. That is modest, mixed evidence, not overwhelming endorsement.
- **Design Gurus:** the [catalog](https://www.designgurus.io/courses) listed the AI course at $99; the course page describes one-time lifetime access and displays 4.6/5 from 661 ratings. Those ratings are provider-hosted, and the testimonials shown include other courses. I did not establish a broad independent review consensus for this specific AI course. Sample it before purchasing; verify checkout price.
- **Educative:** the course page displays 4.6/5, but the fetched page did not establish the rating count or a dependable current price. This is provider-hosted evidence. Choose it if you want its learning format, after checking the actual subscription term and included course access.
- **Hello Interview:** the [pricing page](https://www.hellointerview.com/pricing) displayed $47 for one month and $89 for one year, with no auto-renewal. Prices may change. Its advertised guided-practice counts cover several interview categories, not just AI/ML design; do not purchase assuming dozens of GenAI walkthroughs.

## Additional breadth, with lower confidence

[ML/AI System Design Handbook](https://github.com/shantam21/ml-ai-system-design-handbook) advertises 46 worked designs across classical ML, ML platforms, GenAI and agents. It is worth browsing for extra prompts, but its public page showed little adoption evidence at review time. I have not audited all designs; use it as a supplement and cross-check technical claims.

## How to select an answer worth studying

Use this original checklist when comparing explanations:

1. Does it specify the product goal, users, constraints and a simple baseline?
2. Does it explain data access, quality, ingestion and update paths?
3. Does it justify model/retrieval choices and viable alternatives?
4. Does it define offline evaluation, online success and failure thresholds?
5. Does it quantify traffic, latency, storage and inference cost with assumptions?
6. Does it address permissions, unreliable tools, degradation and recovery?
7. Can you explain the design without copying its diagram?

For public repository notes, write original prompts, summaries and agent solutions with links to learning sources. Preserve attribution for imported material; link to paid walkthroughs rather than copying their chapters or diagrams.
