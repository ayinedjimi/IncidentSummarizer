"""Setup for IncidentSummarizer
Author: Ayi NEDJIMI
"""
from setuptools import setup, find_packages

setup(
    name="incidentsummarizer",
    version="1.0.0",
    author="Ayi NEDJIMI",
    author_email="contact@ayinedjimi-consultants.fr",
    description="AI-Powered Incident Summarizer",
    url="https://github.com/ayinedjimi/IncidentSummarizer",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=["transformers>=4.35.0", "spacy>=3.7.0", "torch>=2.0.0"],
)
