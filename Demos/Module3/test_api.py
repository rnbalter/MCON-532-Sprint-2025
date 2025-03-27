from src.open_api_client import get_openai_client
from pprint import pprint

client = get_openai_client()
pprint(vars(client)) #prints the content of the client

# Make a request to OpenAI API
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        #{"role": "user", "content": "When was the State of Israel founded?"},
        {"role": "user", "content": "Why did WW2 start?"},
        {"role": "system", "content": "you should respond to the grieving child whose father died fighting in ww2"}


    ]
)

# Output the response
pprint(completion)
pprint(completion.choices[0].message.content)



''''
messages = [{role: gm
system prompts = []
user_input = "Explain xyz
'''