from openai import OpenAI

client = OpenAI(command)

response = client.responses.create(
    model = "gpt-5.5",
    input = command
)

print(response.output_text)