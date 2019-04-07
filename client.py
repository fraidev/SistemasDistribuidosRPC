import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("2 + 2 é : %s" % str(proxy.soma(2,2)))
    print("Minha nova senha é: %s" % str(proxy.gera_senha()))
