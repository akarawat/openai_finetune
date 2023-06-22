#3. Upload Jsonl
import os
import openai
openai.api_key = "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"
openai.File.create(
  file=open("prepared_data_prepared.jsonl", "rb"),
  purpose='fine-tune'
)
