<div align="center">

# AI-Assisted Development

[🇺🇸 English](README.en.md) · [🇧🇷 Português](README.pt-BR.md) · [🇪🇸 Español](README.es.md)

</div>

Artificial intelligence can accelerate research, organization, explanation, translation, programming, and review. It can also produce incorrect, incomplete, outdated, or fabricated information with confident language.

This project therefore uses AI as a support tool, not as a final authority.

The guiding principle is simple:

> Use AI to expand your ability to think, build, verify, and learn. Do not use it to surrender responsibility for the result.

## Purpose of this document

This page explains:

- how AI supports Python Study Guide;
- how a beginner can speak with an AI assistant;
- how to provide useful context;
- how to write and refine prompts;
- how to ask for teaching instead of only answers;
- how to turn a conversation into an implementation brief;
- how to send a reviewed brief to Codex;
- how to validate AI-assisted work;
- how to protect private and confidential information.

No previous experience with AI tools is required.

## How AI supports this project

ChatGPT and Codex may assist with activities such as:

- planning repository structure;
- explaining Python concepts;
- researching and checking technical information;
- drafting and reviewing educational content;
- aligning English, Brazilian Portuguese, and Spanish documentation;
- creating original examples and exercises;
- identifying inconsistencies;
- reviewing pull requests;
- editing files and maintaining the repository.

Their roles are related but not identical.

### ChatGPT

ChatGPT is useful for conversation, explanation, study, brainstorming, comparison, drafting, translation, and turning an unclear idea into a structured plan.

### Codex

Codex is an AI coding agent that can work from a prompt or specification to inspect a repository, edit files, run commands, execute tests, review code, and prepare changes for human review.

The exact interfaces and available features may change. The durable workflow is more important than any particular button:

```text
Understand the problem
        ↓
Discuss and learn
        ↓
Define requirements
        ↓
Create an implementation brief
        ↓
Ask Codex to implement it
        ↓
Review files, tests, and explanations
        ↓
Open and review a pull request
        ↓
Merge only after validation
```

## Human responsibility

AI does not remove human responsibility.

A clear or persuasive answer is not automatically correct. The maintainer and contributor remain responsible for:

- understanding what is being submitted;
- checking technical claims;
- verifying important information with reliable sources;
- testing executable examples;
- reviewing translations;
- identifying unsupported assumptions;
- protecting private information;
- deciding whether a change is ready to merge.

Do not submit content you cannot explain, review, or defend.

## Think before writing the prompt

A useful prompt often begins before the message is typed.

Try to answer these questions in your own words:

1. What am I trying to accomplish?
2. What do I already know?
3. Where am I stuck?
4. What constraints must be respected?
5. What result would be useful?
6. How will I know whether the result is correct?

You do not need perfect answers. The goal is to give the conversation a direction.

## Anatomy of a useful prompt

A prompt can be organized with six simple elements:

| Element | Question it answers |
|---|---|
| Context | What situation are we working in? |
| Goal | What do I want to achieve? |
| Current state | What do I already have or understand? |
| Constraints | What rules or limits must be followed? |
| Expected result | What form should the answer take? |
| Validation | How should the result be checked? |

This is a guide, not a mandatory formula. A small question may need only one sentence. A repository change may need a detailed specification.

### Weak prompt

```text
Make a Python program.
```

The request is too broad. The AI must guess the audience, purpose, inputs, output, restrictions, and desired teaching style.

### Better learning prompt

```text
I am beginning to study Python and have not learned functions yet.

I want to create a small program that receives three grades and calculates
an average.

First, explain which basic concepts I need. Then show a simple example and
explain it line by line.

Do not give me a complete project immediately. At the end, give me a similar
exercise to solve on my own and provide the answer only after I try.
```

This prompt gives context, a goal, the learner's current level, a teaching constraint, and an expected result.

## Ask AI to help you think

AI can act as a tutor rather than an answer dispenser.

Useful instructions include:

```text
Do not give the complete answer yet. Give me one hint at a time.
```

```text
Explain why my solution fails, but let me try to correct it.
```

```text
Ask me questions to check whether I understood the concept.
```

```text
Compare my solution with another approach and explain the trade-offs.
```

```text
Tell me which parts of my reasoning are correct before discussing the mistake.
```

```text
After the explanation, ask me to summarize the concept in my own words.
```

The objective is not to make learning unnecessarily difficult. It is to keep the learner mentally involved.

## Refine the conversation

A good prompt does not need to be perfect on the first attempt.

A productive cycle is:

```text
Ask
  ↓
Read critically
  ↓
Identify what is missing or unclear
  ↓
Add context or constraints
  ↓
Ask for revision
  ↓
Verify the result
```

Examples of useful follow-up messages:

```text
Use a simpler vocabulary and define each technical term.
```

```text
Your example introduced lists, but I have not studied them yet. Rewrite it
using only variables, input, conversion, arithmetic, and print.
```

