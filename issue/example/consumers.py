from channels.generic.websockets import WebsocketConsumer


class ExampleConsumer(WebsocketConsumer):

    http_user = True
    strict_ordering = False

    def connection_groups(self, **kwargs):
        return ["example"]

    def connect(self, message, **kwargs):
        self.message.reply_channel.send({'accept': True})

    def receive(self, content, **kwargs):
        self.send(content)

    def disconnect(self, message, **kwargs):
        pass