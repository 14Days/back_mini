import jwt

key = 'secret'


def create_token(name: str, password: str) -> str:
    payload = {
        'name': name,
        'password': password
    }

    return jwt.encode(payload, key, 'HS256')


def parse_token(token: str) -> dict:
    return jwt.decode(token, key, 'HS256')
