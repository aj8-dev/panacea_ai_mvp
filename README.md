#PanaceaAI MVP

  

##Overview

PanaceaAI MVP is a prototype that transforms plain English problem statements into interactive optimization environments. Built with Streamlit, PuLP, and a plug-and-play NLP module, it lets users explore real-time solutions to complex challenges—without writing a single line of code.

##Features

Natural Language Input: Describe problems in plain English.

Automated Parsing: Converts text into model specifications (variables, objectives, constraints).

Interactive Controls: Sliders to adjust variable bounds and parameters.

Optimization Engine: Uses PuLP for quick linear programming solutions.

Live Visualization: Charts and JSON outputs update in real time.

Modular Architecture: Easily extendable for new domains and solver engines.


##Demo



###Getting Started

Prerequisites

Python 3.7 or higher

pip


###Installation

1. Clone the repo

git clone https://github.com/aj8-dev/panacea_ai_mvp.git
cd panacea_ai_mvp


2. Install dependencies

pip install -r requirements.txt


3. Run the app

streamlit run app.py


4. Open in browser Visit http://localhost:8501 to interact with the prototype.



###Usage

1. Enter a real-world problem in the text area.


2. Click Parse & Build Model to generate model specs.


3. Adjust parameters using sliders.


4. Click Solve Optimization to view results and charts.



###Example

"Design a solar microgrid for a village of 500 people under a $10k budget with at least 95% reliability."

##Project Structure

panacea_ai_mvp/
├── app.py           # Streamlit frontend
├── nlp_parser.py    # Text-to-model parser (placeholder)
├── optim.py         # Optimization logic using PuLP
├── requirements.txt # Python dependencies
├── README.md        # Project documentation
└── LICENSE          # MIT License

##Next Steps

Integrate GPT-4 API for dynamic parsing

Add additional solver backends (stochastic, nonlinear)

Expand domains: logistics, finance, healthcare

Build user authentication and collaboration features


##License

This project is licensed under the MIT License. See the LICENSE

> Repo: https://github.com/aj8-dev/panacea_ai_mvp file for details.




---

Prototype by Ayush Jha, Creator of PanaceaAI

