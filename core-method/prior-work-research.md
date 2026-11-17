# Prior work: how much of this project has been done before?

12 Nov 2026. A literature search on what this project actually tests, separate from [seed-sources-research.md](seed-sources-research.md) (where seeds come from) and [review-areas-research.md](review-areas-research.md) (which areas seats cover). It doesn't change the experiment plan.

**What the project tests, for judging closeness:**
- several LLM reviewer agents in seats with roles;
- a judge that keeps or dismisses findings and sets severity, and a second agent that can appeal the judge's dismissals;
- scoring against planted bugs, with an outside-family judge for matching;
- council configurations that compete and advance over rounds;
- role sets compared at equal cost (A, B, C and one generalist with an ISO checklist);
- the risk that the reviewers, the code's author and the seed writer are all Claude.

**How the search was done:**
- **The searchers:** three research agents, two topics each, searched the web and fetched each paper's own page:
  - the arXiv abstract page or full text;
  - the ACL Anthology, PMLR, ICML and ICLR proceedings pages;
  - conference listings on researchr.
- **Sites that failed:** IEEE Xplore returned an empty page (Hydra-Reviewer); Semantic Scholar and dblp blocked the fetch; Google Scholar wasn't searched. So this isn't a full search of every listing named in the brief.
- **Fetch summaries:** every page was read through a fetch tool, so what was seen was a summary of the page with quotes. Figures need a second look before the paper cites them.
- **Rechecks:** I checked 11 papers' arXiv pages myself, and all matched the agents' notes on title, authors, dates and headline numbers. They are marked **(rechecked)**.
- **Read labels:** each entry says whether the abstract page or the full text was read. Anything seen only in search snippets is marked *(snippet only)*.
- **Peer review:** most of this work is from 2025–2026 and many papers are unrefereed preprints. A venue is given only where the paper's own page or the proceedings state it.

## 1. Multi-agent LLM code review

