from openai import OpenAI

client = OpenAI(
  api_key="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"
)

prompt = f"Convert this JavaScript code into Python"
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message);
