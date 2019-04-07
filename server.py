from xmlrpc.server import SimpleXMLRPCServer
import random
import string

def soma(a, b):
    print("Requisição recebida com o seguinte argumento: " + str(a) + "e " + str(b))
    return a + b

def gera_senha():
    print("Requisição recebida para nova senha")
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(soma, "soma")
server.register_function(gera_senha, "gera_senha")
server.serve_forever()