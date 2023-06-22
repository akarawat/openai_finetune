#4. เอา id มาจาก https://api.openai.com/v1/files เพื่อทำ fine_tune
import os
import openai
openai.api_key = "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"
openai.FineTune.create(training_file="file-hQYpE9jQHvJm8xiJ5GXsVXFx")
