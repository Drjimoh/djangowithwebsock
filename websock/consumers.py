from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        packet_too_long = json.dumps({'message': 'packet too large'})
        packet_empty = json.dumps({'message': 'Empty packet received'})
        message_type = type(message)

        if len(message) > 1:
            self.send(text_data=packet_too_long)
        elif len(message) == 0:
            self.send(text_data=packet_empty)
        else:
            self.send(text_data=json.dumps({
            'message': f"packet of type {message_type} received: {message}"
        }))