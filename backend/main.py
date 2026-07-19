from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import glob
import json

# Define o caminho absoluto para a pasta de imagens para garantir que o servidor a encontre independente de onde for executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")
CAMINHO_JSON = os.path.join(PASTA_BASE, "figurinhas.json")

# Leitura do arquivo externo figurinhas.json ao inicializar o servidor para carregar todas as 30 figurinhas na memória
with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
    figurinhas = json.load(f)

# Criação da instância principal da aplicação FastAPI
app = FastAPI()

# Configura o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mantém a configuração para servir arquivos estáticos na rota "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Endpoint GET "/figurinhas" para listar apenas as figurinhas cujas imagens existem na pasta
@app.get("/figurinhas")
def listar_figurinhas():
    # Filtra dinamicamente as figurinhas que possuem o arquivo de imagem correspondente na pasta
    figurinhas_disponiveis = []
    for figurinha in figurinhas:
        padrao = os.path.join(PASTA_IMAGENS, f"{figurinha['id']:02d}[!0-9]*")
        if glob.glob(padrao):
            figurinhas_disponiveis.append(figurinha)
    return figurinhas_disponiveis

# Endpoint GET "/figurinhas/total" para obter as estatísticas de preenchimento do álbum
@app.get("/figurinhas/total")
def estatisticas_album():
    # Total de slots do álbum
    total_album = 30
    
    # Quantidade de figurinhas coladas é calculada dinamicamente com base nas imagens existentes
    coladas = 0
    for figurinha in figurinhas:
        padrao = os.path.join(PASTA_IMAGENS, f"{figurinha['id']:02d}[!0-9]*")
        if glob.glob(padrao):
            coladas += 1
            
    # Quantidade de figurinhas restantes para completar o álbum
    faltam = total_album - coladas
    
    # Retorna o dicionário contendo as estatísticas calculadas
    return {
        "total_album": total_album,
        "coladas": coladas,
        "faltam": faltam
    }

# Endpoint GET "/figurinhas/{id}" para buscar os dados de uma figurinha específica pelo ID (na lista completa)
@app.get("/figurinhas/{id}")
def obter_figurinha(id: int):
    # Procura a figurinha na lista completa com base no ID
    for figurinha in figurinhas:
        if figurinha["id"] == id:
            return figurinha
            
    # Caso a figurinha não seja encontrada, retorna erro 404 (Not Found)
    raise HTTPException(status_code=404, detail="Figurinha não encontrada")

# Endpoint GET "/figurinhas/{id}/imagem" para buscar e retornar o arquivo de imagem da figurinha
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Usa glob para encontrar o arquivo correspondente com o prefixo do ID formatado com 2 dígitos (ex: 01, 02)
    # seguido por qualquer caractere que não seja número [!0-9], para evitar colisões (ex: ID 1 e ID 10)
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    # Se nenhum arquivo correspondente for encontrado na pasta, retorna erro 404
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
        
    # Retorna o primeiro arquivo correspondente encontrado como resposta
    caminho_imagem = arquivos[0]
    return FileResponse(caminho_imagem)
