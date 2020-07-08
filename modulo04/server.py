# 1º importa o socket
import socket

# 2º Define o HOST e a PORTA
HOST = '127.0.0.1'
PORT = 65432

if __name__ == "__main__":
    # 3º Criamos o socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 4º Fazemos o Bind desse Socket
        s.bind((HOST, PORT))
        # 5º Fazemos o Listen desse Porta
        s.listen()
        print(f"Esperando conexão em {HOST}:{PORT}")
        # 6º Esperamos a conexão
        conn, addr = s.accept()
        # 7º Quando eu receber a conexão
        with conn:
            print('Conectado por ', addr)
            # 8º Enquanto estiver recebendo dados, envia uma resposta através de 'sendall'
            while True:
                data = conn.recv(1024)
                # 9º Quando não tem mais dados para receber, dá o break e sai dos Loops
                if not data:
                    break
                conn.sendall(b'Server ' + data)
