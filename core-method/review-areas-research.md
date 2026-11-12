# Review areas for council seats: what the literature says

12 Nov 2026. Background for [outside-reviews.md](outside-reviews.md) entry 2, "Which review areas should council seats cover?". It checks that entry's claims and collects sources for choosing seat roles. It doesn't change the experiment plan.

**How each source was read:**
- **Read in full:** I downloaded the PDF and read the extracted text myself.
- **Read through a fetch tool:** the full page was fetched, but what I saw was a summary of it written by the fetch tool's model, with quotes. Treat figures from these as needing a second look before citing.
- **Abstract or listing only:** only the abstract, the author's page or a conference listing was read.
- **Snippet only:** seen only in search-result snippets.

## (a) Software quality models

### ISO/IEC 25010:2023, product quality model

- **Links:** the [ISO/IEC FDIS 25010 sample](https://cdn.standards.iteh.ai/samples/78176/da352588834f46f2a1235f00d1fc23db/ISO-IEC-FDIS-25010.pdf) on iTeh, whose foreword and introduction I read in full, and the [iso25000.com pages on ISO/IEC 25010](https://iso25000.com/index.php/en/iso-25000-standards/iso-25010), read through a fetch tool. The ISO catalogue page ([78176](https://www.iso.org/standard/78176.html)) refused the fetch.
- **What it says:**
  - The product quality model has "nine characteristics (which are further subdivided into subcharacteristics)". In the 2023 edition they are functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility and safety.
  - **Changes from the 2011 edition (foreword, read in full):** "Safety has been added as a quality characteristic"; "Usability and portability have been replaced with interaction capability and flexibility respectively"; maturity became faultlessness; and resistance and scalability were added under security and flexibility.
  - **Subcharacteristics, through a fetch tool:**
    - performance efficiency: time behaviour, resource utilisation and capacity;
    - compatibility: co-existence and interoperability;
    - interaction capability: eight, including user error protection, user assistance and self-descriptiveness;
    - reliability: faultlessness, availability, fault tolerance and recoverability;
    - security: confidentiality, integrity, non-repudiation, accountability, authenticity and resistance.
  - **Snippet only:** maintainability (modularity, reusability, analysability, modifiability and testability) and flexibility (adaptability, scalability, installability and replaceability).
- **Claims in entry 2:**
  - **Confirms** ISO/IEC 25010 as a reference point, and that the current three seats cover only part of it. Correctness maps to functional suitability. Security and privacy maps to security, though the model has no privacy characteristic of its own; confidentiality is the nearest. Docs and policy accuracy has no direct counterpart.
  - **Confirms** that maintainability, reliability, performance and compatibility are areas the seats don't name.
  - **Qualifies two points.** "Usability" is called interaction capability in the 2023 edition. And the model has two more areas that entry 2 didn't list: flexibility and safety.
  - **The app's own tests aren't a characteristic.** The nearest is testability, a subcharacteristic of maintainability, which is about how easily a product can be tested, not whether its tests test the right things.
- **For choosing seats:** the model is a product quality model, not a review checklist. It says what quality is made of, not what a reviewer can find by reading code. It's still a usable coverage map: for each seat, record which characteristics it is meant to cover, and say which are left out on purpose.

## (b) What code reviewers actually flag

### Mäntylä and Lassenius 2009, "What Types of Defects Are Really Discovered in Code Reviews?"

- **Link:** [author's page](https://mmantyla.github.io/wiki/What+Types+of+Defects+Are+Really+Discovered+in+Code+Reviews%253F.html) (IEEE TSE 35(3), [doi:10.1109/TSE.2008.71](http://doi.ieeecomputersociety.org/10.1109/TSE.2008.71)). **Abstract only:** the full-text PDF the page links to wouldn't load over a secure connection, so I didn't read it.
- **What it says:** defects from 9 industrial (C/C++) and 23 student (Java) reviews, 388 and 371 defects, were classified as functional or evolvability defects. "75 percent of defects found during the review do not affect the visible functionality of the software."
- **Claims in entry 2:** **confirms** that most of what review finds isn't functional bugs. The paper's word is evolvability, which is close to maintainability.

### Beller, Bacchelli, Zaidman and Juergens 2014, "Modern Code Reviews in Open-Source Projects: Which Problems Do They Fix?"

- **Link:** MSR 2014, [doi:10.1145/2597073.2597082](https://doi.org/10.1145/2597073.2597082), with a full text in the [TU Delft repository](https://repository.tudelft.nl/record/uuid:8747d363-137b-4a9a-a02a-f8aebd26c674). **Snippet only:** the repository refused the connection, so I read only search-result summaries of the abstract.
- **What it says:** over 1,400 review-induced changes in two open-source projects were classified by hand. The mix of maintainability and functional changes was about 75:25, matching the earlier studies. 7% to 35% of review comments were discarded, and 10% to 22% of changes weren't triggered by an explicit review comment.
- **Claims in entry 2:** **confirms** the maintainability majority, in open-source projects.

### Bacchelli and Bird 2013, "Expectations, Outcomes, and Challenges of Modern Code Review"

- **Link:** ICSE 2013, [PDF at Microsoft Research](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ICSE202013-codereview.pdf). **Read in full.**
- **What it says:**
  - At Microsoft, 570 comments in 200 review threads were card-sorted into nine categories.
  - **Code improvements were the largest category:** "The most frequent category, with 165 (29%) comments, is 'code improvements'": 58 on better code practices, 55 on removing unnecessary or unused code and 52 on readability.
  - **Defects came fourth:** "the category 'defect' is the only the fourth most frequent, out of nine items, with 78 (14%) comments". Of those, 65 were logic issues, 6 high-level issues, 5 security and 3 wrong exception handling.
  - **The gap with what people expect:** finding defects was still the first motivation for 383 programmers (44%) and the top reason for 44% of managers.
- **Claims in entry 2:** **confirms** that reviews flag code improvements more than bugs. Code improvements aren't the majority here, though: they are the largest single category, at 29%.
- **For choosing seats:** security came up in 5 of the 570 comments. Human reviewers in this sample rarely raised it, which is one argument for giving security its own seat rather than hoping a general reviewer covers it.

### Czerwonka, Greiler and Tilford 2015, "Code Reviews Do Not Find Bugs"

- **Link:** ICSE 2015 (SEIP), [PDF at Microsoft Research](https://microsoft.com/en-us/research/wp-content/uploads/2015/05/PID3556473.pdf). **Read in full.** It's a two-page talk abstract, so it summarises Microsoft data rather than presenting it.
- **What it says:**
  - "Only about 15% of comments provided by reviewers indicate a possible defect, much less a blocking defect."
  - Feedback on "long-term code maintainability" makes up "at least 50% of all".
  - Without prior exposure to the code, "only 33% of any reviewer's comments are deemed useful", rising to about 67% by the third review of the same code. Usefulness falls as the number of files in a review rises.
- **Claims in entry 2:** **confirms** that maintainability comments outnumber defect comments, in Microsoft's data.
- **For choosing seats:** usefulness depends on familiarity and review size. Each council seat starts with no familiarity, and the briefs could split large material.

### Goldman et al. 2025, "What Types of Code Review Comments Do Developers Most Frequently Resolve?"

- **Link:** [arXiv 2510.05450](https://arxiv.org/html/2510.05450v1) (Melbourne, Atlassian and Monash). **Read through a fetch tool.**
- **What it says:**
  - **Taxonomy:** six Atlassian engineers card-sorted 336 human comments into readability, bugs, maintainability, design, no issue and other.
  - **Human comments on internal projects:** readability 46.0%, maintainability 19.1% and bugs 6.5%.
  - **LLM-written comments:** readability 33.2%, maintainability 26.8% and bugs 18.2%.
  - **Resolution rates of LLM comments:** readability 43.3%, bugs 41.9%, maintainability 36.2% and design 28.6%. 60% to 70% of the LLM's comments weren't resolved.
- **Claims in entry 2:** **confirms** that bugs are a small share of human review comments. **Qualifies** "maintainability": here readability is the largest category, and maintainability alone is under a fifth. The robust finding across sources is that non-bug comments dominate. Which non-bug category leads depends on the taxonomy.
- **For choosing seats:** an LLM reviewer already raises more bug comments than humans do, and most of its comments go unresolved. So the cost of false or unwanted flags matters as much as coverage when seats are added.

## (c) Review areas for LLM or automated review, specialised roles and checklists

### Tufano et al. 2024, "Code Review Automation: Strengths and Weaknesses of the State of the Art"

- **Link:** [arXiv 2401.05136](https://arxiv.org/abs/2401.05136). **Abstract only.**
- **What it says:** it analyses where automated review techniques succeed and fail, and produces "two taxonomies", one for commenting on a change and one for revising code after a comment. RevAgent (below) takes five issue categories from it: refactoring, bug fix, testing, logging and documentation. I saw those categories only through RevAgent.
- **Claims in entry 2:** testing as a category of its own **supports** treating the app's tests as a review area.

### Li et al. 2025, RevAgent: "Issue-Oriented Agent-Based Framework for Automated Review Comment Generation"

- **Link:** [arXiv 2511.00517](https://arxiv.org/html/2511.00517v1). **Read through a fetch tool.**
- **What it says:**
  - **Design:** five category-specific "commentator" agents, one per issue type, each write a candidate comment on a diff hunk. A critic agent then picks the best one.
  - **Specialised agents win:** in the ablation, "using multiple specialized commentator agents significantly improves the generation of category-aligned comments" compared with one unified agent.
  - **The critic matters most:** "the critic agent plays the most crucial role".
  - **Setting:** the agents are fine-tuned small models, scored by similarity to human comments and by human ratings.
- **Claims in entry 2:** **bears on** "fold in or give it a seat". It favours specialised agents, but in a different task: writing comments that resemble human ones, not catching planted bugs. Like the council, its critic plays the role of a judge.

### Tang et al. 2024, CodeAgent: "Autonomous Communicative Agents for Code Review"

- **Link:** [arXiv 2402.02172](https://arxiv.org/abs/2402.02172). **Abstract only.**
- **What it says:** a multi-agent reviewer with a supervising "QA-Checker" agent. It covers four tasks: inconsistencies between code changes and commit messages, vulnerabilities introduced, code style and suggested revisions.
- **For choosing seats:** another role split chosen from practice. Its consistency task, checking code against its stated intent, is close to the docs and policy accuracy seat.

### Hydra-Reviewer, "A holistic multi-agent system for automatic code review comment generation"

- **Link:** [FSE 2026 journal-first listing](https://conf.researchr.org/details/fse-2026/fse-2026-journal-first/40/Hydra-Reviewer-A-holistic-multi-agent-system-for-automatic-code-review-comment-gener). **Listing and snippet only:** I found no full text.
- **What it says:** it builds "a comprehensive taxonomy of code review dimensions" from an empirical study, then a multi-agent framework on that taxonomy. Its comments span 7.8 review dimensions on average.
- **For choosing seats:** this is the source most likely to offer a ready-made taxonomy of review dimensions for LLM review. It should be read before the seat roles are settled.

### Gonçalves et al. 2022, "Do explicit review strategies improve code review performance? Towards understanding the role of cognitive load"

- **Link:** Empirical Software Engineering 27:99, [doi:10.1007/s10664-022-10123-8](https://doi.org/10.1007/s10664-022-10123-8). **Read in part:** I read the abstract and the participant section from the full text. It's a registered report.
- **What it says:**
  - **Design:** 67 professional Java developers were each given ad hoc reviewing, a checklist or a guided checklist; most were novice reviewers.
  - **Mixed results:** "the guided checklist is a more effective aid for a simple review, while the checklist supports reviewers' efficiency and effectiveness in a complex task. However, we did not identify a strong relationship between the guidance provided and code review performance."
- **Claims in entry 2:** **bears on** folding areas into briefs as subsections, which works like a checklist. For human reviewers, the evidence that checklists help is mixed. That supports testing it, as entry 2 proposes, rather than assuming it.
- **Also relevant:** it's an example of a registered report in software engineering, the model for locking the plan.

## Entry 2's claims, in short

| Claim | Status |
|---|---|
| The seat roles came from practice, not a framework | Consistent: none of the sources proposes these three roles, and ISO/IEC 25010 doesn't match them. The literature can't confirm the project's history. |
| ISO/IEC 25010 is a reference point | Confirmed. The current edition is 2023, with nine characteristics. |
| Most review comments concern maintainability, not bugs | Confirmed in substance by five sources: defect comments run from about 6.5% to 25%. Qualified: the sources call the majority evolvability, code improvement, maintainability or readability, and in two of them (Bacchelli and Bird; Goldman et al.) no single non-bug category is a majority. |
| Areas not covered: maintainability, reliability, performance, the app's tests, usability, compatibility | Consistent with ISO/IEC 25010, which calls usability interaction capability and also lists flexibility and safety. The app's tests aren't an ISO characteristic, but they are a category in Tufano et al.'s taxonomy, seen through RevAgent. |
| The WinScope pilot's 97 problems passed the builders' tests | Confirmed in this repo: [winscope-pilot.md](winscope-pilot.md) says the review rounds "found 97 problems that the builders' own tests had passed". |
| Many performance problems can be spotted by reading the code | Not checked: none of the sources read covers it. |
| Fold areas into briefs or give them seats | Not settled by the literature. RevAgent favours specialised agents for writing comments, and checklists help human reviewers only in some conditions. Testing role sets against each other on the same seeds, as entry 2 proposes, is the way to settle it. |

## How this bears on choosing seat roles

1. **Use ISO/IEC 25010:2023 as the coverage map.** For each seat, record which characteristics it covers, and list the ones left out on purpose (for example interaction capability for Claude skills).
2. **Seeds and seats have to match.** Human reviewers mostly raise non-functional issues, but the experiment scores seats only on planted bugs. A maintainability seat would look useless if the seeds hold no maintainability problems. If maintainability or performance is in scope, the seeds need a stated mix of those categories too. Otherwise keep those areas out of the scored experiment.
3. **Count the cost of extra flags.** LLM reviewers raise many comments that go unresolved (60% to 70% in the Atlassian study), so each new area adds false or unwanted flags as well as catches. The scoring already counts false flags, which is the right place to see it.
4. **Specialised seats or folded-in subsections is an open question.** RevAgent's ablation favours specialised agents, in a different task. Checklist evidence for humans is mixed. A head-to-head test on the same seeds is needed.
5. **Read Hydra-Reviewer before settling.** It's the one source found with a taxonomy of review dimensions built for multi-agent LLM review.
6. **Not found:** a study comparing role sets for LLM review councils against planted bugs. If none exists, this experiment would be the first.
