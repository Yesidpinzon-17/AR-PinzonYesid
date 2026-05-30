import socket
import sys

def escanear_puertos_seguridad():
    print("=" * 50)
    print("   ESCANER DE PUERTOS DE RED (EXCLUSIVO - YESID)   ")
    print("=" * 50)
    
    host = input("Introduce la IP o dominio a escanear: ")
    
    
    puertos_clave = [22, 23, 80]
    
    print(f"\nIniciando analisis de seguridad en: {host}")
    print("-" * 50)
    
    for puerto in puertos_clave:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        sock.settimeout(2.0)
        
        
        resultado = sock.connect_ex((host, puerto))
        
        
        if resultado == 0:
            if puerto == 22:
                print(f"[+] Puerto {puerto} (SSH): ¡ABIERTO! -> Red segura detectada.")
            elif puerto == 23:
                print(f"[!] Puerto {puerto} (Telnet): ¡ABIERTO! -> ALERTA: Protocolo inseguro.")
            else:
                print(f"[+] Puerto {puerto}: ABIERTO")
        else:
            print(f"[-] Puerto {puerto}: CERRADO o bloqueado por Firewall.")
            
        sock.close()
        
    print("-" * 50)
    print("Analisis de red finalizado con exito.")

if __name__ == "__main__":
    escanear_puertos_seguridad()