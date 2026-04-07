# Statistical Engineering & Simulation Engine

## Overview
This project implements a statistical engine from scratch using pure Python and demonstrates the Law of Large Numbers via Monte Carlo simulation.

## Features
- Mean, Median, Mode (multimodal)
- Sample & Population Variance
- Standard Deviation
- Outlier Detection
- Monte Carlo Simulation

## Mathematical Logic
- Population Variance: sum((x - μ)^2) / N
- Sample Variance: sum((x - x̄)^2) / (N - 1)
- Median:
  - Odd: middle value
  - Even: average of two middle values

## Setup
```bash
python main.py