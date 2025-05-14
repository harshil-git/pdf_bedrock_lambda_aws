import json
import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-west-2")
inference_profile_arn = "us.meta.llama3-1-8b-instruct-v1:0"

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        question = body["question"]
        context_paragraphs = body.get("context", [])

        context = "\n\n".join(context_paragraphs)
        prompt = f"""
                <s>[INST]<<SYS>>
                You are helpful, respectful and honest assistant. Always answer as helpfully as possible only using the context text provided. Your answers should only answer the question once to the user and not have any other text like <<SYS>>/[INST] tags in the answer and after the answer text is done. 
                Don't behave like a chatbot and ask user again only provide answer like question answering.
                if a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information. 
                <</SYS>>

                CONTEXT:/n/n {context} /n/n
                Question: {question}

                Answer: [/INST]"""

        response = bedrock.invoke_model(
            modelId=inference_profile_arn,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "prompt": prompt,
                "temperature": 0.3,
                "top_p": 0.9,
                "max_gen_len": 512
            })
        )

        model_output = json.loads(response["body"].read())
        return {
            "statusCode": 200,
            "body": json.dumps({
                "answer": model_output["generation"].strip()
            }),
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
