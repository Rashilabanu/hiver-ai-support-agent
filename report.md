# Evaluation Report

## Problem Framing

The goal is to classify customer-support messages, draft helpful replies, and decide when human escalation is needed.

## What Good Looks Like

A good support agent should identify the customer intent correctly, provide a useful response, and avoid automatically handling uncertain or sensitive cases.

## Baselines

The system is compared with simple rule-based and majority-class baselines.

## Failure Modes

- Unclear customer requests
- Multiple issues in one message
- Missing conversation context
- Unusual wording
- Out-of-scope requests

## What Is Misleading About My Headline Number?

A single accuracy number may look better than real-world performance because the evaluation set is sampled and the labels and data may not represent all customer-support conversations.

## Next With One More Week

I would improve intent classification, retrieve relevant historical brand responses, expand the human-labelled evaluation set, and add stronger reply-quality evaluation.
