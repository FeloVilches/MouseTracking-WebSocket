import websocket

PORT = 9876

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:" + str(PORT) + "/mousetracking",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.run_forever()
