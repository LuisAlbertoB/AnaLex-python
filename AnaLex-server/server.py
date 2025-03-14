import asyncio
from main import automata, mostrar_instrucciones

# Función asíncrona para manejar la conexión de un cliente
async def manejar_cliente(reader, writer):
    """
    Maneja la conexión de un cliente, procesa su entrada y responde con el resultado.
    """
    nivel_actual = 1  # Comenzar en el nivel más bajo
    nivel_maximo = 6  # Nivel más alto

    # Obtener la dirección del cliente
    addr = writer.get_extra_info('peername')
    print(f"Conexión establecida con {addr}")

    while nivel_actual <= nivel_maximo:
        # Mostrar instrucciones del nivel actual
        instrucciones = f"Nivel {nivel_actual}: " + mostrar_instrucciones(nivel_actual)
        writer.write(instrucciones.encode())
        await writer.drain()

        # Solicitar la palabra al cliente
        writer.write(b"Ingresa una palabra: ")
        await writer.drain()

        # Leer la palabra enviada por el cliente
        data = await reader.read(100)
        palabra = data.decode().strip()

        # Validar la palabra con el autómata
        if automata(palabra, nivel_actual):
            respuesta = f"¡Correcto! '{palabra}' es válida en el Nivel {nivel_actual}.\n"
            nivel_actual += 1  # Avanzar al siguiente nivel
        else:
            respuesta = f"Incorrecto. '{palabra}' no es válida en el Nivel {nivel_actual}. Intenta de nuevo.\n"

        # Enviar la respuesta al cliente
        writer.write(respuesta.encode())
        await writer.drain()

    # Mensaje de finalización
    writer.write(b"¡Felicidades! Has completado todos los niveles. ¡Eres un campeón/ona de las palabras!\n")
    await writer.drain()

    # Cerrar la conexión
    print(f"Conexión cerrada con {addr}")
    writer.close()
    await writer.wait_closed()

# Función principal para iniciar el servidor
async def main():
    # Configurar el servidor
    server = await asyncio.start_server(manejar_cliente, '127.0.0.1', 8888)

    # Mostrar información del servidor
    addr = server.sockets[0].getsockname()
    print(f"Servidor escuchando en {addr}")

    # Mantener el servidor en ejecución
    async with server:
        await server.serve_forever()

# Punto de entrada del programa
if __name__ == "__main__":
    asyncio.run(main())