import Socket_Class

ip = input("Connecting ip")
port = int(input("Connecting port"))

s = Socket_Class.Server(ip, port)
s.listen(1)
s.accept()
print("Connected")
data = "Yes It Works"
s.sendall(data)