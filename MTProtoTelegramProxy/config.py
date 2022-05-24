import hashlib


PORT = 8585

# name -> secret (32 hex chars)
USERS = {
    "public": hashlib.md5(b'Public').hexdigest(),
    "family": hashlib.md5(b'family').hexdigest(),
    "friends": hashlib.md5(b'friends').hexdigest(),
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": True,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
TLS_DOMAIN = "mamad.dev"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "59666f315c64c825b6c017f4f170afca"