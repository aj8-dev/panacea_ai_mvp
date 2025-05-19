# PanaceaAI MVP

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/streamlit-v1.0-orange.svg)](https://streamlit.io/)

---

## 📖 Overview

**PanaceaAI MVP** is a lightweight prototype that transforms plain-English problem statements into live, interactive optimization environments. Built with Streamlit, PuLP, and a plug-and-play NLP module, it enables users to explore complex challenges without writing a single line of code.

---

## ✨ Features

- **Natural Language Input**  
  Describe your problem in plain English.

- **Automated Parsing**  
  Converts text into model specs (variables, objectives, constraints).

- **Interactive Controls**  
  Sliders to tweak variable bounds and parameters.

- **Optimization Engine**  
  Leverages PuLP for quick linear programming solutions.

- **Live Visualization**  
  Charts and JSON outputs update in real time.

- **Modular Architecture**  
  Easily extendable to new domains and solver engines.

---


## 🚀 Getting Started

### 1. Prerequisites

- Python 3.7 or higher  
- pip

### 2. Installation

```bash
git clone https://github.com/aj8-dev/panacea_ai_mvp.git
cd panacea_ai_mvp
pip install -r requirements.txt
streamlit run app.py
```

### 3. Usage

1. Enter your problem statement in the text area.  
2. Click **Parse & Build Model** to generate model specs.  
3. Use the sliders to adjust parameters.  
4. Click **Solve Optimization** to view results and live charts.

> **Example Input:**  
> “Design a solar microgrid for a village of 500 people under a $10k budget with at least 95% reliability.”

---

## 🗂 Project Structure

```
panacea_ai_mvp/
├── app.py           # Streamlit frontend
├── nlp_parser.py    # Text-to-model parser (placeholder)
├── optim.py         # Optimization logic using PuLP
├── requirements.txt # Python dependencies
├── README.md        # This documentation
└── LICENSE          # MIT License
```

---

## 🔮 Next Steps

- Integrate GPT-4 API for dynamic parsing  
- Add more solver backends (stochastic, nonlinear)  
- Expand to logistics, finance, healthcare domains  
- Build multi-user collaboration features

---

## 📜 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

> **Repo:** https://github.com/aj8-dev/panacea_ai_mvp

---

*Developed by Ayush Jha*
