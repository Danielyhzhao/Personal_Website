---
title: "DCGAN vs DDPM on MNIST: what I learned"
date: "2025-04-23"
description: "Comparing two generative models end to end — training stability, image quality, and the trade-offs."
tags: ["Generative AI", "PyTorch", "Diffusion"]
---

## Why compare them

GANs and diffusion models are the two dominant approaches to image generation, but they fail in very different ways. I trained a conditional DCGAN and a conditional DDPM on MNIST to see the trade-offs firsthand.

## The setup

- **Dataset**: MNIST (28x28 grayscale digits)
- **Models**: conditional DCGAN vs conditional DDPM
- **Framework**: PyTorch

```python
# DCGAN generator (simplified)
class Generator(nn.Module):
    def __init__(self, latent_dim, label_dim):
        super().__init__()
        # embedding + transposed conv stack
```

## What I found

- **DCGAN** trains fast but is prone to mode collapse and instability.
- **DDPM** produces more diverse, stable samples but samples much more slowly.
- The final deliverable was an interactive Flask app that generates digits with the pre-trained models.

## Key takeaway

Diffusion models trade speed for stability and fidelity. For MNIST-scale tasks, both work — the choice depends on whether you prioritize speed or quality.
