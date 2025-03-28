import socket

localhost = "127.0.0.1"  
puerto = 5000  

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((localhost, puerto))  

print("Conexión establecida...")
print("Para desconectarte del servidor escribe 'DESCONEXION'.")
print("Escribe un mensaje al servidor.")

while True:
    mensaje = input(f"\nMensaje de {localhost}: ")  
    cliente.send(mensaje.encode('utf-8'))  

    if mensaje.strip().upper() == "DESCONEXION":
        print("Servidor cierra la conexión con el cliente.")
        cliente.close()
        break 
    
    respuesta = cliente.recv(1024).decode('utf-8')
    print(f"Respuesta del servidor: {respuesta}")

