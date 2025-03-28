# Cliente y Servidor TCP en Python

Este proyecto implementa un **servidor TCP** y un **cliente TCP** en Python que pueden comunicarse entre sí en la misma máquina (**localhost**) utilizando el puerto `5000`.

## ✨ Requisitos
- Python **3.x** instalado en el sistema.
- Un editor de código o terminal para ejecutar los archivos.

---

## 🔄 Ejecución

### 1. Clonar o descargar el proyecto
Puedes descargar los archivos o clonarlos desde GitHub si ya están en un repositorio.

Si tienes `git` instalado, usa:
```bash
 git clone https://github.com/YairBrito2022/TCP.git
 cd repositorio
```
Si prefieres hacerlo manualmente:
- Descarga los archivos `servidor.py` y `cliente.py`.
- Guárdalos en una misma carpeta en tu equipo.

---

### 2. Iniciar el **Servidor**

1. **Abrir una terminal o CMD**.
2. **Navegar hasta la ubicación del archivo** `servidor.py` con:
   ```bash
   cd ruta/del/proyecto
   ```
   Por ejemplo, si el archivo está en `C:\Users\TuUsuario\TCP_Proyecto`, usa:
   ```bash
   cd C:\Users\TuUsuario\TCP_Proyecto
   ```
3. **Ejecutar el servidor con:**
   ```bash
   python servidor.py
   ```
4. Si todo funciona correctamente, deberías ver un mensaje como este:
   ```bash
  Escuchando en 127.0.0.1:5000
  Conexión establecida con ('127.0.0.1', XXXXX)
   ```

---

### 3. Iniciar el **Cliente**

1. **Abrir otra terminal o CMD**.
2. **Navegar hasta la ubicación del archivo** `cliente.py` con:
   ```bash
   cd ruta/del/proyecto
   ```
3. **Ejecutar el cliente con:**
   ```bash
   python cliente.py
   ```
4. Verás un mensaje indicando que el cliente está conectado y puedes escribir mensajes:
   ```bash
   Conexión establecida...
   Para desconectarte del servidor escribe 'DESCONEXION'.
   Escribe un mensaje al servidor.
   
   Mensaje de 127.0.0.1:
   ```
5. Ahora puedes escribir mensajes en el cliente y recibir respuestas del servidor.

---

## 💪 Pruebas Manuales

### **Prueba 1: Enviar un mensaje normal**
1. En la terminal del **cliente**, escribe:
   ```bash
   hola servidor
   ```
2. El servidor deberá responder con el mensaje en mayúsculas:
   ```bash
   Respuesta del servidor: HOLA SERVIDOR
   ```
3. En la terminal del **servidor**, verás:
   ```bash
   Conexión establecida con ('127.0.0.1', XXXXX)
   Cliente envía: hola servidor
   ```

### **Prueba 2: Desconectar el cliente**
1. En la terminal del **cliente**, escribe:
   ```bash
   DESCONEXION
   ```
2. Verás el mensaje:
   ```bash
   Servidor cierra la conexión con el cliente.
   ```
3. En la terminal del **servidor**, verás:
   ```bash
   Cliente envía: DESCONEXION
   El cliente ('127.0.0.1', 54251) se desconecto.
   ```

---

## 🔧 Solución de Problemas

### ❓ **Error: 'python' no se reconoce como un comando interno o externo**
- Asegúrate de que Python está instalado y agregado a la variable de entorno `PATH`.
- Verifica instalación con:
  ```bash
  python --version
  ```

### ❓ **Error: Address already in use (Dirección en uso)**
- El puerto `5000` ya está ocupado.
- Cierra procesos en ese puerto o cambia el puerto en `servidor.py` y `cliente.py`.

### ❓ **No se establece conexión**
- Revisa que el **servidor esté ejecutándose** antes de iniciar el cliente.
- Usa `127.0.0.1` y el mismo puerto en ambos scripts.






