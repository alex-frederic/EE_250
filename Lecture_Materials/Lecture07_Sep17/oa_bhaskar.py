from openai import OpenAI
client = OpenAI(api_key="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")

response = client.responses.create(
    model="gpt-4",
    input=input()
)

print(type(response))

rj = response.model_dump_json(indent=4)

print(rj)

rd = response.model_dump()

print(rd)
print(rd["output"])
print(rd["output"][0]["content"][0]["text"])

print(response.output_text)