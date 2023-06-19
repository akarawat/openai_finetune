import openai

openai.api_key = "your-api-key"

model_engine = "text-davinci-002"
n_epochs = 3
batch_size = 4
learning_rate = 1e-5
max_tokens = 1024

training_file = "path/to/your/training_data.jsonl"
validation_file = "path/to/your/validation_data.jsonl"