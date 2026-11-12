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
- **Paper:** Xiaoxue Ren, Chaoqun Dai, Qiao Huang, Ye Wang, Bo Jiang and Chao Liu; an IEEE journal paper presented in the [FSE 2026 Journal-First track](https://conf.researchr.org/details/fse-2026/fse-2026-journal-first/40/Hydra-Reviewer-A-holistic-multi-agent-system-for-automatic-code-review-comment-gener). Only the listing was read: IEEE Xplore (document 11203269) returned an empty page and no preprint was found.
- **Tested:** agents built around a taxonomy of review dimensions from an empirical study, with context retrieval and reflection. It reports BLEU 8.20 against 7.85 for DeepSeek-V3, 7.8 dimensions covered per comment, and $0.018 and 62.63 s per change.
- **Closeness: medium.** Its dimension-based agents are the nearest thing to seat roles chosen from a taxonomy. It is scored by BLEU, and whether its ablation compares role sets couldn't be checked.

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
- **Closeness: high on scoring** (real known bugs, review by reading). It tests single agent set-ups, not councils, and there is no same-family analysis.

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
