import json
from utils import get_db_handle
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .tasks import add_message
""" 
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("Websockets connect")
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        print("room_group_name: ", self.room_group_name)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print("Websockets receive")
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        print("Websockets chat_message")
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message})) """


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print("Websockets connect")
        self.accept()

    def disconnect(self, close_code):
        print("Websockets disconnect")
        pass

    def receive(self, text_data):
        print("Websockets receive")
        # handle, client = get_db_handle(db_name="radiohound",
        #                                host="mongo",
        #                                port=27017,
        #                                username="django",
        #                                password="vogqx496RjrJ")
        text_data_json = json.loads(text_data)
        #print(text_data_json)
        # collection = handle['messages']
        # result = collection.insert_one(text_data_json)
        # print("result: ", result)
        add_message.apply_async(args=[text_data])
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": "received: " + message}))
