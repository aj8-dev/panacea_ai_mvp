import streamlit as st
from nlp_parser import parse_problem
from optim import solve_optimization
import matplotlib.pyplot as plt

st.set_page_config(page_title="PanaceaAI MVP", layout="wide")

st.title("PanaceaAI Prototype")
st.write("Describe a real-world problem. We’ll turn it into an interactive solution space.")

description = st.text_area(
    "Problem Description",
    height=150,
    placeholder="e.g., Optimize solar panel setup for a village with $10k budget and 95% uptime."
)

if st.button("Parse & Build Model"):
    with st.spinner("Parsing problem and building model..."):
        model_specs = parse_problem(description)
        st.success("Model built!")
        st.subheader("Parsed Specifications")
        st.json(model_specs)

        st.subheader("Adjust Parameters")
        params = {}
        for var, bounds in model_specs['variables'].items():
            params[var] = st.slider(var, bounds[0], bounds[1], (bounds[2], bounds[3]))

        if st.button("Solve Optimization"):
            with st.spinner("Solving..."):
                solution = solve_optimization(model_specs, params)
                st.subheader("Solution Results")
                st.json(solution)

                fig, ax = plt.subplots()
                ax.bar(solution.keys(), solution.values())
                ax.set_ylabel('Value')
                ax.set_title('Optimization Outputs')
                st.pyplot(fig)
