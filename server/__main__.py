import socket
import pyqrcode

import uvicorn


ip = socket.gethostbyname(socket.gethostname())
print(pyqrcode.create(f"http://{ip}").terminal(quiet_zone=1, background="white"))
uvicorn.run("server:app", host=ip, port=80)
