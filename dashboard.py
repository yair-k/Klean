import os
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import ast
import git
from git import Repo
from git.exc import InvalidGitRepositoryError, GitCommandError
import json
import logging
import re
import math
from collections import Counter
from memory_profiler import memory_usage, profile
from codecarbon import EmissionsTracker
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import time

model_name = "microsoft/codebert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
code_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

logging.basicConfig(filename='sustainability_dashboard.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def track_emissions(func):
    def wrapper(*args, **kwargs):
        tracker = EmissionsTracker()
        tracker.start()
        result = func(*args, **kwargs)
        emissions = tracker.stop()
        return result, emissions
    return wrapper

def function_tracker(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_usage_before = memory_usage()[0]
        result, emissions = track_emissions(func)(*args, **kwargs)
        mem_usage_after = memory_usage()[0]
        duration = time.time() - start_time
        mem_diff = mem_usage_after - mem_usage_before

        logging.info(f"Function {func.__name__}: Duration: {duration}s, Memory Usage: {mem_diff} MiB, Emissions: {emissions} CO2eq")
        return result
    return wrapper

@function_tracker
def your_function():
    for i in range(1000000):
        pass

def main():
    st.set_page_config(page_title="Project Klean", layout="wide", initial_sidebar_state="collapsed")
    apply_custom_styles()
    st.title("🌿 Project Klean Dashboard 🌿")

    st.markdown("### Input Section")
    with st.container():
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            user_code = st.text_area("Enter your Python code here:", height=150, value=st.session_state.get('user_code', ''))
        with col2:
            description = st.text_area("Enter a description for code generation:", height=150)

    st.markdown("### Actions")
    with st.container():
        col1, col2, col3 = st.columns(3, gap="medium")
        with col1:
            if st.button("Analyze Code"):
                if user_code.strip():
                    st.session_state.user_code = user_code
                    analyze_code(user_code)
                else:
                    st.error("Please enter some code to analyze.")
        with col2:
            if st.button("Generate Code"):
                if description:
                    generated_code = generate_sustainable_code(description)
                    st.session_state.generated_code = generated_code
                    st.code(generated_code, language='python')
                    analyze_code(generated_code)
                else:
                    st.error("Please enter a description for code generation.")
        with col3:
            if st.button("Refactor Code"):
                if 'user_code' in st.session_state:
                    refactor_code(st.session_state.user_code)
                else:
                    st.error("Please analyze code before refactoring.")

    st.markdown("---")  

    st.markdown("### Dashboard Metrics")
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        display_primary_metrics()
        display_performance_metrics()

    with col2:
        display_code_analysis()
        display_environmental_impact()

    with col3:
        display_optimization_suggestions()
        display_sustainability_metrics()

    display_benchmarking_and_goals()
    display_expanded_metrics()

    st.markdown("---")  
    st.markdown("### Git Integration")
    repo_url = st.text_input("Repository URL:", "https://github.com/yair-k")
    repo_path = os.path.join(os.getcwd(), repo_url.split('/')[-1].replace('.git', ''))

    if st.button("Analyze Last Commit"):
        if repo_url:
            clone_or_open_repo(repo_url, repo_path)
            analyze_last_commit(repo_path)
        else:
            st.error("Please enter a repository URL.")

    if st.button("Download Logs"):
        download_logs()

def analyze_code(code):
    try:
        tree = ast.parse(code)
        st.session_state.time_complexity = calculate_time_complexity(tree)
        st.session_state.space_complexity = calculate_space_complexity(tree)
        st.session_state.code_quality = calculate_code_quality(tree)
        st.session_state.scalability_score = calculate_scalability(tree)
        st.session_state.maintainability_index = calculate_maintainability_index(tree)
        st.session_state.test_coverage = calculate_test_coverage(code)

        energy_consumption, carbon_footprint, sustainability_score, energy_by_operation = analyze_energy_and_carbon_footprint(tree)

        st.session_state.energy_consumption = energy_consumption
        st.session_state.carbon_footprint = carbon_footprint
        st.session_state.sustainability_score = sustainability_score
        st.session_state.energy_by_operation = energy_by_operation

        st.success("Code analysis completed successfully.")
    except Exception as e:
        st.error(f"Error analyzing code: {str(e)}")
        logging.error(f"Error analyzing code: {str(e)}")

def generate_sustainable_code(description):
    prompt = f"Generate sustainable and efficient Python code based on the following description:\n\n{description}\n\nPython code:"
    generated_code = code_generator(prompt, max_length=1000, num_return_sequences=1)[0]['generated_text']
    return generated_code.strip()

def refactor_code(code):
    st.subheader("Refactored Code for Improved Sustainability")
    prompt = f"Refactor the following Python code to improve its sustainability and efficiency:\n\n{code}\n\nRefactored code:"
    refactored_code = code_generator(prompt, max_length=2000, num_return_sequences=1)[0]['generated_text']
    st.code(refactored_code, language='python')
    analyze_code(refactored_code)

def get_optimization_suggestions(code):
    prompt = f"Provide optimization suggestions to improve the sustainability and efficiency of the following Python code:\n\n{code}\n\nOptimization suggestions:"
    suggestions = code_generator(prompt, max_length=1000, num_return_sequences=1)[0]['generated_text']
    return suggestions.split('\n') if suggestions else ["No suggestions available"]

def calculate_time_complexity(tree):
    return "O(n)"

def calculate_space_complexity(tree):
    return "O(1)"

def calculate_code_quality(tree):
    return "High"

def calculate_scalability(tree):
    return "Good"

def calculate_maintainability_index(tree):
    return 85

def calculate_test_coverage(code):
    return 75

def analyze_energy_and_carbon_footprint(tree):
    return 100, 50, 90, {"operation1": 30, "operation2": 70}

def clone_or_open_repo(repo_url, repo_path):
    try:
        if os.path.exists(repo_path):
            repo = Repo(repo_path)
            repo.remotes.origin.pull()
        else:
            Repo.clone_from(repo_url, repo_path)
    except (InvalidGitRepositoryError, GitCommandError) as e:
        st.error(f"Error with repository: {str(e)}")
        logging.error(f"Error with repository: {str(e)}")

def analyze_last_commit(repo_path):
    try:
        repo = Repo(repo_path)
        last_commit = repo.head.commit
        st.subheader("Last Commit Analysis")
        st.write(f"Commit Hash: {last_commit.hexsha}")
        st.write(f"Author: {last_commit.author.name}")
        st.write(f"Date: {last_commit.committed_datetime}")
        st.write(f"Message: {last_commit.message}")
    except Exception as e:
        st.error(f"Error analyzing last commit: {str(e)}")
        logging.error(f"Error analyzing last commit: {str(e)}")

def download_logs():
    with open("sustainability_dashboard.log", "rb") as file:
        btn = st.download_button(
            label="Download Log File",
            data=file,
            file_name="sustainability_dashboard.log",
            mime="text/plain"
        )

def display_primary_metrics():
    st.markdown("<div class='metrics-box'>🌟 **Primary Metrics**</div>", unsafe_allow_html=True)
    st.write("Display primary metrics here.")

def display_code_analysis():
    st.markdown("<div class='metrics-box'>🧩 **Code Analysis**</div>", unsafe_allow_html=True)
    st.write("Display code analysis results here.")

def display_performance_metrics():
    st.markdown("<div class='metrics-box'>🚀 **Performance Metrics**</div>", unsafe_allow_html=True)
    st.write("Display performance metrics here.")

def display_environmental_impact():
    st.markdown("<div class='metrics-box'>🌍 **Environmental Impact**</div>", unsafe_allow_html=True)
    st.write("Display environmental impact metrics here.")

def display_optimization_suggestions():
    st.markdown("<div class='metrics-box'>💡 **Optimization Suggestions**</div>", unsafe_allow_html=True)
    st.write("Display optimization suggestions here.")

def display_sustainability_metrics():
    st.markdown("<div class='metrics-box'>♻️ **Sustainability Metrics**</div>", unsafe_allow_html=True)
    st.write("Display sustainability metrics here.")

def display_benchmarking_and_goals():
    st.markdown("<div class='metrics-box'>🎯 **Benchmarking and Goals**</div>", unsafe_allow_html=True)
    st.write("Display benchmarking and goals here.")

def display_expanded_metrics():
    st.markdown("<div class='metrics-box'>📊 **Expanded Metrics**</div>", unsafe_allow_html=True)
    st.write("Display expanded metrics here.")

def apply_custom_styles():
    st.markdown("""
        <style>
            .reportview-container {
                background: black;
                color: #e0e0e0;
            }
            .stTextInput>div>div>input, .stTextArea>div>div>textarea {
                background-color: #111;
                color: #e0e0e0;
                border: 1px solid #444;
                border-radius: 4px;
                transition: all 0.3s ease;
            }
            .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
                border-color: #34c759;
                box-shadow: 0 0 5px #34c759;
            }
            .stButton>button {
                background-color: #1e6f5c;
                color: #e0e0e0;
                border-radius: 4px;
                height: 3em;
                width: 100%;
                margin-top: 10px;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }
            .stButton>button:hover {
                background-color: #155c48;
                transform: scale(1.02);
            }
            .metrics-box {
                background-color: rgba(0, 128, 0, 0.1);
                border: 1px solid #444;
                border-radius: 5px;
                padding: 15px;
                margin-bottom: 15px;
                transition: background-color 0.3s ease, border-color 0.3s ease;
            }
            .metrics-box:hover {
                background-color: rgba(0, 128, 0, 0.2);
                border-color: #34c759;
            }
            .stAlert, .css-2trqyj {
                background-color: rgba(255, 255, 255, 0.1);
                border: none;
            }
            .css-1d391kg, .css-145kmo2 {
                padding: 0px;
            }
            .css-12oz5g7 {
                display: none;
            }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
message.txt
13 KB