```text
Show the source for the technical claim about Python behavior.
```

```text
Create two test cases, including one that could reveal a common mistake.
```

Refinement is not failure. It is part of communicating requirements.

## From ChatGPT to Codex

ChatGPT can help transform an idea into a reviewed implementation brief. Codex can then work from that brief inside a repository.

Before sending the task to Codex, confirm that the brief describes:

- the repository context;
- the task;
- the files or area that may be changed;
- requirements;
- exclusions;
- acceptance criteria;
- validation steps;
- language and documentation rules.

### Example implementation brief for Codex

```text
Repository context

This is a multilingual educational Python repository for beginners.
Directory names, file names, code identifiers, code comments, branch names,
and commit messages must remain in English.
Documentation is maintained in English, Brazilian Portuguese, and Spanish.

Task

Create a beginner example that calculates the average of three grades.

Requirements

- Use only built-in Python features.
- Keep the example small and executable.
- Use descriptive English variable names.
- Explain the required concepts before the example.
- Create conceptually aligned documentation in all three supported languages.
- Use only original, fictional, and non-confidential data.
- Do not modify unrelated files.

Acceptance criteria

- The example runs without errors.
- The average is calculated correctly.
- The explanation is suitable for someone who has not studied functions.
- The three language versions preserve the same meaning and learning objective.
- Links and relative paths work.

Validation

- Run the example with at least two test cases.
- Review every changed file.
- Report what was tested and disclose anything that could not be verified.
- Submit the work through a focused branch and pull request.
```

A detailed prompt improves direction. It does not guarantee correctness.

## Review AI-generated work

Review the result as if it came from a capable but fallible collaborator.

### Documentation review

Confirm that:

- the explanation is technically correct;
- important claims are supported by appropriate sources;
- the text matches the intended learning level;
- examples are original;
- the three languages remain conceptually aligned;
- links work;
- uncertainty is disclosed instead of hidden.

### Code review

Confirm that:

- the code runs as described;
- expected and edge cases were considered;
- names are clear;
- the example does not introduce unnecessary concepts;
- comments explain reasons rather than obvious operations;
- dependencies are justified;
- no secrets or private data are present.

### Repository review

Confirm that:

- only relevant files changed;
- the branch was created from the current `main`;
- the pull request has one clear purpose;
- automated review comments were considered;
- conversations were resolved only after the underlying issue was addressed.

## Privacy and confidential information

Never give an AI system information that you are not authorized to share with another person or external service.

Remove or avoid:

- real names when they are unnecessary;
- email addresses and telephone numbers;
- passwords, API keys, tokens, cookies, and credentials;
- financial, medical, employment, or customer data;
- private URLs, hostnames, paths, and infrastructure details;
- internal documents and private or proprietary source code;
- confidential business rules and workflows;
- identifying details from personal, family, employer, or client projects.

Superficial anonymization may not be enough. A combination of dates, roles, system names, account structures, unusual rules, and workflow details can still reveal the original source.

For educational material, create a new fictional scenario from the ground up.

## Data controls and model improvement

Plan choice, data controls, and model improvement are separate topics.

OpenAI provides Data Controls that allow users to choose whether eligible ChatGPT conversations help improve its models. Available settings and policies may vary by product, account type, and time.

Regardless of the selected setting, do not submit confidential or unauthorized information.

Consult the current official documentation before making decisions about privacy or data use.

## Plans, availability, and limits

OpenAI offers free and paid ChatGPT plans. Codex availability, supported interfaces, features, usage limits, and credit options may vary by plan and may change over time.

A paid plan may be useful when its current features and limits match a person's study or development needs. Payment does not replace understanding, verification, testing, or responsible use.

This repository does not publish fixed prices or plan limits. Consult OpenAI's current official documentation before choosing a plan.

## AI-assisted contributions

AI-assisted contributions are welcome when the contributor remains accountable for the result.

The contributor must:

- understand the submitted content;
- review and verify it;
- run relevant examples and tests;
- check every affected language version;
- disclose uncertainty;
- remove private or proprietary material;
- comply with licenses and repository policies.

Do not submit automatically generated content without meaningful human review.

## Independence and trademarks

ChatGPT, Codex, and OpenAI are trademarks of OpenAI.

Python Study Guide is an independent educational project. It is not affiliated with, sponsored by, or endorsed by OpenAI.

References to OpenAI products are descriptive. The project's own identity must remain primary.

## Official resources

Because product capabilities and policies can change, consult the current official pages:

- [ChatGPT capabilities overview](https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview)
- [Prompt engineering best practices for ChatGPT](https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt)
- [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)
- [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq)
- [OpenAI brand guidelines](https://openai.com/brand/)

## Final principle

A useful AI workflow does not end when an answer appears. It ends when the person understands the result, verifies it, improves it, and can take responsibility for it.
