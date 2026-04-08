# daemon-coin-mathematicians

Monte Carlo simulation for the “daemon coin” probability game  
Inspired by: https://youtu.be/oAj4xPXKzwg

---

## Overview

This project simulates a coordination problem where two players must independently select unknown coin flips in a way that maximizes their probability of survival.

The simulation evaluates strategies based on detecting the **first occurrence of a pattern** in a binary sequence.

---

## Problem Statement

An Evil Spirit captures two mathematicians and isolates them in separate rooms.

He flips a fair coin infinitely many times:

- Player A (Dmitry) sees results of **even-indexed** flips
- Player B (Alexey) sees results of **odd-indexed** flips

Each player must then choose an index of a flip they **do not know**:

- Dmitry selects an **odd** index
- Alexey selects an **even** index

### Outcome

- If both chosen flips have the **same value** → they survive  
- Otherwise → they lose

Before separation, they can agree on a deterministic strategy.

---

## Simulation Model

The infinite process is approximated using finite random sequences.

For each trial:

1. Two independent binary sequences are generated
2. Each player searches for the **first occurrence** of a predefined pattern
3. Each player uses the position found in their own sequence
4. That position is applied to the *other player's sequence*
5. If the resulting bits match → success

---

## Strategy

Each player applies:

- pattern search using **regular expressions**
- selection of the **first match index**

Example:

```python
m1_pattern = r"0"
m2_pattern = r"0"
