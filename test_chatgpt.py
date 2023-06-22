
import openai
openai.api_key = "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"

prompt = "Hello, my name is tommy and I am a software engineer."
model = "text-davinci-003"
response = openai.Completion.create(engine=model, prompt=prompt, max_tokens=50)

generated_text = response.choices[0].text
print(generated_text)
