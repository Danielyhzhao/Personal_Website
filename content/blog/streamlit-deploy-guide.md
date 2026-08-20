---
title: "Deploying a Streamlit ML app for free"
date: "2025-03-10"
description: "From a trained model to a public URL in under 30 minutes, with a real-time prediction endpoint."
tags: ["Streamlit", "ML", "Deployment"]
---

## The problem

A trained model sitting in a notebook has zero value to a hiring manager. The moment you put it behind a public URL, it becomes a portfolio piece people can actually click.

## The workflow

1. Wrap the model in a small Streamlit app.
2. Push the repo to GitHub with a `requirements.txt`.
3. Connect Streamlit Community Cloud to the repo.
4. Pick the entry file — you get a `*.streamlit.app` URL immediately.

## One tip

Add an LLM API call to turn raw predictions into human-readable explanations. It makes the demo feel like a product, not a script.
