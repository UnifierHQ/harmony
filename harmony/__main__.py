from . import sender

class Harmony:
    def __init__(self, bot):
        self.__bot = bot

    async def send(self, channel_id, *args, **kwargs):
        """Send a message to the room associated with the channel."""
