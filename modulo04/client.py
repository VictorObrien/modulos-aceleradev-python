# 1º importa o socket
import socket

# 2º Define o HOST e a PORTA
HOST = '127.0.0.1'
PORT = 65432

if __name__ == "__main__":
    # 3º Criamos o socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 4º Conectamos no Server
        s.connect((HOST, PORT))
        # 5º Envamos a mensagem
        s.sendall(b'Hello world')
        # 6º Aguarda a resposta
        data = s.recv(1024)
    # 7º Após receber a resposta encerra
    print('Recebido: ', repr(data))
