import Socket_Class

list

s = Socket_Class.Server("127.0.0.0", 21542)
s.listen(1)
s.accept()
print("Connected")
data = "Yes It Works"
s.sendall(data)