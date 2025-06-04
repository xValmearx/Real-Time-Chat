from channels.generic.websocket import WebsocketConsumer

class ChatroomComsumer(WebsocketConsumer):
    def connect(self):
        self.accept()