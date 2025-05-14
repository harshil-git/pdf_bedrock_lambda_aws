import streamlit as st
import requests
import boto3
import json
from app.query_handler import query_documents
from app.process_pdfs import process_all_pdfs

#API_URL = "http://<YOUR_EC2_PUBLIC_IP>:8000/query"  # Replace this with your EC2 IP / # with API GATEWAY- stages URL
API_URL = "https://xffqc2rdve.execute-api.us-west-2.amazonaws.com/dev/query"
st.title("📄 PDF Search")


s3 = boto3.client("s3")


uploaded_file = st.file_uploader("Choose a PDF", type="pdf")

if uploaded_file:
    process_all_pdfs(uploaded_file)
    st.success("File uploaded and vectors db created! Ready to query.")



query = st.text_input("Ask a question about the PDFs:")
if st.button("Search") and query:
    with st.spinner("Searching..."):
        try:
            context = query_documents(query)
            information = {"question": query, "context": context}
            
            response = requests.post(API_URL, json=information)
            if response.status_code == 200:
                    ans = response.json()
                    st.subheader("💡 Answer")
                    st.write(ans["answer"])
            else:
                    st.error("API Error: " + response.text)
        except Exception as e:
                st.error(f"Connection failed: {e}")
else:
        st.warning("Please enter a question.")

