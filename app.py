# ---------------------------------------- IMPORTS ---------------------------------------- #

# import flask and flask_cors to host the api
from flask import Flask, request, jsonify
from flask_cors import CORS

# import the api class
from assets.source.api import Api, non_streamed_format

# import addon
from assets.source.addons.translation import translate

# logging module for debugging
import logging

# json module to parse json
from json import loads

# ---------------------------------------- CONFIGURE LOCAL SERVER ---------------------------------------- #

# create flask app
app = Flask(__name__)

# enable cors
CORS(app)

# ---------------------------------------- READ FROM CONFIG FILE ---------------------------------------- #
with (open("assets/config.json", "r")) as f:

    config_file = loads(f.read())

    # check if user wants to use a global server too
    if config_file["use_global"]:

        # import neccessary modules
        from flask_cloudflared import run_with_cloudflared

        # run with cloudflared
        run_with_cloudflared(app)

# ---------------------------------------- LOGGING CONFIG ---------------------------------------- #

# set logging level
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

# ---------------------------------------- API ---------------------------------------- #

# create api instance
api = Api()

# ---------------------------------------- ROUTES ---------------------------------------- #

# chat generaiton route
@app.route("/chat/completions", methods=["POST"])
def chat():

    # get request data
    data = request.get_json()

    # get messages
    messages = data["messages"]

    # get model
    model = translate(data["model"]) if config_file["use_addons"] else data["model"]

    # get max tokens
    max_tokens = data.get("max_tokens")

    # top p and top k
    top_p = data.get("top_p")
    top_k = data.get("top_k")

    # temperature, frequency penalty and presence penalty
    temperature = data.get("temperature")

    # frequency penalty
    frequency_penalty = data.get("frequency_penalty")

    # presence penalty
    presence_penalty = data.get("presence_penalty")

    # streaming function. uses text/event-stream instead of application/json
    def stream():

        # generate chat
        for chunk in api.chat(messages, 
                              model, 
                              stream=True, 
                              max_tokens=max_tokens, 
                              top_p=top_p, 
                              temperature=temperature, 
                              frequency_penalty=frequency_penalty, 
                              presence_penalty=presence_penalty,
                                top_k=top_k
        ):

            # yield chat
            #print(chunk)
            yield chunk + b'\n\n'

        # in the end, return done
        yield b'data: [DONE]'

    # check if user wants to stream
    if data["stream"]:

        # log
        logging.info(f"Streaming requested for model {model}\n")

        # return stream
        return app.response_class(stream(), mimetype='text/event-stream')
    
    # even if not, stream but collect all data to a full string
    else:

        # log
        logging.info(f"Non-streaming requested for model {model}\n")

        # pre-init
        full: str = ""

        # generate chat
        for chunk in api.chat(messages, 
                              model, 
                              stream=True, 
                              max_tokens=max_tokens, 
                              top_p=top_p, 
                              temperature=temperature, 
                              frequency_penalty=frequency_penalty, 
                              presence_penalty=presence_penalty,
                                top_k=top_k
        ):

            try:

                # append chunk
                full += loads(chunk.decode("utf-8").removeprefix('data: '))["choices"][0]["delta"]["content"]

            except: pass

        # return full
        return jsonify(non_streamed_format(model, full))


# route to get all models
@app.route("/models", methods=["GET"])
def get_models():

    # return models
    return jsonify(api.get_models())

# root route to check if api is online
@app.route("/", methods=["GET"])
def root():
    
        # return root
        return "<h1>API is online!</h1>"

# ---------------------------------------- ERROR HANDLING ---------------------------------------- #
@app.errorhandler(403)
def forbidden():

    # return 403
    return jsonify(

        {"status": False},
        {'error': [

            {'message': 'Something went wrong, the API was blocked from sending a request to the DeepInfra API. Please try again later.'},
            {'tpye': 'forbidden'},
        ]},
        {'hint': 'please report issues on the github page'}
    ), 403

@app.errorhandler(500)
def internal_server_error():
    
        # return 500
        return jsonify(
    
            {"status": False},
            {'error': [
    
                {'message': 'Something went wrong, the API was unable to complete your request. Please try again later.'},
                {'tpye': 'internal server error'},
            ]},
            {'hint': 'please report issues on the github page'}
        ), 500

# ---------------------------------------- START API ---------------------------------------- #

# start the api
if __name__ == "__main__":

    app.run(debug=False, host="0.0.0.0", port=5000)

# Path: app.py
