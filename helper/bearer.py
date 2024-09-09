def validate_bearer(bearer):
    if bearer is None:
        raise Exception("Bearer token is required")
    token = bearer.split()[1]
    return token
