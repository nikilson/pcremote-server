import socket
import time
import controller

listensocket = socket.socket()
Port = 8005
maxConnections = 999
IP = socket.gethostbyname_ex(socket.gethostname())[-1][-1]
listensocket.bind(('', Port))

control = controller.PcController()

print("Server started at " + IP + " on port " + str(Port))



while True:
    listensocket.listen(maxConnections) 
    (clientsocket, address) = listensocket.accept()
    # print(clientsocket.gettimeout())
    clientsocket.settimeout(180)
    print("New connection made!!")
    return_msg = "None"
    message = "None"
    running = True
    while running:
        try:
            message = clientsocket.recv(1024).decode()
            print(f"client : {message}")
            control.call(message)
            # print(return_msg)
            if (message=="pwd") or (message=="ls"):
                return_msg = control.getReturnValue()
                clientsocket.send(bytes(return_msg + "\n", "utf-8"))
            if not (message == ""):
                # time.sleep(1)
                pass
            else:
                clientsocket.close()
                running = False
                continue
        except:
            running = False
            continue
