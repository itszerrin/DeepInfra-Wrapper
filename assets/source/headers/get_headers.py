def get_headers(user_agent: str, content_length: int):

    return {
        'Authority': 'api.deepinfra.com',
        'Host': 'api.deepinfra.com',
        'User-Agent': f'{user_agent}',
        'Accept': 'text/event-stream',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://deepinfra.com/',
        'Content-Type': 'application/json',
        'X-Deepinfra-Source': 'web-page',
        'Content-Length': f'{content_length}',
        'Origin': 'https://deepinfra.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'
}

# Path: assets/source/headers/get_headers.py