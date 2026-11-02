# Council evidence check: debate, personas and self-correction

Nov 2, 2026

Five claims the project makes about debate, personas and self-correction, checked against the three papers they come from. For each claim: a verdict (supported, partly supported or wrong), the exact numbers, and where in the paper they are. After that, a section on what these papers say **in favour of** councils and role diversity, so the summary stays balanced.

**How sources were checked.** Each source is marked:

- **Full text:** I opened the PDF and read the whole paper, appendices included. The version is named.
- **Abstract only:** only the abstract or landing page was read.

All three papers here are **full text**. I downloaded the PDFs from arXiv, converted them to text and read them myself; no subagents were used. Plots came through only as axis labels, so I quote numbers from tables and prose, not values read off figures. Where a table's columns were scrambled in the text, I rebuilt it and checked it against the numbers quoted in the prose. Where a symbol such as ≤ was lost in the conversion, I say so.

| Source | Version read | How read | Status |
|---|---|---|---|
| Ferreira, Liu & Zheng, "Beyond Symmetric Agents: Cognitive Diversity and Multi-Agent Debate in Small Language Models" | arXiv:2609.35875v1, 26 Sep 2026 | **Full text** (sections 1–8, appendices A–L) | Preprint, not peer reviewed |
| Smit, Grinsztajn, Duckworth, Barrett & Pretorius, "Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs" | arXiv:2311.17371v3, 18 Jul 2024 | **Full text** (main paper and appendix A) | ICML 2024 (PMLR 235; the venue is printed in the PDF, not on the arXiv page) |
| Huang, Chen, Mishra, Zheng, Yu, Song & Zhou, "Large Language Models Cannot Self-Correct Reasoning Yet" | arXiv:2310.01798v2, 14 Mar 2024 | **Full text** (main paper and appendix A) | ICLR 2024 |

## Contents

