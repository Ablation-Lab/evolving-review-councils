# Evolving Councils – Accent and Dialect Understanding

A spin-off of the Evolving Council & Optimum Size Experiment. It applies the same evolve-and-test method to how well AI understands accented and dialect speech.

## The problem

Speech recognition and AI assistants tend to work worse for some accents and dialects, such as Welsh English. People in those regions can quietly get worse answers without knowing why.

## The idea

Use an evolving council to improve the step after transcription: correcting and interpreting what the speech model produced. The council can't retrain the speech model itself, but it can evolve better correction and interpretation of its output.

## How it's measured

- **Benchmark:** human-checked transcripts of accented speech.
- **Hard score:** word error rate, plus whether the meaning was understood correctly.
- **Held-out speakers:** some speakers are never shown to the council, so it learns the accent rather than individual voices.
- Same rules as the main experiment: a generation advances only if it beats the score, with fresh sessions and blind judging.

## Why it matters

If it works, it's a cheap way to narrow the gap for under-served accents without retraining large models, and the method could carry over to other dialects.

## Background (verify before citing)

- Koenecke et al., PNAS 2020: racial disparities in automated speech recognition.
- Hofmann et al., Nature 2024: dialect prejudice in language models.

These are from general knowledge and need checking before use in any paper or application.

## Status

Idea stage. Runs only after the main council experiment has produced a working recipe.
