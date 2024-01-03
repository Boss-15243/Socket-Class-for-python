import Socket_Class

ip = input("Connecting ip")
port = int(input("Connecting port"))

c = Socket_Class.Client()
c.connect(ip,port)
print(c.recv())