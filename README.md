# Hiver AI Customer Support Agent

## Overview

This project builds an AI-based customer support agent using the Customer Support on Twitter dataset.

The system performs three main tasks:

1. Classifies customer messages into support intents.
2. Drafts a suitable support reply.
3. Decides whether the message can be auto-handled or should be escalated to a human.

## Dataset

Primary dataset:
Customer Support on Twitter

The dataset contains real customer-support conversations between customers and brands.

## Pipeline

Customer Message
        ↓
Intent Classification
        ↓
Draft Reply Generation
        ↓
Escalation Decision
        ↓
Auto-Handle / Human Support

## Current Approach

The initial system uses simple rule-based intent classification and predefined response templates as a baseline.

Messages with unclear intents or potentially sensitive issues are escalated to a human.

## Evaluation

The project evaluates:

- Intent classification
- Response quality
- Escalation decisions
- Baseline performance
- Failure cases

## Failure Analysis

Common failure cases include:

- Unclear customer requests
- Messages containing multiple issues
- Missing context
- Unusual wording
- Requests outside the defined intents

## Limitations

The current implementation is evaluated on a sampled subset of the full dataset. The headline metrics may not represent performance on the complete dataset.

## Future Improvements

With additional development time, the system can be improved using:

- LLM-based intent classification
- Retrieval from historical brand responses
- Better escalation policies
- Larger human-labelled evaluation sets
- LLM-as-a-judge evaluation

## Project Structure

```text
hiver-ai-support-agent/
│
├── README.md
├── app.py
└── evaluation/
