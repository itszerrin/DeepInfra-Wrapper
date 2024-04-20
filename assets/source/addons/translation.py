"""
This addon is used to make OpenAI model names point to one of these models. The names are semi-random picked.
"""

map = [
    {"gpt-3.5-turbo-0125": "codellama/CodeLlama-34b-Instruct-hf"},
    {"gpt-4-0613": "jondurbin/airoboros-l2-70b-gpt4-1.4.1"},
    {"gpt-4": "mistralai/Mistral-7B-Instruct-v0.1"},
    {"gpt-4-0125-preview": "mistralai/Mixtral-8x7B-Instruct-v0.1"},
    {"gpt-4-1106-preview": "cognitivecomputations/dolphin-2.6-mixtral-8x7b"},
    {"gpt-4-0314": "lizpreciatior/lzlv_70b_fp16_hf"},
    {"gpt-3.5-turbo-0613": "deepinfra/airoboros-70b"},
    {"davinci-002": "HuggingFaceH4/zephyr-orpo-141b-A35b-v0.1"},
    {"babbage-002": "microsoft/WizardLM-2-8x22B"},
    {"gpt-4-turbo-preview": "mistralai/Mixtral-8x22B-Instruct-v0.1"},
    {"gpt-3.5-turbo-instruct-0914": "meta-llama/Meta-Llama-3-70B-Instruct"},
    {"gpt-3.5-turbo-16k": "meta-llama/Meta-Llama-3-8B-Instruct"},
]

def translate(model: str) -> str:

    """
    Translate model names to the actual model names
    """

    for i in map:
        if model in i:
            return i[model]

    return model
