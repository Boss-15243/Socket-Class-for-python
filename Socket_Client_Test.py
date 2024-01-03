import Socket_Class

ip = input("Connecting ip")

c = Socket_Class.Client()
c.connect(ip,21542)
print(c.recv())