"""
This addon is used to make OpenAI model names point to one of these models. The names are semi-random picked.
"""

map = [
    {"gpt-3.5-turbo-1106": "codellama/CodeLlama-70b-Instruct-hf"},
    {"gpt-3.5-turbo-0125": "codellama/CodeLlama-34b-Instruct-hf"},
    {"gpt-4-0613": "jondurbin/airoboros-l2-70b-gpt4-1.4.1"},
    {"gpt-4": "mistralai/Mistral-7B-Instruct-v0.1"},
    {"gpt-4-0125-preview": "mistralai/Mixtral-8x7B-Instruct-v0.1"},
    {"gpt-4-1106-preview": "cognitivecomputations/dolphin-2.6-mixtral-8x7b"},
    {"gpt-4-0613": "lizpreciatior/lzlv_70b_fp16_hf"},
    {"gpt-3.5-turbo-0613": "deepinfra/airoboros-70b"},

]

def translate(model: str) -> str:

    """
    Translate model names to the actual model names
    """

    for i in map:
        if model in i:
            return i[model]

    return model