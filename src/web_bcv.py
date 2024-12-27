import requests

def obtener_tasa(url):
    response = requests.get(url=url)
    
    if response.status_code == 200:
        return 50.41
    else:
        raise Exception("Pagina del BCV Caida")