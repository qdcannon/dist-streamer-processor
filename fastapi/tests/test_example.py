from fastapi.example import hello

def test_hello():
    assert hello() == "Hello, world!"
