import socket

localhost = "127.0.0.1"  
puerto = 5000  

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((localhost, puerto)) 
servidor.listen(1)  

print(f"Escuchando en {localhost}:{puerto}")

while True:    
    conn, dir = servidor.accept()  
    print(f"Conexión establecida con {dir}")

    while True:
        mensaje = conn.recv(1024).decode('utf-8')  
        if not mensaje:
            break  

        print(f"Cliente envía: {mensaje}")

        if mensaje.strip().upper() == "DESCONEXION":
            print(f"El cliente {dir} se desconecto.")
            conn.close() 
            break 
        
        respuesta = mensaje.upper()
        conn.send(respuesta.encode('utf-8'))

