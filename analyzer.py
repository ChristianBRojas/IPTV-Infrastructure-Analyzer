import requests
import json

def analizar_servidor(url_o_ip):
    print(f"[+] Iniciando análisis OSINT para: {url_o_ip}")
    
    # Consulta a API pública de ciberseguridad para Geolocalización e Infraestructura
    api_url = f"https://ipapi.co{url_o_ip}/json/"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        print("\n=== RESULTADOS DE INTELIGENCIA DE AMENAZAS ===")
        print(f"País de origen: {data.get('country_name')}")
        print(f"Ciudad: {data.get('city')}")
        print(f"Proveedor de Hosting (ISP): {data.get('org')}")
        print(f"ASN (Red de Datacenter): {data.get('asn')}")
        
    except Exception as e:
        print(f"[-] Error al consultar la infraestructura: {e}")

if __name__ == "__main__":
    # Puedes cambiar esta IP por el dominio o IP del servidor que quieras auditar
    objetivo = "8.8.8.8" 
    analizar_servidor(objetivo)
