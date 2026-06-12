# Prompt Engineering Guide

This guide covers principles, templates, and evaluation methods for crafting effective prompts across models.

1) Principles
- Be explicit about format, length, and role.  Example: "You are an expert product manager. Produce a 5-bullet feature brief." 
- Provide examples (few-shot) when tasks require specific structure.
- Use step-by-step decomposition for complex reasoning tasks.

2) Prompt Templates
- Summarization:
  "Summarize the text below in 3 short bullet points focusing on outcomes and decisions.\n\nText:\n{input}"

- Classification (with output schema):
  "Classify the following customer feedback into one of: [Feature Request, Bug Report, Praise, Other]. Output JSON: {\"label\":..., \"reason\":...}\n\nFeedback:\n{input}"

3) Evaluation Rubric
- Correctness (0-3)
- Completeness (0-3)
- Conciseness (0-2)
- Tone/Style match (0-2)

Use automated checks where possible: JSON schema validation, token length, and simulated user tests.
