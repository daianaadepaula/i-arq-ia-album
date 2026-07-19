# Álbum de Figurinhas - Backend API

Este é o servidor de API para o projeto **Alura Album**, desenvolvido em Python utilizando o framework **FastAPI**. O backend é responsável por gerenciar o catálogo de figurinhas, fornecer as estatísticas de preenchimento do álbum e servir dinamicamente os arquivos de imagem das figurinhas para o frontend.

## 🎯 Objetivo

O objetivo deste backend é expor uma API REST estável, rápida e com suporte a CORS para que a aplicação frontend possa consumir e exibir de forma interativa as figurinhas colecionáveis da Cultura Pop, além de permitir o acompanhamento do progresso de preenchimento do álbum pelo colecionador.

---

## 📂 Estrutura de Arquivos e Pastas

* **`main.py`**: O ponto de entrada da aplicação. Contém a inicialização do FastAPI, configuração de middlewares (CORS), a leitura dinâmica das figurinhas a partir do arquivo JSON e todos os endpoints da API.
* **`figurinhas.json`**: Arquivo externo de configuração contendo os dados estruturados de todas as 30 figurinhas (incluindo nome, categoria e URL dinâmica da imagem) servindo como banco de dados em formato de arquivo.
* **`figurinhas/`**: Diretório que armazena os arquivos físicos de imagem (ex: `.jpg`, `.png`, `.webp`, `.avif`) associados a cada figurinha do álbum. As imagens são nomeadas com o formato de dois dígitos correspondente ao ID (ex: `01-alan-turing.jpg`, `02-john-mccarthy.jpg`).
* **`.venv/`**: Ambiente virtual Python isolado contendo as dependências do projeto (FastAPI, Uvicorn, etc.).
* **`__pycache__/`**: Arquivos de bytecode gerados automaticamente pelo Python para otimização de tempo de inicialização do servidor.

---

## 🚀 Como Executar o Servidor

### Pré-requisitos
Certifique-se de ter o Python 3 instalado em sua máquina.

### 1. Iniciar o Servidor
Com o terminal aberto no diretório `backend/`, execute o seguinte comando para iniciar o servidor Uvicorn com recarregamento automático (reload):

```bash
.venv\Scripts\uvicorn main:app --reload
```

O servidor iniciará localmente e estará acessível em: **`http://127.0.0.1:8000`**

---

## 🛣️ Endpoints da API

A API expõe as seguintes rotas de acesso:

### 1. Listar todas as Figurinhas
* **Rota**: `GET /figurinhas`
* **Descrição**: Retorna a lista contendo as figurinhas ativas (as que possuem imagem física disponível na pasta).
* **Exemplo de Retorno**:
  ```json
  [
    {
      "id": 1,
      "nome": "The Beatles",
      "categoria": "MUSIC-INT",
      "imagem_url": "/figurinhas/1/imagem"
    }
  ]
  ```

### 2. Estatísticas do Álbum
* **Rota**: `GET /figurinhas/total`
* **Descrição**: Retorna o progresso de preenchimento do álbum (calculado de forma dinâmica).
* **Exemplo de Retorno**:
  ```json
  {
    "total_album": 30,
    "coladas": 29,
    "faltam": 1
  }
  ```

### 3. Detalhes de uma Figurinha Específica
* **Rota**: `GET /figurinhas/{id}`
* **Descrição**: Retorna os dados detalhados de uma única figurinha pelo seu ID numérico.
* **Status**: Retorna `404 Not Found` caso a figurinha não exista na lista.

### 4. Obter Imagem da Figurinha
* **Rota**: `GET /figurinhas/{id}/imagem`
* **Descrição**: Busca dinamicamente na pasta `figurinhas/` pelo arquivo correspondente ao ID informado e o retorna como resposta de arquivo (`FileResponse`).
* **Status**: Retorna `404 Not Found` caso a imagem não exista física no diretório.

---

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework moderno, rápido e de alta performance para construção de APIs com Python.
- **Uvicorn**: Servidor web ASGI para rodar a aplicação FastAPI.
- **Glob & OS (Nativos)**: Utilizados para a manipulação de caminhos de arquivos de forma independente do sistema operacional e busca dinâmica de padrões de nomenclatura.
