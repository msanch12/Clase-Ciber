import socket

ip_objetivo = '127.0.0.1'
puerto_inicio = 1
puerto_fin = 200

print(f'Escaneando {ip_objetivo} de puerto {puerto_inicio} a {puerto_fin}...')
print('-' * 50)


for puerto in range(puerto_inicio, puerto_fin + 1):
    try:
        socket_conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        resultado = socket_conexion.connect_ex((ip_objetivo, puerto))
        
        if resultado == 0:
            
            print(f'Puerto {puerto}: ABIERTO')
            
            # Intentamos obtener el banner
            try:
                
                socket_conexion.settimeout(2) # Timeout de 2 segundos
                
                banner = socket_conexion.recv(1024)
                
                banner_texto = banner.decode('utf-8', errors='ignore')
                
                print(f' Banner: {banner_texto.strip()}')
            
            except:
                
                print(f' Banner: No disponible')
        
        socket_conexion.close()
    
    except:
        pass
        
print('-' * 50)
print('Escaneo completado')

