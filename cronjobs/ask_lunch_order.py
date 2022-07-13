from mycroft_bus_client import MessageBusClient, Message

client = MessageBusClient()
client.run_in_thread()

# Invoke as if someone had said "Hey Mycroft... place lunch order"
client.emit(Message("recognizer_loop:utterance", {'utterances': ["timed entry order meal"], 'lang': 'en-us'}))