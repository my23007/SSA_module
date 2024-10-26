# Initialize and run the controller in a separate thread
controller = Controller()
controller_thread = threading.Thread(target=controller.start)
controller_thread.daemon = True
controller_thread.start()

# Initialize the client and send some messages
client = Client()

# Send a series of test messages from the client to the controller
messages = ["Hello Controller", "Request Data", "Status Update", "Shutdown Signal"]
for msg in messages:
    client.send_message(msg)
    time.sleep(1)  # Simulate a delay between messages

# Close the client connection
client.close()
