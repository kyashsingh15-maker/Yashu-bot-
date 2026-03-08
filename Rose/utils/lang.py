def language(func):
    async def wrapper(client, message, *args, **kwargs):
        _ = lambda x: x  # dummy translate function
        return await func(client, message, _, *args, **kwargs)
    return wrapper

def languageCB(func):
    async def wrapper(client, query, *args, **kwargs):
        _ = lambda x: x  # dummy translate function
        return await func(client, query, _, *args, **kwargs)
    return wrapper