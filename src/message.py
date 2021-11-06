# Message object
class Message:
    def __init__(self, sender: str, content: str, time: str) -> None:
        self.sender = sender
        self.content = content
        self.time = time