1. [Summary](#1-summary)
2. [The five claims](#2-the-five-claims)
3. [What argues for councils or role diversity](#3-what-argues-for-councils-or-role-diversity)
4. [Wording to fix elsewhere in the repo](#4-wording-to-fix-elsewhere-in-the-repo)
5. [Sources](#5-sources)

## 1. Summary

| # | Claim | Verdict |
|---|---|---|
| 1 | At equal generations, debate tied or lost to repeated sampling plus majority vote, at about 3.4 times the tokens | **Supported** |
| 2 | Debate gains were mainly an ensemble effect | **Supported** |
| 3 | Assigned personas lowered accuracy | **Supported for Ferreira's setting.** Smit is mixed, so it isn't a general rule |
| 4 | The tasks were reasoning tasks, not independent code review | **Supported** on the part that matters (no code review). "Reasoning tasks" is too narrow |
| 5 | Models struggle to correct their own reasoning without outside feedback | **Supported** |

The main things to keep in mind:

- **3.4× is total tokens, not generated tokens.** Debate generates about the same number of tokens as the vote (1.06×). The extra cost comes from re-reading the other agents' transcripts every round.
- **"Tied or lost" is the paper's own wording, and it's accurate**, but debate is slightly ahead on two of the four tasks (by amounts too small to count). Losses are clear only on CommonsenseQA and for mixed-model teams.
- **The persona result is about small models (0.6B–109B) wearing deliberately odd personas** ("a Zen master who communicates only through … koans"), not task-matched expert roles. The authors expect larger models to pay less.
- **None of the three papers tests code review or independent review.** All of them test debate or self-correction on tasks with a single right answer.

## 2. The five claims

### Claim 1. At equal generations, debate tied or lost to repeated sampling plus majority vote, at about 3.4 times the tokens

**Verdict: supported.** Source: Ferreira, section 5.1, Table 1, Table 18 (appendix H).

**Setup.** Three agents debate for three rounds, giving 9 generations, and are compared with 9 independent samples from the same model, majority-voted ("SC-9", self-consistency). Same model, same temperature spread, same 100 problems for each of 23 models.

**Table 1** (mean accuracy %, 23 models, after the context-window fix described below):

| Task | Solo | Debate (3×3) | SC-9 vote | Debate − vote |
|---|---|---|---|---|
| Arithmetic | 91.2 | 91.5 | 90.6 | +0.9 (not significant) |
| GSM8K | 87.9 | 91.2 | 91.0 | +0.2 (not significant) |
| MMLU | 69.9 | 76.5 | 76.8 | −0.3 (not significant) |
| CommonsenseQA | 72.6 | 78.3 | 80.6 | **−2.3** (p = 0.011) |
| Mean of these four | 80.4 | 84.4 | 84.8 | −0.4 |
| Biography (claim precision) | 54.6 | 55.6 | 64.6 | −8.9 (see caveat) |

- The paper says the advantage "disappears in all cases and it is indistinguishable from zero on math, GSM8K, and MMLU", and that "at equal generation counts, debate ties or loses to sampling-plus-voting on every task".
- **Cost** (Table 18, mean over tasks): debate takes **1.61×** the wall-clock time and **3.42×** the total tokens, with a range of about **2.3–4.1×** across tasks. Generated tokens are only **1.06×**, so the gap is debate re-reading its peers' transcripts. Token ratios are medians over the 23 models.
- **Mixed-model teams** (section 5.3, Table 2): 80 three-model teams lost to a 9-sample vote over the same models by **−1.04 points** (95% CI −1.61 to −0.52). Debate won only 83 of 320 team-task cells, and the median difference was exactly zero. This repeated at a second problem seed (**−0.93**, CI −1.45 to −0.44). Pairs with the strong model duplicated lost by **−2.68**. Four-model teams were level with the vote (+0.04 and +0.56, neither significant).
- **Harder questions** (appendix G): on GPQA Diamond, debate minus SC-9 is **−0.6 points** (CI −2.2 to +1.0) once a thinking-budget bug that was handicapping the vote is fixed. On MMLU-Pro the vote leads by **2.0 points**.
- **Caveat on biography:** the 64.6 is inflated partly by how claims are pooled. The authors say the debate comparison "is the robust one" (appendix E). Don't quote −8.9 as the headline number.

**The other two papers agree.**

- **Huang** (section 4, Table 7; GPT-3.5, all 1,319 GSM8K test problems, 3 agents): debate scores **83.2** with 6 responses against **85.3** for a 6-sample vote, and **83.0** with 9 responses against **88.2** for a 9-sample vote. Debate only edged a vote over 3 samples (82.5), which is the baseline the original debate paper used.
- **Smit** (abstract, section 3, Table 2) found that debate systems "do not reliably outperform" self-consistency or ensembling. Smit didn't match budgets as strictly, comparing best configurations against cost and API calls instead.

### Claim 2. Debate gains were mainly an ensemble effect

**Verdict: supported.** Sources: Ferreira abstract and sections 5.1, 5.2 and 8, Table 13. Huang section 4.

- **Ferreira** puts it more strongly than "mainly": debate's gains are "an ensemble-sampling effect: nearly all benefit arrives with the first exchange, and none survives budget matching" (section 8).
- **Rounds ablation** (Table 13, 10 mixed teams, not budget-matched): mean accuracy **84.6%** at 1 round (just a vote), **87.2** at 2, 87.4 at 3, 87.5 at 4 and 87.0 at 5. CommonsenseQA falls after round 2. So the one exchange of answers does add about 2.6 points over a 3-vote. But 9 independent votes buy as much without any exchange.
- **Varying temperature alone does nothing** (section 5.2): spreading the vote's samples over temperatures 0.5–1.0 changed accuracy by **−0.11 to −0.41 points** across 92 model-task cells, none significant.
- **Huang**: debate's improvement "is evidently not attributed to 'self-correction', but rather to 'self-consistency'".
- **Qualification:** the exchange isn't useless, just expensive. Debate corrects more answers than it breaks: helpful answer changes outnumber harmful ones **7.6% to 4.0%** of agent-problem pairs. Mixed teams overturn **63.7%** of wrong first-round majorities, against **42.9%** for teams of one model (sections 5.1 and 8). Voting simply gets at least as much accuracy for the same budget.
- **Smit** is less sure it's only ensembling. They argue debate is "not necessarily" worse but "more sensitive to hyperparameters". See section 3.

### Claim 3. Assigned personas lowered accuracy

**Verdict: supported for Ferreira's setting, but not a general rule.** Sources: Ferreira section 5.2, Figures 1–2, section 6, appendices E and L. Smit section 3, Figure 4.

**Ferreira's numbers:**

- **Most diverse persona teams against plain debate** (same model, team size and budget): lower by **−2.1 to −4.4 points**. This is significant on GSM8K at 3 and 5 agents and on CommonsenseQA at every team size (p ≤ 0.005; the ≤ sign was garbled in the PDF text, and ≤ is the likely reading). It is lower, but mostly not significantly, on MMLU and biography: −3.8 to −5.0 points, significant at 5 agents. The paper doesn't make clear whether that range covers both tasks or only biography. Table 1 means: persona debate **81.9** against plain debate **84.4**.
- **Any persona at all costs accuracy.** Even the most redundant trio of near-identical personas loses **−4.3** on GSM8K (p = 0.012), **−4.2** on MMLU (p = 0.003), **−7.3** on CommonsenseQA (p = 10⁻⁴) and **−7.1** on biography (p = 0.048). The authors call this "a persona tax, not a diversity tax".
- **Persona debate is also slower:** 1.26× the wall-clock time of plain debate (appendix H).

**Scope limits, all from the paper:**

- **Small open models only.** The tax shrinks as models get stronger (Spearman +0.46, p = 0.027): "stronger models afford the costume".
- **The personas were chosen to be extreme, not useful.** All persona teams come from a pool of 50 "extreme unconventional" personas (appendix L), such as a pirate captain, a pre-lingual infant, a Zen master speaking in koans and a Gothic novelist. They are not task-matched roles like "security reviewer". The authors note that "task-aligned persona choice, fine-tuned styles, or tool and information asymmetries could produce cognitive diversity that prompting cannot" (section 7).
- **The biography penalty depends on the judge.** It is significant only under the Gemma judge (−7.4 points); neither OpenAI judge alone sees it (appendix E).
- **There is a counterexample.** The largest model in the pool, Llama-4-Scout, did better with diverse personas than the matched vote: **87.0 vs 83.0** on MMLU and **91.0 vs 89.0** on CommonsenseQA. The authors call this "an anecdote, not a trend".

**Smit is mixed.** Their "Multi-Persona" system gives one agent the role of an "angel" and the other a "devil" prompted to disagree. Untuned, it lowered accuracy compared with the first agent's opening answer (Figure 4), and on MedQA it ran "consistently about 7% worse" than Medprompt. Tuned so the devil agrees 90% of the time, it went from "the worst-performing protocol to the best-performing" on MedQA (section 4). Those personas set how much an agent argues, not what it is an expert in.

### Claim 4. The tasks were reasoning tasks, not independent code review

**Verdict: supported on the part that matters. "Reasoning tasks" is too narrow.**

None of the three papers tests code review, and none tests independent review where reviewers don't see each other's work. All of them test debate (agents read each other's answers) or self-correction, on tasks with a checkable answer. But the tasks aren't all reasoning:

| Paper | Tasks |
|---|---|
| Ferreira | 100 arithmetic expressions, GSM8K maths, MMLU four-choice academic questions, CommonsenseQA, **factual biographies of 40 computer scientists** (scored claim by claim by LLM judges), plus MMLU-Pro, GSM-Symbolic and GPQA Diamond (section 4.2, appendix G) |
| Smit | Multiple-choice QA: **MedQA, PubMedQA, MMLU clinical topics** (medical knowledge), CosmosQA, CIAR counter-intuitive arithmetic, GPQA, **BIG-bench chess state tracking** (section 3) |
| Huang | GSM8K, CommonSenseQA, **closed-book HotpotQA** (multi-hop QA), plus **CommonGen-Hard constrained generation** in section 5 |

Ferreira says plainly that "objectively verifiable domains such as BIG-Bench Hard or code generation remain untested here", and that "domains valuing novelty or synthesis may reward diversity differently" (section 7). Huang mentions code only through other people's work (section 6).

**Suggested wording:** "knowledge and reasoning tasks with a single checkable answer (plus factual biography writing), all in a debate or self-correction setup, never code review."

### Claim 5. Models struggle to correct their own reasoning without outside feedback

**Verdict: supported.** Source: Huang, sections 3 and 6, Tables 2–6.

The abstract says: "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction." In the results, accuracy is lower after two rounds of self-correction for every model on every benchmark (section 3.2).

**Intrinsic self-correction** (no correct answers given), accuracy % as initial → round 1 → round 2:

| Model | GSM8K | CommonSenseQA | HotpotQA |
|---|---|---|---|
| GPT-3.5 | 75.9 → 75.1 → 74.7 | 75.8 → 38.1 → 41.8 | 26.0 → 25.0 → 25.0 |
| GPT-4 | 95.5 → 91.5 → 89.0 | 82.0 → 79.5 → 80.0 | 49.0 → 49.0 → 43.0 |
| GPT-4-Turbo | 91.5 → 88.0 → 90.0 | 84.0 → 81.5 → 83.0 | not tested |
| Llama-2-70B | 62.0 → 43.5 → 36.5 | 64.0 → 37.5 → 36.5 | not tested |

- **Earlier gains came from leaking the right answer** (Table 2). When the correct answer is used to decide when to stop, accuracy rises: GPT-3.5 goes 75.9 → 84.3 on GSM8K and 75.8 → 89.7 on CommonSenseQA, and GPT-4 goes 49.0 → 59.0 on HotpotQA. The authors call this "an oracle's performance".
- **Why accuracy drops:** on GSM8K, GPT-3.5 kept its answer 74.7% of the time. When it did change, it was more likely to turn a right answer wrong than a wrong answer right (Figure 1).
- **None of the three feedback prompts tried helped** (Tables 5–6).
- **Scope:** reasoning only. The models are from 2023 (the title says "yet"). Self-correction of style or safety is outside the claim, and the authors note it has worked in earlier studies (section 7).

## 3. What argues for councils or role diversity

None of this overturns sections 1 and 2, but it should be in any balanced summary.

**Ferreira**

- **Debate does beat one model working alone**, by +3.3 points (GSM8K), +6.6 (MMLU) and +5.7 (CommonsenseQA), all p < 0.002 (section 5.1). Its weakness is cost against voting, not quality against a single model.
- **A mix of different models is useful**, if you vote. On knowledge tasks, weak and mid-tier mixed teams beat their own best member by 10 points in 19 team-task cells. The matched vote did even better (+16.4 against debate's +13.5). The practical advice is to "pool different small models and vote (mixed rosters lift weak deployments 10-20 points over their best member, no debate needed)" (section 5.3, appendix K). That is a point for a **council of different models that votes independently**, which is closer to this project's design than debate is.
- **Variety of roles beats sameness.** Once agents wear personas, more varied teams do better than redundant ones: +2.9 points on MMLU (p = 0.003) and +3.3 on biography from the most redundant team to the most varied. Redundant personas were "the most harmful configuration we test", because they "add correlated bias that majority voting cannot remove" (sections 5.2, 6).
- **Mixing models costs nothing.** Unlike personas, it "is harmless" (section 6). Debate's shortfall is largest for the least varied teams and gone for the most varied: −2.68 for strong-duplicated pairs, about zero for four-model teams (Table 2).
- **There are a few debate wins.** Weak-duplicated four-model teams on MMLU beat the vote by +2.80 points (CI +0.9 to +4.6), and all-strong teams by +0.44 (Tables 10, 12). Llama-4-Scout persona teams beat the vote too (claim 3).
- **Larger models may behave differently.** The authors expect larger models could "adopt unconventional cognitive frames without paying the tax", and call "whether larger models can convert diversity into genuinely deliberative gains" "the natural follow-up" (sections 6–7).
- **Other work they cite points the same way.** The "most consistently positive reported reason" for debate is model heterogeneity (citing Chen et al. 2023 and Zhang et al. 2025). Debate's clearest wins come "under information asymmetry" (citing Khan et al. 2024 and Kenton et al. 2024), where agents see different things (section 2). A review council where each reviewer looks at different files or tools is closer to that than to symmetric debate.
- **Some apparent losses were measurement errors.** Transcripts overflowing the context window made debate look 1.84 points behind the vote. Fixed, the gap is −0.06 (section 5.5). The GPQA gap closed the same way after a budget bug was fixed. Debate isn't worse than voting, only more expensive.

**Smit**

- **Debate isn't inherently worse.** It is "more sensitive to different hyperparameter settings and difficult to optimize" (abstract).
- **Tuning how much agents agree helps a lot:** about **+15%** for Multi-Persona and +5% for Society of Mind on a 376-question USMLE subset (the paper doesn't say whether these are points or relative). At 90% agreement, Multi-Persona became the best method on full MedQA, beating Medprompt and self-consistency (section 3, Conclusions).
- **A dissenting role pays off on trick questions.** On CIAR, which was built to be counter-intuitive, accuracy rose when the second agent was told to disagree strongly (section 3, Figure 5). That suggests a devil's-advocate role helps where the obvious answer is wrong.
- **The persona method held up on new data.** Settings were chosen on other datasets of the same kind and then applied to new ones (Figure 3). On the non-medical datasets, single agents beat every method except Multi-Persona and self-consistency. On the medical datasets, every method except Multi-Persona beat single agents, so the persona system's result changes with the domain.
- **Society of Mind gained the most from debating**, comparing its final answer with the first agent's opening answer (Figure 4).

**Huang**

- **Outside feedback works, and "other models" counts as outside feedback.** Huang's definition of external feedback includes "inputs from humans, other models … or external tools" (section 2). They recommend using valid outside feedback where it exists, for example code execution results and unit tests (section 6). A reviewer that is a different model, or that runs the code, is outside feedback by this definition. Note the limit, though: Huang's own debate test used copies of one model and gained nothing over voting.
- **Debate narrowly beat a 3-sample vote** (83.2 vs 82.5, Table 7), although it lost at equal response counts.

## 4. Wording to fix elsewhere in the repo

I haven't edited these, because another session has uncommitted changes in `core-method/experiment-plan.md`. They're listed here for whoever next updates that file.

- **Ferreira summary (sources list):** "on maths and quiz questions" leaves out the biography-writing task and the GPQA Diamond and MMLU-Pro slices. "Personas lowered accuracy" needs the scope added: small models with extreme, not task-matched, personas. "At a fraction of the token cost" is right: the vote uses about 1/3.4 of debate's total tokens.
- **Huang summary:** "Supports using fresh reviewers rather than self-review" goes slightly beyond the paper. Huang shows self-review fails and outside feedback helps, and counts other models as outside feedback. But its only test of other agents used copies of the same model, which matched voting and did no better. It supports *different* models or tool-based checks more than fresh copies of the same model.
- **Smit summary:** fine as written. Consider adding that tuning agreement made Multi-Persona the best method on MedQA, so debate isn't shown to be worse in principle.

## 5. Sources

- Ferreira, L., Liu, G., & Zheng, K. (2026). [Beyond Symmetric Agents: Cognitive Diversity and Multi-Agent Debate in Small Language Models](https://arxiv.org/abs/2609.35875). arXiv:2609.35875v1, preprint. **Full text.**
- Smit, A., Grinsztajn, N., Duckworth, P., Barrett, T. D., & Pretorius, A. (2024). [Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs](https://arxiv.org/abs/2311.17371). ICML 2024, PMLR 235. arXiv:2311.17371v3. **Full text.**
- Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X., & Zhou, D. (2024). [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798). ICLR 2024. arXiv:2310.01798v2. **Full text.**