### RevAgent: Issue-Oriented Agent-Based Framework for Automated Review Comment Generation (rechecked)
- **Paper:** Shuochuan Li, Dong Wang, Patanamon Thongtanunam, Zan Wang, Jiuqiao Yu and Junjie Chen; arXiv preprint, 1 Nov 2025; [arXiv 2511.00517](https://arxiv.org/abs/2511.00517). Full text read.
- **Tested:** five fine-tuned commentator agents, one per issue category (refactoring, bug fix, testing, logging and documentation), plus a critic that picks the best issue and comment. Scored against human comments: BLEU +12.90%, ROUGE-L +10.87%, METEOR +6.32% and SBERT +8.57% over the best baseline.
  - Its ablation beats a single agent fine-tuned on all categories, at about 8.7 times LLaMA-Reviewer's tokens (full text).
- **Closeness: medium-high.** It has category specialists and a critic as judge, and the specialists beat a single agent.
- **Differences:**
  - the critic picks one comment instead of pooling findings;
  - there is no appeal;
  - it is scored by similarity to human comments, not planted bugs;
  - the role set isn't varied and cost isn't matched.

### Hydra-Reviewer: A holistic multi-agent system for automatic code review comment generation
- **Paper:** Xiaoxue Ren, Chaoqun Dai, Qiao Huang, Ye Wang, Bo Jiang and Chao Liu.
  - **Venue:** IEEE Transactions on Software Engineering, 2025, issue 12. This is from the IEEE Computer Society listing (path `ts/2025/12/11203269`), seen via search only. It was also presented in the [FSE 2026 Journal-First track](https://conf.researchr.org/details/fse-2026/fse-2026-journal-first/40/Hydra-Reviewer-A-holistic-multi-agent-system-for-automatic-code-review-comment-gener).
  - **Read:** abstract read (pasted by the researcher from the IEEE page, 12 Nov 2026). ~~Only the listing was read: IEEE Xplore (document 11203269) returned an empty page and no preprint was found.~~ The full text still isn't accessible; I'm requesting a copy from the first author.
- **Tested:** agents built around a taxonomy of review dimensions from an empirical study, with context retrieval and reflection.
  - **Motivation:** the authors name three limitations of existing automated code review: lack of comprehensiveness, incorrectness and vagueness.
  - **Evaluation:** on CodeReview, CodeReviewNew and a new dataset of their own, against CodeReviewer, LLaMA-Reviewer, ChatGPT, Comprehensive-ChatGPT and DeepSeek-V3. Each component is ablated, and there is a user study.
  - **Results:** BLEU 8.20 against 7.85 for DeepSeek-V3, 7.8 dimensions covered per comment, and $0.018 and 62.63 s per change.
  - **The taxonomy's dimensions** aren't listed in the abstract.
- **Closeness: medium.** Its dimension-based agents are the nearest thing to seat roles chosen from a taxonomy. It is scored by BLEU, and whether its ablation compares role sets couldn't be checked.
- **How it bears on the project:**
  - **Its three limitations map onto parts of the council:**
    - comprehensiveness onto seat coverage;
    - incorrectness onto the judge, the appeal and the checks;
    - vagueness onto the findings format, which asks for the file, the line and the evidence (as in Lite's reviewer, judge and appeal briefs).
  - **Its BLEU gain** (8.20 against 7.85) measures similarity to human comments, not bugs caught.
  - **Its ablation** is the part to read for the question of folding areas into existing seats against giving them seats of their own.

### CodeAgent: Autonomous Communicative Agents for Code Review
- **Paper:** Xunzhu Tang et al. (9 authors); EMNLP 2024 main conference; [arXiv 2402.02172](https://arxiv.org/abs/2402.02172) (v1 3 Feb 2024, v5 24 Sep 2024). Full text read, except the appendices.
- **Tested:** six company-style roles plus a QA-Checker that keeps agents on the question, across four review tasks.
  - **Vulnerability detection:** 449 of 483 flags were confirmed by hand after the fact (92.96%), against 51.42% for GPT-4. Without the QA-Checker the figure falls to 73.23%.
- **Closeness: medium-low.** It has a supervisor, but the roles are company roles, there is no answer key set in advance and no role-set comparison.

### Adversarial Review: Structured Disagreement for Grounded Agentic Code Review (rechecked)
- **Paper:** Eric S. Qiu and Joyce Gill; ICML 2026 DL4C workshop; [arXiv 2608.18167](https://arxiv.org/abs/2608.18167) (16 Aug 2026). Full text mostly read.
- **Tested:** a main agent, a reviewer and a critic that audits the review. It was compared with one reviewer, two reviewers and a five-agent baseline (MARS).
  - **SWE-PRBench** (100 real PRs, human comments as ground truth, a GPT-5.2 judge with kappa 0.75): the first protocol showed "false consensus" (F1 0.457). Requiring evidence for disagreement gave 0.533, against 0.495–0.503 for the others.
  - **Headline finding:** more independent reviewers didn't reliably help.
- **Closeness: medium-high.** It compares reviewer counts and structures in code review, and the critic is a rough analogue of an appeal.
- **Differences:** the reviewers aren't specialised, there is no planted-bug key and cost isn't matched.

### Using Agentic AI for contextualized and multifaceted code review at Ericsson
- **Paper:** Muhammad Laiq, Ricardo Britto, Muhammad Usman, Nishrith Saini and Deepika Badampudi; PROFES 2026; [arXiv 2609.15877](https://arxiv.org/abs/2609.15877) (14 Sep 2026). Full text read.
- **Tested:** an orchestrator picks among four dimension agents (readability, maintainability, reliability and performance) and merges their output. Developers judged 96% of 206 issues correct and about 69% important.
- **Closeness: medium.** Its seats are close to options B and C. There is no generalist baseline, no role-set ablation and no answer key.

### VulTrial: Let the Trial Begin: A Mock-Court Approach to Vulnerability Detection using LLM-Based Agents
- **Paper:** Ratnadira Widyasari et al. (9 authors); ICSE 2026, according to the full text and the DOI 10.1145/3744916.3773256; [arXiv 2505.10961](https://arxiv.org/abs/2505.10961) (v1 16 May 2025, v2 3 Dec 2025). Full text mostly read.
- **Tested:** prosecutor, defence, moderator (judge) and review board (jury) agents on PrimeVul vulnerable and benign pairs, a known-label key. With GPT-4o it got 81 pairs correct, against 44 for GPTLens.
  - **Role ablation:** removing the moderator drops a configuration from 96 to 32. One debate round works best.
- **Closeness: medium-high.** It has a judge, adversarial roles, a role ablation and a known-label key.
- **Differences:** it classifies functions as vulnerable or not instead of combining review findings, there is no appeal of dismissals and no equal-cost control.

### GPTLens and MAVUL
- **[GPTLens](https://arxiv.org/abs/2310.01152):** Sihao Hu et al., IEEE TPS 2023 (abstract page read). An auditor generates candidate vulnerabilities and a critic filters false positives. It is the original generate-then-judge design for code findings.
- **[MAVUL](https://arxiv.org/abs/2510.00317):** Youpeng Li et al., IEEE TPS 2025 (abstract page read). An analyst, an architect and an evaluation judge on a pairwise known-label set.
- **Closeness: medium** and **medium-low.** Each has a judge-like filter, with no role sets or appeal.

### MultiVer and CodeX-Verify (both Shreshth Rajan)
- **[MultiVer: Zero-Shot Multi-Agent Vulnerability Detection](https://arxiv.org/abs/2602.17875)** (arXiv, 19 Feb 2026; full text read):
  - **Tested:** four agents (security, correctness, performance and style) combined by union voting with Claude Opus 4.5. On PyVul, recall was 82.7% and precision 48.8%. Security alone loses 17 points of recall.
  - **Caveat:** the style agent never calls the LLM.
- **[CodeX-Verify: Multi-Agent Code Verification via Information Theory](https://arxiv.org/abs/2511.16708)** (arXiv, v1 20 Nov 2025, v3 3 Dec 2025; full text read; v1 had a different title):
  - **Tested:** all 15 combinations of four agents on 29 samples. Correctness plus performance (79.3%) beat all four.
  - **Caveat:** the "agents" are static analysers, not LLMs, and the weights were tuned on the same data.
- **Closeness: medium.** These are the only role-set comparisons against labelled bugs found. Neither uses a generalist baseline or matches cost, and CodeX-Verify isn't LLM review at all.

### OpenCodeReview and BitsAI-CR: production pipelines with a filter
- **[OpenCodeReview: Determinism over Non-Determinism for Cost-Effective Agent-Based Code Review](https://arxiv.org/abs/2608.09290)** (rechecked): Zhengfeng Li et al. (11 authors, Alibaba), arXiv, 10–11 Aug 2026. Full text read.
  - **Tested:** parallel sub-agents, then a reflection filter that sees only the diff and removes hallucinated comments. On AACR-Bench it reached up to 2.17 times the SEM-F1 of Claude Code and Codex (25.10% against 11.57%), with 5–15 times fewer tokens.
  - **The filter is delete-only:** it fails open on a parse error, nothing restores what it deletes and it isn't ablated on its own (full text).
- **[BitsAI-CR: Automated Code Review via LLM in Practice](https://arxiv.org/abs/2501.15134):** Sun et al. (12 authors, ByteDance), arXiv 25 Jan 2025, FSE 2025 Industry *(venue from a snippet)*. Abstract page read.
  - **Tested:** a rule checker flags issues and a review filter verifies them, for 75.0% precision.
- **Closeness: high on structure** (parallel reviewers plus a judge-like filter), with no appeal, no severity judge and no planted bugs.

### Lower relevance (abstract pages read)
- **[Multi-role Consensus for Vulnerability Detection](https://arxiv.org/abs/2403.14274):** Mao et al. 2024. Developer and tester roles reach consensus, with F1 +16.13% over a single role.
- **[RepoReviewer](https://arxiv.org/abs/2603.16107):** 2026, a systems paper with no benchmark.
- **[Kamalı et al.](https://arxiv.org/abs/2605.17548):** 2026, a vision paper.
- **[DeputyDev](https://arxiv.org/abs/2509.19708):** 2025, productivity only; its six specialised agents are *(snippet only)*.

## 2. Role design for reviewer agents

### MARG: Multi-Agent Review Generation for Scientific Papers
- **Paper:** Mike D'Arcy, Tom Hope, Larry Birnbaum and Doug Downey; arXiv preprint, 8 Jan 2024; [arXiv 2401.04259](https://arxiv.org/abs/2401.04259). Full text read.
- **Tested:** specialist agents for experiments, clarity and impact (MARG-S), against a generic multi-agent version, single agents and each specialist alone.
  - **Recall:** 15.84 for the specialists, 8.49 for the generic team, 10.62 for the best single agent and 3.25–8.88 for each specialist alone.
  - **Cost:** the specialists used about 1.24M input tokens against about 135k for the generic team.
- **Closeness: high on design.** It is the clearest specialists-against-generic-against-single comparison, with each specialist ablated.
- **Differences:** it reviews papers, not code, there is no planted key and the cost is about nine times higher for specialists. The generic team did worse than a tuned single agent.

### ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate
- **Paper:** Chi-Min Chan et al. (8 authors); ICLR 2024 (per the [proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/25cc3adf8c85f7c70989cb8a97a691a7-Abstract-Conference.html)); [arXiv 2308.07201](https://arxiv.org/abs/2308.07201). Abstract and proceedings pages read.
- **Tested:** debating panels of evaluators. Giving every agent the same role prompt did worse than diverse roles, and no better than one agent *(ablation detail from a search summary)*.
- **Closeness: medium-high.** It shows role diversity matters in a judging panel. It evaluates text, not code, and cost isn't equal.

### Agents with Feelings? Personality and Emotion in Multi-Agent Software Teams
- **Paper:** Yunyan Ding, Thomas Zimmermann and Iftekhar Ahmed; arXiv preprint, 6 Jul 2026; [arXiv 2607.05659](https://arxiv.org/abs/2607.05659). Full text read.
- **Tested:** 78 team-profile configurations with four LLMs. Its code-review team is two writers split by quality areas plus a supervisor who merges and filters, on Hydra-Reviewer's data. Profiles change BLEU by 8.3–18.9% relative.
- **Closeness: medium-high.** It compares team configurations for code review systematically, with a supervisor as judge. But it varies personas, not seat scopes, it is scored by BLEU and cost isn't matched.

### Other role and persona studies
- **Philosophical Dispositions as Behavioral Constraints for AI-Assisted Code Review** ([arXiv 2605.23108](https://arxiv.org/abs/2605.23108); Kaushal Bansal, 2026; abstract page read):
  - **Tested:** four reviewer "dispositions" on 50 PRs. 51% of their findings weren't produced by a generic "expert reviewer" prompt on the same model.
  - **Caveat:** false positives were judged by the author alone.
  - **Closeness: medium, weak evidence.**
- **Pornprasit and Tantithamthavorn, Fine-Tuning and Prompt Engineering for LLM-based Code Review Automation** ([arXiv 2402.00905](https://arxiv.org/abs/2402.00905); 2024; abstract page read):
  - **Tested:** fine-tuning and prompt set-ups for code review. It recommends few-shot prompting *without* a persona.
  - **Closeness: medium-low.**
- **Zheng et al., personas in system prompts** (Findings of EMNLP 2024, [arXiv 2311.10054](https://arxiv.org/abs/2311.10054)):
  - **Tested:** personas didn't beat a no-persona control. Already cited in the plan and the paper.
  - **Bearing on seats:** a role label alone may not be what makes a seat work; its scope, checklist and context may matter more.

### Equal-cost and panel-size precedents
- **Tran and Kiela, Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets** ([arXiv 2604.02460](https://arxiv.org/abs/2604.02460); 2026; abstract page read):
  - **Tested:** with reasoning tokens held equal, one agent matched or beat multi-agent systems, and many reported multi-agent gains came from extra compute.
  - **Closeness: medium.** It is the key precedent for the equal-cost rule and the one-generalist arm. It isn't about review.
- **Kim et al., Towards a Science of Scaling Agent Systems** ([arXiv 2512.08296](https://arxiv.org/abs/2512.08296); abstract page read):
  - **Tested:** 260 configurations with compute controlled. Designs without central verification spread errors more.
  - **Already cited** in the plan and the paper. The agent found that the abstract now says 260 configurations, where the Google blog said 180.
- **Jung and Na, Logarithmic Scores, Power-Law Discoveries** (COLM 2026, [arXiv 2604.00477](https://arxiv.org/abs/2604.00477); abstract page read):
  - **Tested:** as persona-conditioned judge panels grow, scores level off about twice as fast as new issues are found.
  - **Closeness: medium**, on panel size against coverage.
- **ReviewAgents** ([arXiv 2503.08506](https://arxiv.org/abs/2503.08506); Gao et al., 2025; full text read):
  - **Tested:** with 1 to 6 identical paper reviewers plus an area chair, 3 reviewers did best and more didn't help.
- **Self-MoA** ([arXiv 2502.00674](https://arxiv.org/abs/2502.00674); Li et al., 2025):
  - **Tested:** repeated samples of the best single model beat mixing models.
- **Automatic team selection:**
  - **[DyLAN](https://arxiv.org/abs/2310.02170)** (COLM 2024) picks a team from an importance score after a trial run.
  - **[AgentInit](https://arxiv.org/abs/2509.19236)** (Findings of EMNLP 2025) picks teams on the trade-off between diversity and task relevance.
  - Neither is about review.

## 3. Scoring LLM code review against known or planted bugs

Builds on seed-sources-research.md, which covers ReviewBench, Martian, Qodo and Kumar et al. I found no academic paper that builds on those four.

### CRBugBench: (When) Should a Software Factory be Lights-off? Benchmarking Code Review Agents on Bug Detection (rechecked)
- **Paper:** Chenyang Yang, Hao He, Ti-Chung Cheng, Jenna Butler, Emerson Murphy-Hill, Carmen Badea and Christian Bird; arXiv preprint, 9 Oct 2026; [arXiv 2610.13668](https://arxiv.org/abs/2610.13668). Abstract page read.
- **Tested:** 1,000 review tasks from 98 open-source repositories plus 800 proprietary ones. Each is a human-verified bug paired with the PR that introduced it.
  - **Results:** the best set-up (claude-opus-5 with copilot-cli) catches 71.9% of bugs in its top 5 comments, up from 47.7% for opus-4.6.
  - **Cost:** prompts that nudge exploration gain up to 5.8% for 10% more cost.
- **Closeness: high on scoring** (real known bugs, review by reading). ~~It tests single agent set-ups, not councils, and there is no same-family analysis.~~ There is no same-family analysis. (amended 17 Nov 2026, from the full text, which Claude Code read through a fetch tool: section 4.6 and Table 3 do test multi-agent set-ups on gpt-5.6-sol. Self-refine, Ensemble@3, Ensemble@5, a three-model ensemble and sub-agents gain "+2.8% on average" in recall@5 "with a much higher cost (3.68x)", and the authors conclude that "comprehensive prompt configurations dominate multi-agent configurations". Ensemble@5 reached 70.4 against the base's 65.6, at $8.07 against $1.50 per task. Sub-agents scored 61.9. It measures recall@k only, never precision. See the 2026 additions below.)

### CR-Bench: Evaluating the Real-World Utility of AI Code Review Agents (rechecked)
- **Paper:** Kristen Pereira, Neelabh Sinha, Rajat Ghosh and Debojyoti Dutta; arXiv preprint, 10 Mar 2026; [arXiv 2603.11078](https://arxiv.org/abs/2603.11078). Full text read. Already cited in [decision-6-seeds-and-stopping.md](../research/decision-6-seeds-and-stopping.md).
- **Tested:** 584 instances (174 verified) of real bugs, traced back to the PR that introduced them.
  - **Judge:** a Claude Sonnet 4.5 judge labels each comment Bug Hit, Valid Suggestion or Noise.
  - **Results:** the best recall was 32.8% at 3–5% precision.
- **Closeness: high on scoring.** Its three labels match the project's hit, unplanted finding and false flag.
- **Differences:** the judge isn't checked against human labels, there is one real bug per PR and there are no councils.

### SWR-Bench: Assessing LLM Performance in Real-World Code Review Comment Generation (rechecked)
- **Paper:** Zhengran Zeng et al. (10 authors); arXiv v1 1 Sep 2025, v2 5 Jun 2026; [arXiv 2509.01494](https://arxiv.org/abs/2509.01494). FSE 2026 *(snippet only: the arXiv page lists no venue)*. Full text mostly read.
- **Tested:** 1,000 human-verified PRs, with ground truth mined from the review timelines. An LLM judge checks each ground-truth issue. Its agreement with humans (kappa 52.8–62.0) matches human-to-human agreement (56.3–62.6), and BLEU correlated negatively.
  - **Multi-review aggregation** (several runs merged by an LLM that drops invalid points) raised F1 by up to 43.67%.
  - **A two-agent debate baseline** did worst.
- **Closeness: high.** It has a known-issue key, a judge checked against humans, pooling of several reviews and a debate baseline.
- **Differences:** the issues are real rather than planted, and there are no seats, no keep-or-dismiss judge with severity, no appeal and no competing configurations.

### Other benchmarks with a known-issue key
- **c-CRAB, Code Review Agent Benchmark** ([arXiv 2603.23448](https://arxiv.org/abs/2603.23448); Zhang et al., 2026; full text read):
  - **Tested:** human review comments turned into 234 executable tests over 184 PRs. Claude Code passes 32.1%, and all four tools together pass 41.5%.
  - **Closeness: medium.** It avoids an LLM judge on purpose.
- **AACR-Bench** ([arXiv 2601.19494](https://arxiv.org/abs/2601.19494); Zhang, Yu et al., 2026):
  - **Tested:** 200 PRs with 1,505 expert-checked defects in 10 languages.
  - **Closeness: medium.**
- **MCR-Bench** ([arXiv 2608.27442](https://arxiv.org/abs/2608.27442); Zheng, Wang et al., ISSTA 2026 per the arXiv page):
  - **Tested:** 2,269 multi-round review tasks, with each defect's type and **severity** in the key. Its judge agreement figure (QWK about 0.67–0.73) is *(snippet only)*.
    - (amended 17 Nov 2026: confirmed from the full text by a Claude Code subagent, through a fetch tool, not rechecked by me. Section 5.3, Table 4: the LLM hit judge's QWK with humans is 0.73 for GPT-5.2 Pro, 0.70 for Claude Opus 4.5 and 0.67 for Gemini 3 Pro. Its 0.87 kappa is agreement between the human annotators. Table 9 gives higher hit rates on Major and Critical defects, about 0.52, than on Trivial and Minor, about 0.40.)
  - **Closeness: medium.**
- **Sphinx** ([arXiv 2601.04252](https://arxiv.org/abs/2601.04252); Zhang et al., 2026):
  - **Tested:** coverage of a known-issue checklist instead of BLEU, including bug-free PRs for measuring false positives.
  - **Closeness: medium-low.**
- **ContextCRBench** ([arXiv 2511.07017](https://arxiv.org/abs/2511.07017); Hu et al., 2025):
  - **Tested:** line-level defect localisation among its three tasks.
  - **Closeness: medium-low.**
- **CodeFuse-CR-Bench** ([arXiv 2509.14856](https://arxiv.org/abs/2509.14856); Guo et al., 2025; full text read; its dataset is called SWE-CARE):
  - **Tested:** 601 Python instances, scored partly by BLEU-4 against the human comment.
  - **Closeness: low-medium.**

### Planted or reintroduced bugs (all single reviewers, mostly security)
- **SEVRA-BENCH** ([arXiv 2606.13757](https://arxiv.org/abs/2606.13757); Melo et al., 2026):
  - **Tested:** about 1,000 PRs that reverse historical vulnerability fixes, wrapped in persuasive PR descriptions. Review agents were "susceptible to narrative manipulation".
- **When AI Agrees Too Much** ([arXiv 2603.18740](https://arxiv.org/abs/2603.18740); Alexopoulos et al., to appear at ICSE 2027 per the arXiv comment):
  - **Tested:** 33 CVEs reintroduced against the Claude Code and CodeRabbit review pipelines. A biased PR description got past review in 32 of 33 cases.
  - **Bearing on the project:** it is a direct threat to any judge that reads the PR text.
- **PRWeaver** ([arXiv 2608.02693](https://arxiv.org/abs/2608.02693); Wang et al., 2026):
  - **Tested:** 208 planted malicious changes. Detection was 50–60% per PR, but fell to 16–22% when a 24-PR window was reviewed at once.
- **Jin and Chen, Systematic Overcorrection in Requirement Conformance Judgement** ([arXiv 2603.00539](https://arxiv.org/abs/2603.00539); 2026):
  - **Tested:** LLMs often flag correct code as faulty, and asking for explanations made it worse. It uses correct and bug-injected solutions *(snippet only)*.
- **Closeness: medium.** These are planted keys, but with single agents.
- **A name to avoid confusing:** a personal GitHub repository called `KyleSau/reviewbench`, with 25 seeded-bug PRs, is *(snippet only)*. It is not GitHub's ReviewBench.

### Critiques of similarity scoring
- **DeepCRCEval** ([arXiv 2412.18291](https://arxiv.org/abs/2412.18291); Lu et al., FASE 2025):
  - **Tested:** fewer than 10% of benchmark comments are good enough to use as references, and similarity correlates weakly with defect detection.
- **Jiang et al., Beyond Lexical Similarity** ([arXiv 2501.05176](https://arxiv.org/abs/2501.05176); 2025):
  - **Tested:** semantic and LLM scoring raised correlation with human grades from 0.22 to 0.47.
- **Bearing on the project:** both support scoring against a key rather than human comments.

## 4. Judges, filters and appeals in review pipelines

### Refute-or-Promote: An Adversarial Stage-Gated Multi-Agent Review Methodology (rechecked)
- **Paper:** Abhinav Agarwal; arXiv preprint, 21 Apr 2026; [arXiv 2604.19049](https://arxiv.org/abs/2604.19049). Abstract page read.
- **Tested:** adversarial agents try to disprove each candidate defect at each gate, with a cross-family critic and a required empirical test. About 79% of 171 candidates were killed, and the campaign led to 4 CVEs.
  - **A unanimous error:** ten reviewers unanimously backed an OpenSSL vulnerability that doesn't exist, and one test killed it.
  - *(Snippet only:)* a real CVE was unanimously killed and recovered only by a human.
- **Closeness: medium-high.** It has several agents checking findings across families.
- **Differences:** it runs the **opposite way** to the project's appeal, attacking promotions rather than reinstating dismissals. It is a field campaign, not a controlled test against planted bugs.

### Evident: The Hitchhiker's Guide to Program Analysis, Part III: Mostly Harmless LLMs
- **Paper:** Li, Zhou, Sridharan, Zhang and Qian; arXiv preprint, v1 13 Jun 2026, v2 21 Oct 2026; [arXiv 2606.15122](https://arxiv.org/abs/2606.15122). Abstract page read.
- **Tested:** on 200 kernel-driver warnings (40 real bugs), filters where the LLM makes the final call **missed 27.5–45.0% of confirmed bugs**. Evident dismisses a warning only after a formal check, and missed none.
- **Closeness: medium-high on motivation.** It is direct evidence that LLM dismissals hide real bugs, which is the case for an appeal. Its fix is a formal check, not a second agent.

### One-way filters (no reinstatement)
- **HalluJudge** ([arXiv 2601.19072](https://arxiv.org/abs/2601.19072); Tantithamthavorn et al., FSE 2026 Industry per the arXiv comment):
  - **Tested:** an LLM judge checks whether each review comment is grounded in the code. F1 0.85, and it matched developers about 67% of the time in production.
- **Reducing False Positives in Static Bug Detection with LLMs** ([arXiv 2601.18844](https://arxiv.org/abs/2601.18844); Du et al., Tencent, 2026):
  - **Tested:** 94–98% of false alarms removed "while keeping high recall".
- **ZeroFalse** ([arXiv 2510.02534](https://arxiv.org/abs/2510.02534); 2025) and **QASecClaw** ([arXiv 2605.01885](https://arxiv.org/abs/2605.01885); 2026):
  - **Tested:** both filter static-analysis findings. QASecClaw reports 88.6% fewer false positives for 3.1% lower recall. That recall loss is exactly what an appeal would try to win back.
- **RepoAudit** ([arXiv 2501.18160](https://arxiv.org/abs/2501.18160); Guo et al., 2025):
  - **Tested:** a validator checks that bug paths are feasible.
- **Closeness: medium to low.** All remove findings, and none restores them.

### Juries, courts and judges of judges
- **Replacing Judges with Juries (PoLL)** ([arXiv 2404.18796](https://arxiv.org/abs/2404.18796); Verga et al., Cohere, 2024):
  - **Tested:** a panel of small models from different families beat one large judge, with less self-preference, at over 7 times lower cost.
  - **Closeness: medium.** It supports an outside-family or panel judge.
- **D3: Debate, Deliberate, Decide** ([arXiv 2410.04663](https://arxiv.org/abs/2410.04663); Harrasse et al., EACL 2026):
  - **Tested:** advocates, a judge and an optional jury, with budgeted stopping.
  - **Note:** it had a different title in earlier versions *(snippet only)*.
- **Leveraging LLMs as Meta-Judges** ([arXiv 2504.17087](https://arxiv.org/abs/2504.17087); Li et al., 2025):
  - **Tested:** three agents score other judges' verdicts against a rubric.
  - **Closeness:** the nearest general analogue to an appeal tier, though it filters verdicts rather than reinstating findings.
- **SE-Jury** ([arXiv 2505.20854](https://arxiv.org/abs/2505.20854); Zhou et al., 2025):
  - **Tested:** an ensemble of judging strategies for software tasks, close to human agreement.

### Judge reliability on code
- **CodeJudgeBench** ([arXiv 2507.10535](https://arxiv.org/abs/2507.10535); Jiang et al., 2025; ACL 2026 *(snippet only)*):
  - **Tested:** 26 judges on code tasks. Verdicts change with the order responses are shown in.
- **CodeJudge** ([EMNLP 2024](https://aclanthology.org/2024.emnlp-main.1118); Tong and Zhang):
  - **Tested:** slow-thinking judges of code correctness without tests.
- **Agent-as-a-Judge** ([arXiv 2410.10934](https://arxiv.org/abs/2410.10934); Zhuge et al.; ICML 2025 *(snippet only)*):
  - **Tested:** agent judges on code tasks, with a 90% against 70% human-alignment figure *(snippet only)*.
- **Snippet only, not read:** an appeal stage in multi-agent legal-judgment prediction (arXiv 2601.12815) and maker-checker appeal handling in e-commerce (arXiv 2603.19267). These are the only appeal-like designs found, and neither is in code.

## 5. Evolving or automatically designed agent systems

### EvoMAS: Evolutionary Generation of Multi-Agent Systems (rechecked)
- **Paper:** Yuntong Hu, Yuting Zhang, Matthew Trager, Yi Zhang, Shuo Yang, Wei Xia and Stefano Soatto; ICML 2026 (arXiv comment and journal-ref); [arXiv 2602.06511](https://arxiv.org/abs/2602.06511). Abstract page read, plus part of the full text.
  - **Versions:** v1 6 Feb 2026; v2 withdrawn 11 Feb 2026 ("Employer internal policy compliance"); v3 20 May 2026; v4 27 May 2026.
- **Tested:** it evolves whole multi-agent configurations by selection, mutation and crossover guided by execution traces. A configuration is the agent graph plus each agent's model, prompt and tools.
  - **Results:** it beat EvoAgent by +10.5 points on BBEH and +7.1 on WorkBench, and reached 79.1% on SWE-Bench Verified with Claude 4.5 Sonnet.
  - **Fitness:** an LLM judge's score minus a cost term. The default judge is a Claude model, with a Qwen judge only as an ablation (full text).
- **Closeness: high in method, low in task.** It evolves what this project evolves (models, roles and topology), at a cost penalty. But it solves tasks rather than reviewing them, and it has the same Claude-judges-Claude risk, unanalysed.
- **A second paper with the same name:** "EvoMAS: Heuristics in the Loop—Evolving Smarter Agentic Workflows" by Yangbo Wei et al., [PMLR vol. 306](https://proceedings.mlr.press/v306/wei26m.html), also ICML 2026. It evolves roles among other things, and its page names no evaluation domains. Cite both by full title.

### The main automatic-design methods (abstract pages read; none applied to review)

| Method | Paper | What it searches |
|---|---|---|
| ADAS | Hu, Lu and Clune, [arXiv 2408.08435](https://arxiv.org/abs/2408.08435) (2024–2025) | a meta agent writes new agents in code, with an archive |
| AFlow | Zhang et al., [arXiv 2410.10762](https://arxiv.org/abs/2410.10762) (2024–2025) | tree search over workflows as code; smaller models beat GPT-4o at 4.55% of the cost |
| GPTSwarm | Zhuge et al., ICML 2024, [arXiv 2402.16823](https://arxiv.org/abs/2402.16823) | agents as graphs: prompts and who talks to whom |
| EvoAgent | Yuan et al., NAACL 2025, [arXiv 2406.14228](https://arxiv.org/abs/2406.14228) | mutation, crossover and selection to grow varied agents from one |
| MaAS | Zhang et al., [arXiv 2502.04180](https://arxiv.org/abs/2502.04180) (2025) | a supernet that samples a system per query, at 6–45% of the cost |
| MASS | Zhou et al., ICLR 2026, [arXiv 2502.02533](https://arxiv.org/abs/2502.02533) | prompts and topology, in stages |
| EvoFlow | Zhang et al., [arXiv 2502.07373](https://arxiv.org/abs/2502.07373) (2025) | a diverse population of workflows kept by niching |
| Darwin Gödel Machine | Zhang, Hu, Lu, Lange and Clune, [arXiv 2505.22954](https://arxiv.org/abs/2505.22954) (already cited) | self-modifying coding agents; its "peer-review mechanisms" are another model choosing the best attempt (full text) |
| Meta-Harness | Lee et al., [arXiv 2603.28052](https://arxiv.org/abs/2603.28052) (2026) | a proposer that reads all earlier candidates' code, scores and traces |

Others read on their abstract pages:
- **[SEW](https://arxiv.org/abs/2505.18646):** evolves workflows for code generation, not review.
- **[ARTEMIS](https://arxiv.org/abs/2512.09108):** evolutionary tuning of prompts and tools.
- **[Rethinking the Value of Multi-Agent Workflow](https://arxiv.org/abs/2601.12307)** (Xu et al., 2026): one agent matched same-model multi-agent workflows, which supports a strong single-reviewer baseline.

### The closest in task
- **AgentFlow: Synthesizing Multi-Agent Harnesses for Vulnerability Discovery** (rechecked):
  - **Paper:** Hanzhi Liu et al. (7 authors); arXiv preprint, 22 Apr 2026; [arXiv 2604.20801](https://arxiv.org/abs/2604.20801). Abstract page read.
  - **Tested:** an automatically designed multi-agent harness, covering roles, prompts, tools, topology and protocol. It is rewritten from runtime signals. It found ten zero-days in Chrome and scored 84.3% on TerminalBench-2 with Claude Opus 4.6.
  - **Closeness: high.** It is the closest automatically designed multi-agent bug finder.
  - **Differences:** it tests running programs instead of reading code. It has no judge, appeal or planted key, and it doesn't race councils.
- **MulVul: Retrieval-augmented Multi-Agent Code Vulnerability Detection via Cross-Model Prompt Evolution:**
  - **Paper:** Zihan Wu et al.; [ACL 2026](https://aclanthology.org/2026.acl-long.391/). Abstract page read.
  - **Tested:** a router plus detector agents over 130 CWE types, at 34.79% macro-F1. The prompts are evolved with a *different* model from the one that runs them, to avoid self-bias. Cross-model evolution beats manual prompts by 51.6%.
  - **Closeness: high-medium.** It evolves a multi-agent bug detector and deliberately crosses model families, bridging this topic and the next. But it is a classifier that evolves prompts only.
- **Ouroboros** ([arXiv 2608.08311](https://arxiv.org/abs/2608.08311); Razzhigaev et al., 2026; part of the full text read):
  - **Tested:** every self-edit of an evolving agent passes a multi-model review panel with a quorum, which blocked 63.5% of recent edits. It notes that reviewers "can share blind spots with the agent", but reports no miss rate.
  - **Closeness: medium.**

## 6. Self-preference and shared blind spots

### When Does a Second Model Help? Cross-Model Review in LLM Verification (rechecked)
- **Paper:** Tae-Eun Song; arXiv preprint, v1 1 Oct 2026, v2 6 Oct 2026; [arXiv 2610.01471](https://arxiv.org/abs/2610.01471). Full text read.
- **Tested:** 30 artifacts (Python modules, tutorials and scripts) with 150 planted errors, in 10 review conditions and 900 sessions.
  - **Who wrote the errors:** Claude Opus 4.6 wrote the artifacts and planted the errors, according to the run logs.
  - **Same-model against cross-model:** fresh-session same-model review didn't differ significantly in F1 from the best cross-model reviewer (GPT-5.4).
  - **Complementary errors:** the two found partly different errors (Jaccard 41.2%). One same-model plus one cross-model review matched 56.7% of planted errors, against 42.7% for two same-model reviews (Holm-adjusted p = .006).
- **Closeness: high.** It is close to this project's self-preference concern measured directly: Claude-planted errors in Claude-written code and docs, with same-family and cross-family reviewers.
- **Differences:**
  - it is small, single-author and unrefereed;
  - its ground truth is self-planted;
  - there are no councils, judge or appeal.
- **Companion paper:** the earlier [Cross-Context Review](https://arxiv.org/abs/2603.12123) uses the same 30 artifacts and compares fresh sessions with self-review.

### Same family reviewing code
- **Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?** ([arXiv 2607.21656](https://arxiv.org/abs/2607.21656); Xiang, Zhang, Zhang and Xu; Agentic SE workshop at KDD'26; abstract page read):
  - **Tested:** Claude reviewing Codex drafts raised the pass rate from 71.6% to 89.7%. Codex reviewing Claude drafts lowered it from 91.4% to 82.8%.
  - **Closeness: high-medium.** It measures pass rate after revision, not planted-bug detection.
- **Models are worse at reviewing their own code** ([Greptile blog](https://www.greptile.com/blog/model-inversion), 21 Jul 2026; vendor, not peer-reviewed; full post read):
  - **Tested:** 500 PRs written by Claude Code and 500 by Codex, each reviewed by both. The same-family penalty was 2–3 points of recall, with figures read off a chart.
  - **Caveat:** Greptile sells the routing feature this motivates.
- **Gong et al., How Well Do LLMs Serve as End-to-End Secure Code Agents for Python?** ([arXiv 2408.10495](https://arxiv.org/abs/2408.10495); 2024–2025; full text read):
  - **Tested:** GPT-3.5 and GPT-4 *repaired* their own vulnerable code least well, but showed no own-code blind spot in *detection*.
  - **Closeness: high-medium.** The text and the table differ slightly (54.3% against 55.0%).
- **Articulate but Wrong** ([arXiv 2605.21537](https://arxiv.org/abs/2605.21537); Reddy et al., 2026):
  - **Tested:** 11 models endorsed 31.7% of their own behaviour-changing errors in Python 2 to 3 upgrades.

### Self-preference in judging
- **Self-Attribution Bias: When AI Monitors Go Easy on Themselves** ([arXiv 2603.04582](https://arxiv.org/abs/2603.04582); Khullar, Hopkins, Wang and Roger, 2026):
  - **Tested:** monitors missed bad coding and tool actions more often when judging an action in the same turn that produced it. Simply labelling it as their own didn't cause the bias.
  - **Bearing on seats:** fresh-context subagents should reduce it.
- **Self-Preference Bias in Rubric-Based Evaluation of LLMs** (rechecked; [arXiv 2604.06996](https://arxiv.org/abs/2604.06996); José Pombal, Ricardo Rei and André F. T. Martins; v1 8 Apr 2026, v3 3 Aug 2026):
  - **Tested:** on LiveCodeBench, a judge is over 50% more likely to wrongly pass a failed rubric item when the output is its own. Ensembles reduce this but don't remove it.
  - **Already cited** in [review-notes-oct31.md](../research/review-notes-oct31.md) as COLM 2026, but the arXiv page shows no venue.
- **Do LLM Evaluators Prefer Themselves for a Reason?** ([arXiv 2504.03846](https://arxiv.org/abs/2504.03846); Chen et al., 2025):
  - **Tested:** stronger models show more self-preference on code. Much of it is justified, but it is harmful exactly where they were wrong as generators. Longer reasoning reduces it.
- **Play Favorites** ([arXiv 2508.06709](https://arxiv.org/abs/2508.06709); Spiliopoulou et al., 2025):
  - **Tested:** Claude 3.5 Sonnet and GPT-4o favour their own and their family's outputs, with quality controlled.
- **Who Judges Matters** ([arXiv 2609.17857](https://arxiv.org/abs/2609.17857); Awuni et al., 2026):
  - **Tested:** a same-family lift of 3.4–8.4 points in open-model panels, mostly confounded with quality.
- **Preference Leakage** ([arXiv 2502.01534](https://arxiv.org/abs/2502.01534); Li et al., ICLR 2026):
  - **Tested:** judges favour models trained on data from a related model.
- **Already cited and confirmed:** Panickssery et al. 2024 (the arXiv page lists no venue, so check the one the paper uses) and Wataoka et al. 2024 (NeurIPS 2024 Safe Generative AI Workshop).

### Correlated errors
- **Great Models Think Alike and this Undermines AI Oversight** ([arXiv 2502.04313](https://arxiv.org/abs/2502.04313); Goel et al., 2025):
  - **Tested:** judges favour models similar to themselves, and mistakes grow more similar as models get stronger.
  - **Bearing on the project:** its CAPA metric could measure error overlap between seats.
- **Correlated Errors in Large Language Models** ([arXiv 2506.07962](https://arxiv.org/abs/2506.07962); Kim, Garg, Peng and Garg, ICML 2025):
  - **Tested:** across 350+ models, two models that both err agree 60% of the time. Shared provider and architecture raise this.
- **Is Self-Repair a Silver Bullet?** ([arXiv 2306.09896](https://arxiv.org/abs/2306.09896); Olausson et al., ICLR 2024):
  - **Tested:** self-repair is limited by the model's ability to critique its own code.
- **Self-Correction Bench** ([arXiv 2507.02778](https://arxiv.org/abs/2507.02778); Tsui, COLM 2026):
  - **Tested:** a 64.5% blind spot for the model's own errors in 14 open models.

## How new is this?

**The short answer:** most of the parts have prior work. A few combinations look new, but they are combinations rather than new ideas.

| Part of the project | Prior work? | Closest papers |
|---|---|---|
| Several LLM reviewer agents in role seats, with a judge or critic | **Yes, plenty.** Not new. | RevAgent, Hydra-Reviewer, OpenCodeReview, the Ericsson study, MultiVer, VulTrial, GPTLens |
| Scoring review against known bugs, not similarity to human comments | **Yes.** Not new. | CRBugBench, CR-Bench, SWR-Bench, MCR-Bench, plus the vendor sets in seed-sources-research.md |
| Planted bugs specifically | **Yes**, but for single reviewers and mostly security | Song 2026, SEVRA-BENCH, PRWeaver, When AI Agrees Too Much, Kumar et al. |
| An LLM matching judge checked against human labels | **Yes.** Not new. | SWR-Bench, MCR-Bench, Adversarial Review |
| A judge from another family | **Partly.** Panels and cross-family critics exist, but none matches findings to a planted key. | PoLL, Refute-or-Promote, MulVul |
| Specialist against generalist reviewers | **Partly.** Shown for paper review and with BLEU scoring, never at equal cost against planted bugs. | MARG, RevAgent, ChatEval, Agents with Feelings |
| Comparing whole role sets at equal cost against planted bugs (A, B, C and the generalist) | **Looks new.** | CodeX-Verify (15 role combinations, but static analysers on 29 samples); MultiVer (a role ablation, no cost control); Tran and Kiela, and Kim et al. (equal cost, not review) |
| An appeal that can reinstate the judge's dismissals | **Looks new.** Every filter found is one-way. | OpenCodeReview (delete-only), Refute-or-Promote (the opposite direction), Evident (evidence that dismissals hide bugs), the meta-judges paper |
| Checking the judge's severity calls against human labels | **Looks new.** None found. | MCR-Bench has severity in its key |
| Evolving or racing configurations | **Method: yes, strongly.** **Applied to review councils: looks new.** | EvoMAS (Hu et al.), ADAS, AFlow, EvoAgent, MASS, EvoFlow; AgentFlow and MulVul for bug finding |
| Same-family blind spots when Claude writes the code, plants the bugs and reviews | **Yes, recently and closely.** Not new. | Song 2026 (nearly this design, small), Xiang et al., Greptile, Gong et al., Khullar et al., Pombal et al. |

**Being strict:**
- **Same-family blind spots:** Song 2026 already measures same-model against cross-model review on Claude-planted errors in code and docs. The project can extend it, with councils, a judge and a larger set, but can't claim the question as new.
- **Specialist against generalist:** MARG has already shown specialists beat a generic team and single agents for paper review. The new part is doing it at equal cost, on code, against a planted key.
- **Evolving agent systems:** EvoMAS already evolves models, roles and topology under a cost penalty. The new part is applying it to review councils and scoring against planted bugs.
- **The newest-looking pieces** are the appeal of dismissals, the equal-cost role-set comparison and the racing of review councils. Absence is only what this search found: with IEEE Xplore, Semantic Scholar and Google Scholar not searched, something close could still exist.

## What the research doc and the paper should cite but don't

The paper's `references.bib` has 30 entries. It cites Panickssery, Wataoka, Kim et al. (agent scaling), the persona paper and the Darwin Gödel Machine, but **no multi-agent code-review paper at all**. The experiment plan cites none of the papers below either, though some appear in other research files: RevAgent, CodeAgent and Hydra-Reviewer in review-areas-research.md, CR-Bench in decision-6, and Pombal in the 31 Oct review notes.

**Closest work, which the paper needs:**
- Song 2026 (When Does a Second Model Help?)
- MARG
- RevAgent
- Hydra-Reviewer
- EvoMAS (Hu et al.), as outside review 1 already noted
- CRBugBench
- SWR-Bench
- CR-Bench
- Refute-or-Promote
- OpenCodeReview
- Evident

**Strongly relevant:**
- Adversarial Review
- VulTrial
- MultiVer
- Xiang et al. (Cross-Model LLM Code Review)
- Khullar et al. (Self-Attribution Bias)
- Pombal et al.
- Goel et al. (Great Models Think Alike)
- Kim et al. (Correlated Errors)
- Tran and Kiela (equal token budgets)
- ADAS
- AFlow
- EvoAgent
- AgentFlow
- MulVul
- When AI Agrees Too Much (Claude Code's review pipeline fooled by biased PR text)

## Discrepancies found

- **Two ICML 2026 papers are called EvoMAS** (Hu et al. and Wei et al.). The Hu et al. paper's v2 was withdrawn, and its author order changed between v1 and v3.
- **Pombal et al.:** the 31 Oct review notes give COLM 2026 as the venue, but the arXiv page shows no venue.
- **Kim et al. (scaling agent systems):** the v3 abstract says 260 configurations, where the Google blog said 180.
- **Agent counts that don't match the label:** CodeX-Verify's "agents" are static analysers, and MultiVer's style agent never calls the LLM.
- **Inconsistent figures inside papers:**
  - Adversarial Review gives MARS 85% in the text and 82% in Table 1.
  - c-CRAB gives 67 repositories in one place and 56 in another.
  - Gong et al. give 54.3% in the text and 55.0% in a table.
- **SWR-Bench:** a search snippet gave a different earlier title, but the arXiv page shows only the current one.
- **Kumar et al.** ([arXiv 2606.15689](https://arxiv.org/abs/2606.15689)): the fetch summary gives a submission date that doesn't fit its June 2026 arXiv number. Check this on the page before citing.
- **Entries with no read status** (added 17 Nov 2026): Khullar et al. (Self-Attribution Bias), Goel et al. (Great Models Think Alike), Kim, Garg et al. (Correlated Errors) and "When AI Agrees Too Much" don't say whether the abstract or the full text was read, against the rule at the top of this file. The paper session of 16 Nov 2026 noticed this while drafting its /deep-research commands. Until they're re-read, treat them as abstract only.

## Loosely related

### Predicting Acceptance and Review Effort in Human and Agent Pull Requests
- **Paper:** Kartik Ghanshyambhai Pansuriya, Ehsan Ghorbani, Deepak Singh and Eman Abdullah AlOmar, Stevens Institute of Technology; arXiv preprint, v1 13 Jul 2026; no venue stated. [arXiv 2607.12057](https://arxiv.org/abs/2607.12057). Abstract page and [full text](https://arxiv.org/html/2607.12057v1) read by me through a fetch tool.
- **Tested:** whether a PR's acceptance and review effort can be predicted at submission time, from metadata only. It used classical machine learning (logistic regression, random forests, gradient boosting, extra trees and MLPs) on human- and agent-authored PRs from the AIDev corpus.
  - **Acceptance:** predictable, with tree-based models reaching F1 above 0.95.
  - **Review effort:** comment counts and time to merge are only modestly explained (R² 0.20 and 0.12, pooled).
- **Not prior work on councils:** it doesn't evaluate AI reviewers.
- **How it connects:**
  1. **Motivation.** It reports that "agent-authored PRs show slightly higher discussion and longer median time-to-merge". That is mild support for the project's motivation, though it gives no split figures, only the direction.
  2. **A possible source of real agent-written bugs** for the same-family question: AIDev includes Claude Code PRs. See the "To check" section in [seed-sources-research.md](seed-sources-research.md).

## 7. Additions from a 2026 search (17 Nov 2026)

**How it was done:** an overnight Claude Code session sent one research subagent to search for 2026 work on five topics: multi-agent LLM code review; appeal or re-check steps for LLM judges; precision measures for AI code review; scripted workflows against agent-led orchestration; and project instruction files helping or biasing agents. It opened each item's own page through a fetch tool, so, as in the first search, what was seen was a summary of the page with short quotes. The session then reopened six items itself and found their titles, authors, dates and headline figures matched: CRBugBench's Table 3 (above), CRJudgeBench, Jagged Judges, Evaluating AGENTS.md, Deterministic vs. LLM-Controlled Orchestration and Stale Instruction Files. Everything else is the subagent's read only. Each entry says what was read. None is refereed unless a venue is given, and figures need a second look before the paper cites them.

**What changes for the project:**
- **Judges err both ways.** The case for an appeal rests on judges dismissing real findings (Evident). CRJudgeBench finds LLM judges of review comments mostly *over-keep*. So the scoring should report the judge's errors in both directions: false findings kept and real findings dismissed.
- **The appeal's failure mode has prior work.** Challenging a judge flips its verdict often, and the flips mostly make it less accurate (Jagged Judges, Who Flips). Reinstated findings should be scored on their own against the key.
- **Multi-agent gains at high cost.** CRBugBench's ensembles and sub-agents gain little at 3–5 times the cost, which supports the equal-cost single-reviewer arm.
- **Instruction files.** There's now direct 2026 evidence on both sides of the CLAUDE.md help-or-bias question, though all of it is on coding agents, not reviewers.

### Multi-agent code review and precision

- **Is Agentic Code Review Helpful? Mining Developers' Feedback to CodeRabbit Reviews in the Wild** (Hong Yi Lin, Liang, Thongtanunam and Tantithamthavorn; [arXiv 2607.03316](https://arxiv.org/abs/2607.03316), v1 3 Jul 2026, v2 23 Jul 2026; full text read except the last part):
  - **Tested:** 31,073 review comments and developer responses from 10,191 PRs in 239 repositories. 36.4% were accepted, 7.3% discussed and 56.3% rejected (Table 2).
  - **Why rejected (Table 3):** 58.0% were invalid (43.3% false positives, 10.0% out of scope, 4.7% redundant), and 42.0% conflicted with the developer's design choices. Section 5 gives 35.8% for false positives, which doesn't match Table 3.
  - **A learned filter:** a small fine-tuned model predicted rejection at F1 0.76, while zero-shot GPT-5.1 reached only 0.06–0.24 (Table 5).
  - **How it connects:** its invalid, out-of-scope and redundant labels map onto false flags and extras. The weak zero-shot filter bears on how good an LLM judge's keep-or-dismiss call can be.
- **Agentic Code Review in the Terminal: A Trajectory-Level Analysis of Behavior, Cost, and Human-Alignment** (Charoenwet, Tantithamthavorn et al.; [arXiv 2607.16740](https://arxiv.org/abs/2607.16740), v1 18 Jul 2026; full text read):
  - **Tested:** 362 review tasks. Claude Code on Sonnet 4.6 posted 947 comments, 22.39% localised correctly and 14.37% aligned with humans. A static GPT-5.2 reviewer posted 3,180, 7.86% localised and 21.44% aligned (Table 1). Claude Code spent 51% of its cost exploring.
  - **How it connects:** per-comment precision proxies for single reviewers. No councils.
- **AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection** (Charoenwet et al.; [arXiv 2601.19138](https://arxiv.org/abs/2601.19138), v1 27 Jan 2026, v2 3 Aug 2026; ASE 2026 Industry per the arXiv comment; abstract only):
  - **Tested:** at least 153% relative improvement in correct, relevant comments over a static LLM, a multi-agent reviewer and static analysis tools. In a shadow deployment at Atlassian, security engineers validated 54% of its comments.
  - **How it connects:** a single agent beat a multi-agent reviewer, though cost wasn't matched.
- **The Specification as Quality Gate: Three Hypotheses on AI-Assisted Code Review** (Christo Zietsman; [arXiv 2603.25773](https://arxiv.org/abs/2603.25773), v1 26 Mar 2026; full text, section 2.5):
  - **Tested:** three small sets of five planted bugs each, five runs per function. Claude caught every pattern bug. A cross-family panel caught 57 of 100, one bug was missed by all four seats, and only Gemini caught another.
  - **Two warnings for planted seeds:** hints leak through context, as when a docstring stated the convention a bug broke, and an unused import worked as a hint (removing it dropped one tool from 5 of 5 to 2 of 5).
  - **How it connects:** a second, smaller Claude-reviews-Claude planted-bug test besides Song 2026, and weaker. Its leak warnings match the easy tier's leak tags.
- **From Industry Claims to Empirical Reality: An Empirical Study of Code Review Agents in Pull Requests** (Kowshik Chowdhury et al.; [arXiv 2604.03196](https://arxiv.org/abs/2604.03196), v1 3 Apr 2026; MSR 2026 per the arXiv comment; abstract only):
  - **Tested:** PRs reviewed only by an agent were merged 45.20% of the time, against 68.37% for human-only review. 12 of 13 agents averaged below 60% "signal".
  - **How it connects:** a per-PR signal ratio, roughly the inverse of extras per catch.
- **"Go Home Copilot, You're Drunk": Developer Responses to Agent-Generated Code Review Comments** (Cynthia, Widyasari, Roy, Ting Zhang and David Lo; [arXiv 2607.21997](https://arxiv.org/abs/2607.21997), v1 24 Jul 2026, v2 29 Jul 2026; abstract only):
  - **Tested:** 54,791 comments from five agents in 342 Python repositories. The top reasons for unresolved comments were incorrect suggestions and intentional design decisions. An inline code suggestion best predicted resolution.
  - **How it connects:** resolution rate as a precision measure, like Goldman et al. in review-areas-research. The project scores against a key instead.
- **Two industry write-ups, not peer-reviewed:**
  - **[Bringing Code Review to Claude Code](https://claude.com/blog/code-review)** (Anthropic, 9 Mar 2026; full post): parallel agents, a verification step that filters false positives, and ranking by severity. It reports "less than 1% of findings are marked incorrect" and $15–25 per review, with no recall figure. Its verify step is one-way, with no appeal. Context for the Ultrareview baseline.
  - **[Same model, six code reviewers, 38% to 81% of the bugs](https://quickchat.ai/post/same-model-six-code-reviewers-38-to-81-percent-of-the-bugs)** (Quickchat AI, 13 Nov 2026; vendor; full post): six reviewer harnesses on one model, against an LLM-built key no human checked. Recall ran from 38% to 81%, so the harness mattered more than the model. A three-reviewer panel found 6 points more than one reviewer at $0.46 against $0.17 per PR. It reports cost per extra bug found, close to the project's extras-per-catch idea. Each configuration ran once.

### Judges, re-checks and appeals

- **CRJudgeBench: Can AI Detect Plausible but Invalid Code Reviews?** (Yue Pan, Jiawei Li, Ziyuan Zhang, Xiangxin Zhao and He Ye; [arXiv 2609.37216](https://arxiv.org/abs/2609.37216), v1 29 Sep 2026; under review at ICLR 2027 per the arXiv comment; abstract rechecked by the session, full text read by the subagent):
  - **Tested:** 1,199 review comments, trustworthy or not, with a 359-item test set. The best judge, the authors' own agentic Sentinel, reached 76.60% accuracy (abstract).
  - **Leniency (Tables 2–3, the subagent's read):** every model judged at least 85.52% of comments trustworthy, against a 63.79% base rate. Claude Opus 5 and GPT-5.5 were the most lenient, at 94.99%, and caught only 2.31–20.77% of untrustworthy comments.
  - **A count that doesn't add up:** section 2 says 1,031 items were reviewed by hand, but its counts sum to 829.
  - **How it connects:** the closest benchmark for the project's judge. It shows the opposite error to the one the appeal exists for.
- **Jagged Judges: Epistemic Stability Under Perturbation, Pressure, and Persistence** (Justin Zhao, Himaghna Bhattacharjee, Hannah Korevaar, Bhaktipriya Radharapu and Khalid El-Arini; [arXiv 2608.12645](https://arxiv.org/abs/2608.12645), v1 12 Aug 2026, v2 21 Aug 2026; abstract rechecked):
  - **Tested:** 9 frontier models on 14 judging tasks, none of them code. Verdicts flipped 25–71% of the time under plain pushback and 62–91% against an adversarial persuader. Pressure that changed a verdict was "almost always net-corrupting with respect to ground truth".
  - **How it connects:** an appeal is pushback on a judge. If the main session or a later seat argues with the judge, flips may be wrong more often than right. The appeal here doesn't argue with the judge directly, so this is a risk to test, not a result.
- **Who Flips? Self- and Cross-Model Counterarguments Reveal Answer Instability in LLMs** (Nikeghbal et al.; [arXiv 2606.16011](https://arxiv.org/abs/2606.16011), v1 14 Jun 2026, v2 30 Aug 2026; Findings of EMNLP 2026 per the arXiv comment; abstract only):
  - **Tested:** on MMLU, flip rates of 17.5–97.3% across 7 models. Arguments framed as the model's own raised flips by 7.1 points on average.
  - **How it connects:** a same-family appeal may sway a Claude judge more than an outside-family one. A measurable variable.
- **Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations** (Roytburg et al.; [arXiv 2601.22548](https://arxiv.org/abs/2601.22548), v1 30 Jan 2026, v4 22 Jun 2026; ICML 2026 per the arXiv comment; abstract only):
  - **Tested:** with a baseline for the evaluator's quality, only 51% of earlier self-preference examples stay significant.
  - **How it connects:** a caveat on section 6 above. A same-family analysis should control for whether the judge could find the bug itself.
- **Quantifying and Mitigating Self-Preference Bias of LLM Judges** (Jinming Yang et al.; [arXiv 2604.22891](https://arxiv.org/abs/2604.22891), v1 24 Apr 2026, v4 2 Jun 2026; abstract only): across 20 LLMs, more capable models weren't less self-preferring. A structured, multi-dimensional evaluation cut self-preference by 31.5% on average. Weak support for the judge's fixed ruling format.
- **Reviewer Capability Governs Rejection Targeting, Not Repair Skill** (Faizan Tanveer; [arXiv 2609.04270](https://arxiv.org/abs/2609.04270), v1 2 Sep 2026; a 6-page pilot; full text): on 100 maths problems, self-review falsely rejected 18 of 52 correct answers, and a cross-family reviewer 1 of 52 (Table 2). Not code. Small evidence that same-model checkers over-reject.
- **Prior Audit-Repair Context Shifts LLM Verifier Thresholds Toward Leniency** (Parsa Mazaheri and Kasra Mazaheri; [arXiv 2608.16003](https://arxiv.org/abs/2608.16003), v1 17 Aug 2026; abstract only): an earlier audit-and-repair episode in context lowered false alarms by 2.8–11.5 points in all 15 conditions, by moving the threshold, not the ability to discriminate. An argument for keeping what the judge and appeal see fixed across configurations.
- **Chain-of-Models: Cross-Model Auditing for Bias-Robust LLM Judges** (Qian Wang et al.; [arXiv 2607.28636](https://arxiv.org/abs/2607.28636), v1; marked work in progress; abstract only): a second model audits the judge's reasoning, and a model's own bias resistance doesn't predict how good an auditor it is. The page gives a submission date of 19 May 2026, which doesn't fit its July arXiv number. Check before citing.

### Scripted workflows against agent-led orchestration

- **Deterministic vs. LLM-Controlled Orchestration for COBOL-to-Python Modernization** (Naing Oo Lwin and Rajesh Kumar; [arXiv 2605.09894](https://arxiv.org/abs/2605.09894), v1 11 May 2026; abstract rechecked, full text read by the subagent):
  - **Tested:** the same models, prompts and tools, with only who controls the steps varied. The abstract reports "comparable computational accuracy", better worst-case results and less run-to-run variation for the scripted pipeline, and up to 3.5 times fewer tokens. By the subagent's read of Table 1, LLM-controlled runs had slightly higher success rates (+0.016 to +0.034), and section 5.5 says the scripted advantage shrinks when validators are weak.
  - **How it connects:** the cleanest controlled comparison found for outside review 7's item 11. It predicts a scripted council would be cheaper and more consistent than Lite, perhaps at a small cost. It's translation, not review.
- **Agent Architecture Cost-Success Trade-offs: A Controlled Evaluation across Enterprise-Style SOPs** (Subhrangshu Nandi et al.; [arXiv 2611.12953](https://arxiv.org/abs/2611.12953), v1 7 Nov 2026; abstract only): no architecture won in aggregate. Coordinated set-ups cost 1.4–4.7 times the tokens of a single agent, and a plausible multi-agent build lost to it. Only a targeted redesign beat it. So how well a council is built may matter more than its shape.
- **Abstract only, briefly:**
  - **LLM-as-Code: Agentic Programming for Agent Harness** (Junjia Qi et al.; [arXiv 2606.15874](https://arxiv.org/abs/2606.15874), v3 9 Nov 2026; KDD 2026 AgenticSE workshop): a position paper arguing that code, not the model, should own the loop. No figures.
  - **In-Context Prompting Obsoletes Agent Orchestration for Procedural Tasks** (Simon Dennis et al.; [arXiv 2604.27891](https://arxiv.org/abs/2604.27891), v2 5 May 2026; LLM-judged): cuts the other way. The whole procedure in one prompt beat a LangGraph orchestration.
  - **Multi-Agent Teams Hold Experts Back** (Pappu et al.; [arXiv 2602.01011](https://arxiv.org/abs/2602.01011), v4 28 May 2026; ICML 2026 per the arXiv comment): self-organising teams did up to 41.1% worse than their best member, compromising instead of deferring to the expert. Bears on the free-debate arm of outside review 7's item 8, and on judged against consensus combining.

### Project instruction files (CLAUDE.md, AGENTS.md)

None of these tests reviewers. Each is about coding agents.

- **Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?** (Thibaud Gloaguen, Niels Mündler-Sasahara, Mark Niklas Müller, Veselin Raychev and Martin Vechev; [arXiv 2602.11988](https://arxiv.org/abs/2602.11988), v1 12 Feb 2026, v3 29 Sep 2026; abstract rechecked, full text read by the subagent):
  - **Tested:** context files "do not generally improve task success rates" and raise cost by over 20% (abstract). Agents do follow the instructions in them. By the subagent's read of section 4.2, developer-written files beat LLM-written ones by about 7 points, the one significant comparison.
  - **How it connects:** the main precedent for the help-or-bias test's "help" side.
- **Stale Instruction Files Override the Code in Coding Agents: A One-Sentence Fix** (Xiaonan Xu and Wenjing Wu; [arXiv 2610.30571](https://arxiv.org/abs/2610.30571), v1 22 Oct 2026; abstract rechecked, full text read by the subagent):
  - **Tested:** 40 Python projects with a planted conflict between the instruction file and the code, 320 runs on Claude Code and Codex CLI. 90.1% of choices followed the stale file. Claude Code named the conflict in 79 of 80 runs and still followed the file. One sentence about precedence moved choices following the code from 4.2% to 91.4%.
  - **How it connects:** the closest design for the test's "bias" side. A reviewer that reads a wrong `CLAUDE.md` may excuse a bug that fits it, or flag correct code. That's an inference: the paper doesn't test reviewers.
- **Guardrails Beat Guidance: A Large-Scale Study of Rules, Skills, and Persistent Configuration for Coding Agents** (Xing Zhang et al.; [arXiv 2604.11088](https://arxiv.org/abs/2604.11088), v2 28 May 2026; full text): random and curated `CLAUDE.md` rules both scored 63.8% against a 50.0% baseline on 58 tasks, with no significant difference between conditions. The authors put the gain down to priming that doesn't depend on content. So a CLAUDE.md test needs a random-file control, not just with and without.
- **Do Context Files Help Coding Agents? A Two-Agent Ablation Study** (Prakhar Khatri; [arXiv 2607.27250](https://arxiv.org/abs/2607.27250), v1 28 Jul 2026; full text): no measurable effect on 15–17 tasks, and a power analysis saying 120–200 tasks are needed to detect 10 points. Useful for sizing the test.
- **Abstract only, briefly:**
  - **On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents** (Jai Lal Lulla et al.; [arXiv 2601.20404](https://arxiv.org/abs/2601.20404), v2 30 Mar 2026): lower runtime and output tokens with a file, which partly contrasts with Gloaguen et al.'s higher cost.
  - **Instruction Adherence in Coding Agent Configuration Files** (Damon McMillan; [arXiv 2605.10039](https://arxiv.org/abs/2605.10039), v1 11 May 2026): 1,650 Claude Code sessions, with no detectable effect of file size, position or contradictions on compliance.
  - **When Instruction Files Go Stale** (Tural Mehtiyev et al.; [arXiv 2611.09802](https://arxiv.org/abs/2611.09802), v1 6 Nov 2026): a stale test command cost extra tool calls, and no agent repaired the file.
  - **SWE-PRBench** (Deepak Kumar; [arXiv 2603.26130](https://arxiv.org/abs/2603.26130), v1 27 Mar 2026): the code-review benchmark Adversarial Review used. All 8 models got worse as context grew, and a short diff-plus-summary prompt beat a longer full-context one. A review-specific sign that extra context, instruction files included, can dilute attention.

### Loosely related

- **Do Coding Agents Catch Their Own Bugs? (They Don't.)** (Shaswat Patel et al.; [arXiv 2611.01181](https://arxiv.org/abs/2611.01181), v1 31 Oct 2026; abstract only): 212 pairs where a later PR fixed a defect the first one introduced. It tests authors, not reviewers, but it's a possible source of real escaped bugs for the hard tier.
- **Automating Low-Risk Code Review at Meta: RADAR** (Adams et al.; [arXiv 2605.30208](https://arxiv.org/abs/2605.30208), v2 12 Jun 2026; abstract only): a production pipeline of a risk score, LLM review and fixed checks, so a scripted workflow, not a council. The abstract's "over 330%" time reduction doesn't make sense as written.

### Searched for, not found

- an appeal or second-opinion step for a verifier's wrongful rejections (Jagged Judges, Who Flips, Tanveer and Mazaheri are the nearest);
- a 2026 academic study of several LLM reviewers voting on planted bugs, with precision and recall (only vendor benchmarks, not opened);
- ranking or top-k measures for review comments beyond CRBugBench's recall@k;
- a measured effect of repository instructions on LLM *reviewers*;
- a 2026 self-preference study on code specifically.

So, on this search, the appeal that reinstates dismissals, the equal-cost role-set comparison and a CLAUDE.md test on reviewers still look new. The same caveat applies as before: IEEE Xplore, Semantic Scholar and Google Scholar weren't searched.
