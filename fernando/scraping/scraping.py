# ============================================================
#  Web Scraping – Recolha de notícias de tecnologia
#  Parte 2 – Trabalho Prático (Python)
#  Autor: Fernando Batista
# ============================================================

import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL da secção de tecnologia do Público
url = "https://www.publico.pt/tecnologia"

print("A aceder à página...")
response = requests.get(url)

# Verificar se o pedido foi bem-sucedido
if response.status_code != 200:
    print("Erro ao aceder à página:", response.status_code)
    exit()

# Processar o HTML
soup = BeautifulSoup(response.text, "html.parser")

# Seletores mais robustos (funcionam mesmo que o site mude classes)
noticias = soup.select("h2 a, h3 a")

dados = []
for n in noticias:
    titulo = n.get_text(strip=True)
    link = n.get("href")
    if link and titulo:
        dados.append((titulo, link))

# Criar nome do ficheiro com timestamp
ficheiro = f"noticias_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Guardar resultados no ficheiro
with open(ficheiro, "w", encoding="utf-8") as f:
    for titulo, link in dados:
        f.write(f"{titulo}\n{link}\n\n")

print(f"Foram guardadas {len(dados)} notícias em {ficheiro}")
