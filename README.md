# SHA-256 vs. Poseidon (ZK-Friendly) Hash Benchmark & Analysis

This repository contains a Python benchmark and mathematical analysis comparing traditional bit-oriented cryptographic hash functions (**SHA-256**) with algebraic ZK-friendly hash functions (**Poseidon**).

## 📌 Mathematical Motivation
* **SHA-256**: Operates on 32-bit words using bitwise XOR, AND, and bit rotation. While extremely fast on CPU/hardware, it generates **~25,000 arithmetic constraints** per hash inside ZK-SNARK circuits (e.g., R1CS/PlonK).
* **Poseidon**: Operates directly over Finite Fields $GF(p)$ using algebraic S-boxes ($x^5 \pmod p$). It reduces ZK-SNARK circuit constraints down to **~200–300 constraints**, making proof generation up to 100x faster.

## 🚀 How to Run
```bash
python main.py