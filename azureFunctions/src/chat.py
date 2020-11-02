import sys
import time
import requests
import threading
from azure.storage.queue import QueueClient, BinaryBase64EncodePolicy, BinaryBase64DecodePolicy
import base64

connection_string = "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;"
queue_name = "analyst-queue"

user_name = sys.argv[1]
print("Logging in {}.".format(user_name))
# user_name = 'analyst'
to_user = "technician"

if user_name == "technician":
    queue_name = "technician-queue"
    to_user = "analyst"



def get_messages(connection_string, queue_name):
    while True:
        queue_client = QueueClient.from_connection_string(connection_string, queue_name)
        queue_client.message_encode_policy = BinaryBase64EncodePolicy()
        queue_client.message_decode_policy = BinaryBase64DecodePolicy()  

        messages = queue_client.receive_messages()
        for message in messages:
            print("\nMessage Received: {}".format(base64.b64decode(message.content).decode('utf-8')))
            queue_client.delete_message(message.id, message.pop_receipt)


        properties = queue_client.get_queue_properties()
        if properties.approximate_message_count == 0:
            time.sleep(1)




if __name__ == '__main__':
    receiving_thread = threading.Thread(target=get_messages, args=(connection_string, queue_name))
    receiving_thread.start()
    while True: 
        msg = input("\nType a message: \n")

        if msg == "/stop":
            break            

        if user_name == 'technician':
            d = requests.post("http://localhost:7071/api/MessageAPI", json={'to': 'analyst', 'from': 'technician', 'msg': msg})
        else :
            d = requests.post("http://localhost:7071/api/MessageAPI", json={'to': 'technician', 'from': 'analyst', 'msg': msg})
        
        time.sleep(2)


