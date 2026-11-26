# Behavioral and International Interviews

[🇺🇸 English](README.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

<!-- chapter-navigation:top -->
[← Previous](../22-technical-interview-question-bank/README.md) · [Module index](../README.md) · [Next →](../24-mock-interviews-and-self-assessment/README.md)
<!-- /chapter-navigation:top -->

## Prerequisites

- [Interview foundations](../01-understanding-technical-interviews/README.md)
- [Live coding and take-home assignments](../02-live-coding-and-take-home/README.md)
- [Technical decisions](../21-software-engineering-and-technical-decisions/README.md)

## Behavioral evidence with STAR

Behavioral interviews ask how you acted in a particular situation. A project, class, volunteer activity or personal exercise can provide evidence; do not imply paid work if it was not. Use STAR: Situation (brief context), Task (your responsibility), Action (your personal decisions and steps), Result (observable outcome and learning). A result need not be numeric. Use a number only if you can substantiate it. Distinguish team results from your contribution, and describe what you would improve. Protect customer data, credentials and internal code.

Fictional rehearsal: a study group's script counted duplicate lesson IDs (S). You were responsible for the counting rule (T). You clarified the requirement, added a duplicate-input test, changed the calculation and reran the test (A). The test now passed for the agreed example, and you noted that storage integration still needed verification (R). This example is invented for practice, not a statement about your work.

## International interviews and technical English

Processes vary by employer, country and role. Before the session, confirm the time zone, language, tool policy, expected format and accessibility needs. During the session, use short, precise sentences. Ask for clarification, restate the contract, state an assumption, explain the trade-off, and report verified versus unverified outcomes. You can ask to repeat or rephrase a question. A particular accent or advanced vocabulary is not a correctness criterion. Use English for practice when the role requires it; do not pretend to understand an unfamiliar term.

| Purpose | English phrase |
| --- | --- |
| Clarify | Could you clarify whether duplicate IDs count? |
| Confirm | Let me restate the requirement. |
| State an assumption | I am assuming the input is sorted. Is that correct? |
| Explain a trade-off | This approach uses extra memory to avoid repeated scans. |
| Respond to feedback | Thanks. I will check the failing case and revise my approach. |
| Report evidence | The empty-input test passed; I have not tested the database boundary. |
| Ask for time | May I take a moment to think through the edge case? |

Suppose an interviewer asks to return the first occurrence and then clarifies that the result should instead be the first insertion position. Acknowledge the changed contract, give a discriminating example, revise the planned tests and explain what you have not run. Do not claim both contracts are equivalent. Practice the clarification and the summary aloud, then repeat in a second language if useful.

## Disagreement, ownership and trade-offs

For a disagreement, first state the shared goal and constraints. Ask why the other option is preferred, compare alternatives using evidence and agree a small validation step or documented decision. Explain your individual contribution, the team's decision and the observed outcome separately. If evidence is incomplete, state the uncertainty, the risk and the next test instead of claiming a win. If a decision is made against your recommendation, explain how you supported the agreed plan and monitored risk. Avoid blame and confidential details.

Fictional rehearsal: a team proposes a cache to reduce response latency. You own the investigation; your colleague proposes splitting the service. Agree a latency target, inspect the baseline, compare alternatives against memory, staleness and operational costs, and document an experiment. If no measurements exist yet, report the proposed experiment, not an invented improvement. Relate this to the ADR and measurement guidance in chapter 21.

## Independent practice

Prepare two true, nonconfidential stories (a bug or learning challenge and a disagreement). Label any simulated story as fictional. Record a two-minute STAR answer; identify missing evidence and revise. Next, rehearse a clarification, a complexity explanation and a truthful status update in English. Evaluate whether the listener can restate your contract and trade-off, not whether your accent resembles theirs.

**Quick reference:** truthful evidence; clarify; restate; explain decisions; report actual results; disclose limitations.

<!-- chapter-navigation:bottom -->
[← Previous](../22-technical-interview-question-bank/README.md) · [Module index](../README.md) · [Next →](../24-mock-interviews-and-self-assessment/README.md)
<!-- /chapter-navigation:bottom -->
