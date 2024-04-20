"""
All addons should be imported here
"""
from .translation import translate
from .expose import create_cloudflare_tunnel

# here the addons are exported
__all__ = [
    'translate',
    'create_cloudflare_tunnel'
]