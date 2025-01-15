import streamlit as st

st.title("Explainable Question Answering (XQA)")

question = st.text_input("Enter your question:")
context = st.text_area("Enter the context:")

if st.button("Get Answer"):
    answer, explanation = get_answer_and_explanation(question, context)
    st.write("Answer:", answer)
    st.write("Explanation:", explanation)