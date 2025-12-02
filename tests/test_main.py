from python_dev_template.greetings import hello


def test_hello() -> None:
    assert hello("world") == "Hello, world!"
