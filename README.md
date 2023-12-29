# DeepInfra-Wrapper

DeepInfra-Wrapper is a Python Flask project designed to provide a convenient and free interface for utilizing the DeepInfra API through reverse-engineering. It serves as a local and global server host, allowing users to interact with the DeepInfra chat completion models using Python requests.

## Features

- **Local and Global Server**: Choose between a local server or utilize a global server with Cloudflare integration for enhanced performance.

- **Chat Completion**: Easily generate chat completions by sending messages to the DeepInfra API.

- **Model Selection**: Access a variety of models for different use cases.

- **Streaming Support**: Enable real-time streaming for dynamic chat interactions.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask
- Flask-CORS
- Flask-Cloudflared
- Requests
- Fake User Agent

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/DeepInfra-Wrapper.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python app.py
   ```

## Configuration

Adjust the configuration settings in the `assets/config.json` file to customize your DeepInfra-Wrapper experience.

```json
{
    "use_global": true
}
```

## Usage

### Chat Completion

Send a POST request to `/chat/completions` with the following JSON payload (messages must be in OpenAI format):

```json
{
    "messages": [{"role": "user", "content": "Hello, World!"}],
    "model": "meta-llama/Llama-2-70b-chat-hf (keyword: gpt)",
    "max_tokens": 150,
    "top_p": 1,
    "stream": true
}
```

### Get Models

Retrieve the available models by sending a GET request to `/models`.

Notice: The model names will end with a `` (keyword: gpt)`` this is because some sites don't recognize the models if the keyword isn't included. Simply remove it in your code

### Check API Status

Verify the API status by accessing the root route `/`.

## Error Handling

The API gracefully handles errors, such as forbidden requests, providing meaningful error messages.

## Google Colab

The server is also usable on [This Google Colab Link](https://colab.research.google.com/drive/15sQ6sjZJYUincL3otypxfH96aCfLQ7HZ?usp=sharing)

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the DeepInfra team for providing the chat completion models.

## Contact

For issues and inquiries, please open an [issue](https://github.com/Recentaly/DeepInfra-Wrapper/issues).
