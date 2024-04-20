# DeepInfra-Wrapper Addon - Cloudflare Quick-tunnels.

This addon is needed to globally expose our flask application and create a URL that can be accessed from anywhere.

## Usage

To use, call `create_cloudflare_tunnel` function and pass the port as a paremeter. You will then see Cloudflare emit the created ULR inside the console.
Remember, you need to have `use_addons` set to `true` in the config.json
