# ai_agent.py (Groq version)
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
import streamlit as st
import os

def create_med_ai_agent(model_name="llama3-70b-8192", temperature=0.3):
    """
    🌐 Med AI Agent using Groq API (Free & Fast)
    """

    api_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))
    if not api_key:
        st.error("⚠️ No Groq API key found. Add it in .streamlit/secrets.toml")
        st.stop()

    llm = ChatGroq(
        model=model_name,
        temperature=temperature,
        groq_api_key=api_key
    )

    # ---- Define your prompt chains (same as before) ----
    bill_prompt = ChatPromptTemplate.from_template("""
    You are a certified medical billing auditor.
    Analyze this hospital/pharmacy bill and provide insights:
    {text}
    Include:
    - Total amount (INR)
    - Overcharges detected (if any)
    - Billing accuracy %
    - Recommendations (refund / fair / suspicious)
    """)
    bill_chain = bill_prompt | llm | StrOutputParser()

    medical_prompt = ChatPromptTemplate.from_template("""
    You are a medical AI specializing in clinical report interpretation.
    Task:
    - Extract test names, values, and normal ranges.
    - Identify abnormalities (High glucose, Low HDL, etc.).
    - Diagnose probable conditions.
    - Suggest which specialist to consult.
    Output Format:
    ### Diagnostic Summary
    - Diagnosis
    - Evidence
    - Abnormal Tests
    - Specialist
    - Severity
    Report:
    {text}
    """)
    medical_chain = medical_prompt | llm | StrOutputParser()

    price_prompt = ChatPromptTemplate.from_template("""
    You are a healthcare cost estimator using Indian data sources (1mg, NPPA).
    Based on this report:
    {text}
    Estimate:
    - Medication + Consultation cost (INR)
    - Total estimated cost
    - Verdict: Fair / Costly / Overpriced
    """)
    price_chain = price_prompt | llm | StrOutputParser()

    advice_prompt = ChatPromptTemplate.from_template("""
    You are a professional AI health coach.
    Based on the findings below:
    {text}
    Give actionable advice (under 100 words):
    - Diet/Lifestyle
    - When to revisit doctor
    - Early warning signs
    """)
    advice_chain = advice_prompt | llm | StrOutputParser()

    full_agent = RunnableParallel(
        bill_analysis=bill_chain,
        medical_summary=medical_chain,
        price_estimation=price_chain,
        health_advice=advice_chain
    )
    full_pipeline = RunnableSequence(
        medical_chain,
        price_chain,
        advice_chain
    )

    return {
        "bill_agent": bill_chain,
        "medical_agent": medical_chain,
        "price_agent": price_chain,
        "advice_agent": advice_chain,
        "parallel_agent": full_agent,
        "pipeline_agent": full_pipeline,
    }
