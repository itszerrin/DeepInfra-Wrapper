# ---------------------------------------- IMPORTS ---------------------------------------- #

# this module allows us to get the headers from the get_headers function
from .headers.get_headers import get_headers

# this module allows us to get a random user agent
from fake_useragent import UserAgent

# this module allows us to generate random numbers
import secrets

# to make requests
import requests

# type hints
from typing import Generator, Any, Dict, List

# ---------------------------------------- FUNCTIONS ---------------------------------------- #
def non_streamed_format(model: str, content: str) -> Dict[str, Any]:

    return {
        "object": "chat.completion",
        "model": f"{model}",
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": f"{content}",
            },
            "finish_reason": "stop",
        }],
    }
# ---------------------------------------- API CLASS ---------------------------------------- #

class Api(object):

    # initialize the class and set some variables here
    def __init__(self) -> None:

        """initialize the class"""
        
        self.url: str = "https://api.deepinfra.com/v1/openai/chat/completions"

        self.headers = get_headers(UserAgent().random, secrets.randbelow(500)) # get random headers

        self.session = requests.Session() # create a session

        # codec for encoding and decoding
        self.codec = 'utf-8'

    def get_models(self) -> Dict[str, List[Dict[str, str]]]:

        """get all models"""

        return {'data': [
            {"id": "meta-llama/Meta-Llama-3-70B-Instruct", "context": 8192},
            {"id": "meta-llama/Meta-Llama-3-8B-Instruct", "context": 8192},
            {"id": "jondurbin/airoboros-l2-70b-gpt4-1.4.1", "context": 4096},
            {"id": "mistralai/Mistral-7B-Instruct-v0.3", "context": 32768},
            {"id": "mistralai/Mixtral-8x7B-Instruct-v0.1", "context": 32768},
            {"id": "mistralai/Mixtral-8x22B-Instruct-v0.1", "context": 65536},
            {"id": "cognitivecomputations/dolphin-2.6-mixtral-8x7b", "context": 32768},
            {"id": "cognitivecomputations/dolphin-2.9.1-llama-3-70b", "context": 8192},
            {"id": "lizpreciatior/lzlv_70b_fp16_hf", "context": 4096},
            {"id": "microsoft/Phi-3-medium-4k-instruct", "context": 4096},
            {"id": "microsoft/WizardLM-2-8x22B", "context": 65536},
            {"id": "Sao10K/L3-70B-Euryale-v2.1", "context": 8192},
            {"id": "google/gemma-2-9b-it", "context": 4096},
            {"id": "google/gemma-2-27b-it", "context": 4096}
        ]}
    

    def chat(
            self,
            messages: List[Dict[str, str]], 
            model: str, 
            stream: bool = True, 
            temperature: int = 0.7, 
            max_tokens: int = 150, 
            top_p: float = 1.0, 
            top_k: int = 50,
            presence_penalty: float = 0.0,
            frequency_penalty: float = 0.0
        ) -> Generator[str, Any, Any] | Dict[str, Any]:

        """
        Chat with the DeepInfra models.

        :param messages: list of messages
        :param model: model name

        :param stream: stream the response
        :param temperature: temperature
        :param max_tokens: max tokens

        :param top_p: top p
        :param top_k: top k
        
        :param presence_penalty: presence penalty
        :param frequency_penalty: frequency penalty
        
        :return: generator or dict
        """

        # compile the data
        data = {
            'messages': messages,
            'model': model,
            'stream': stream,

            'temperature': temperature,
            'max_tokens': max_tokens,

            'top_p': top_p,
            'top_k': top_k,

            'presence_penalty': presence_penalty,
            'frequency_penalty': frequency_penalty,
        }

        # make a post request to the api
        response = self.session.post(self.url, headers=self.headers, json=data, stream=stream)

        # raise for status
        response.raise_for_status()

        # if stream is False
        if not stream:
            return non_streamed_format(model, response.json()['choices'][0]['message']['content'])

        return response.iter_lines()

# Path: assets/source/api.py
