# RAG with AWS Bedrock-Lambda-API Gateway


## Overview
- When pdf file is uploaded it learns its contents and answers from it upon user query using RAG.

## Workflow
- When pdf file is uploaded it parses it and create vector embeddings out of its content and store it in chromadb.
- When user hits the query, its posted on API GATEWAY URL and LAMBDA function is triggered to invoke Bedrock model.
- Based on query similarity search on chromadb happens which pulls relevant documents which are later reranked.
- reranked documents are supplied as context in the payload request to API GATEWAY along with the query.
- Bedrock model uses question and context in supplied prompt to generate answer to the user query.

## demo
<img width="1440" alt="Screenshot 2025-05-13 at 10 59 47 PM" src="https://github.com/user-attachments/assets/3083b412-5f52-4a79-8d23-58ee0ba93fc4" />


## Technologies used
- Amazon Bedrock
- AWS Lambda
- Amazon API Gateway
- Langchain
- RAG
- Streamlit
- Chromadb
