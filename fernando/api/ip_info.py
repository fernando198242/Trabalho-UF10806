# ============================================================
#  Extração de dados via API – Informação do IP Público
#  Parte 3 – Trabalho Prático (Python)
#  Autor: Fernando Batista
# ============================================================

import requests
from datetime import datetime

# URL da API pública
url = "https://ipinfo.io/json"

print("A obter informações do IP público...")

# Pedido à API
response = requests.get(url)

if response.status_code != 200:
    print("Erro ao aceder à API:", response.status_code)
    exit()

dados = response.json()

# Extração de informação relevante
ip = dados.get("ip", "N/A")
cidade = dados.get("city", "N/A")
regiao = dados.get("region", "N/A")
pais = dados.get("country", "N/A")
org = dados.get("org", "N/A")
localizacao = dados.get("loc", "N/A")

# Criar ficheiro de saída
ficheiro = f"ipinfo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(ficheiro, "w", encoding="utf-8") as f:
    f.write("Relatório de IP Público\n")
    f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
    f.write(f"IP Público: {ip}\n")
    f.write(f"Cidade: {cidade}\n")
    f.write(f"Região: {regiao}\n")
    f.write(f"País: {pais}\n")
    f.write(f"Localização GPS: {localizacao}\n")
    f.write(f"Organização / ISP: {org}\n")

print(f"Relatório guardado em: {ficheiro}")
