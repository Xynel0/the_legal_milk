import glob
import os
from bs4 import BeautifulSoup

# ------------------- Configurações específicas desta disciplina -------------------
pasta_disciplina = "semestre_1/calculo_diferencial_e_integral_I"
pasta_saida = os.path.join(pasta_disciplina, "arquivos_uteis")
arquivo_saida = os.path.join(pasta_saida, "resumo.md")

# Lista de classes a buscar, na ORDEM em que devem aparecer no arquivo final.
# Cada item é uma tupla (nome_da_classe, aplicar_nome).
# aplicar_nome=True só faz sentido pra classes que tenham um h3 com id igual ao que se quer exibir
# Dentro do strong interno ao h3. (pode ser usado com strong vazio no arquivo original, exibindo 
# corretamente o id apenas no arquivo de saída.
CLASSES = [
    ("definicoes", True),
    ("proposicoes", False),
    ("provas", True),
]
# -----------------------------------------------------------------------------------


def coletar_divs(soup, classe_alvo, aplicar_nome):
    """
    Recebe um soup já parseado e o nome de uma classe.
    Devolve uma lista de tuplas (id, html) com todas as divs
    dessa classe encontradas nesse soup, sem ordenar ainda.
    """
    encontradas = []

    divs_da_classe = soup.find_all("div", class_=classe_alvo, id=True)

    for div in divs_da_classe:
        id_attr = div.get("id")

        # Só aceita divs cujo id seja um número (necessário pra poder ordenar depois)
        if id_attr is None:
            continue
        if not id_attr.isdigit():
            continue

        if aplicar_nome:
            h3 = div.find("h3")
            if h3 is not None:
                id_do_h3 = h3.get("id")
                if id_do_h3 is not None:
                    nome = id_do_h3.replace("_", " ")
                    nome = nome.title()

                    strong = h3.find("strong")
                    if strong is not None:
                        strong.string = nome
                    else:
                        h3.string = nome

        id_convertido = int(id_attr)
        html_da_div = str(div)
        encontradas.append((id_convertido, html_da_div))

    return encontradas


# Dicionário que vai guardar uma lista de divs para cada classe declarada em CLASSES.
# Criado de forma explícita, sem dict comprehension.
resultados = {}
for classe, aplicar_nome in CLASSES:
    resultados[classe] = []


# Varre todos os arquivos .md direto dentro da pasta da disciplina
caminho_busca = os.path.join(pasta_disciplina, "*.md")
arquivos_encontrados = glob.glob(caminho_busca)

for arquivo in arquivos_encontrados:
    with open(arquivo, encoding="utf-8") as f:
        conteudo = f.read()

    soup = BeautifulSoup(conteudo, "html.parser")

    # Para cada classe declarada em CLASSES, coleta as divs desse arquivo
    # e adiciona na lista correspondente dentro do dicionário "resultados"
    for classe, aplicar_nome in CLASSES:
        divs_coletadas = coletar_divs(soup, classe, aplicar_nome)
        resultados[classe] = resultados[classe] + divs_coletadas


# Ordena cada lista do dicionário pelo seu próprio id, individualmente
for classe in resultados:
    lista_da_classe = resultados[classe]
    lista_da_classe.sort(key=lambda tupla: tupla[0])
    resultados[classe] = lista_da_classe


os.makedirs(pasta_saida, exist_ok=True)

# Escreve o arquivo final seguindo exatamente a ordem declarada em CLASSES.
# Primeiro escreve todas as divs da primeira classe da lista, depois todas
# as divs da segunda classe, e assim por diante.
arquivo_de_saida = open(arquivo_saida, "w", encoding="utf-8")

for classe, aplicar_nome in CLASSES:
    lista_da_classe = resultados[classe]
    for item in lista_da_classe:
        id_da_div = item[0]
        html_da_div = item[1]
        arquivo_de_saida.write(html_da_div)
        arquivo_de_saida.write("\n\n")

arquivo_de_saida.close()


# Monta a mensagem final de log, contando quantas divs foram salvas por classe
partes_da_mensagem = []
total_geral = 0

for classe, aplicar_nome in CLASSES:
    quantidade = len(resultados[classe])
    total_geral = total_geral + quantidade
    partes_da_mensagem.append(f"{quantidade} {classe}")

mensagem_final = ", ".join(partes_da_mensagem)
print(f"{mensagem_final} ({total_geral} no total) salvos em {arquivo_saida}")
