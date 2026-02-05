import boto3, json
client = boto3.client("bedrock-runtime", region_name="us-east-1")
prompt = "Review this code for performance and Kubernetes risks"
response = client.invoke_model(
modelId="anthropic.claude-3-sonnet-20240229-v1:0",
body=json.dumps({
"messages": [{"role": "user", "content": prompt}],
"max_tokens": 400
})
)
print(response["body"].read().decode())
