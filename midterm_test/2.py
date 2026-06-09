import socket

# A
name = socket.getfqdn('220.69.189.125')
print(name)

# B
frot = socket.getservbyport(443)
print(frot)

# C
print(f"{frot}://{name}")

# D
packed = socket.inet_aton('220.69.189.125')
print(packed)