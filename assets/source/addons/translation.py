"""
This addon is used to make OpenAI model names point to one of these models. The names are semi-random picked.
"""

model_map = [
    {"gpt-4-0613": ""},
    {"davinci-002": ""},
    {"gpt-4": ""},
    {"gpt-4o": "mistralai/Mistral-7B-Instruct-v0.2"},
    {"gpt-4-0125-preview": "mistralai/Mixtral-8x7B-Instruct-v0.1"},
    {"gpt-4-turbo-preview": "mistralai/Mixtral-8x22B-Instruct-v0.1"},
    {"gpt-4-1106-preview": "cognitivecomputations/dolphin-2.6-mixtral-8x7b"},
    {"gpt-3.5-turbo-16k": "meta-llama/Meta-Llama-3-8B-Instruct"},
    {"gpt-3.5-turbo-instruct-0914": "meta-llama/Meta-Llama-3-70B-Instruct"},
]

def translate(model: str) -> str:

    """
    Translate model names to the actual model names
    """

    for i in model_map:
        if model in i:
            return i[model]

    return model
