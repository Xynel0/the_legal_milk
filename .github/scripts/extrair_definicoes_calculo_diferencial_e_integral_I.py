import glob
import os
from bs4 import BeautifulSoup

# --- Configurações específicas desta disciplina ---
pasta_disciplina = "semestre_1/calculo_diferencial_e_integral_I"
classe_alvo = "definicoes"
pasta_saida = os.path.join(pasta_disciplina, "arquivos_uteis")
arquivo_saida = os.path.join(pasta_saida, f"{classe_alvo}.md")
# ----------------------------------------------------

divs_encontradas = []

for arquivo in glob.glob(os.path.join(pasta_disciplina, "*.md")):
    with open(arquivo, encoding="utf-8") as f:
        conteudo = f.read()

    soup = BeautifulSoup(conteudo, "html.parser")

    for div in soup.find_all("div", class_=classe_alvo, id=True):
        id_attr = div.get("id")
        if id_attr and id_attr.isdigit():
            divs_encontradas.append((int(id_attr), str(div)))

divs_encontradas.sort(key=lambda x: x[0])

os.makedirs(pasta_saida, exist_ok=True)

with open(arquivo_saida, "w", encoding="utf-8") as f:
    for _, html in divs_encontradas:
        f.write(html + "\n\n")

print(f"{len(divs_encontradas)} divs extraídas e salvas em {arquivo_saida}")
