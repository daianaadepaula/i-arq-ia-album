# Alura Album - Copa do Mundo Tech

O **Alura Album** é uma aplicação web interativa que simula um álbum de figurinhas físico em 3D, prestando um tributo a grandes mentes e pioneiros que revolucionaram a história da computação e da tecnologia, divididos em categorias como Inteligência Artificial, Python, Banco de Dados, Sistemas Operacionais e Personalidades Tech do Brasil.

---

## 🎯 Objetivo do Projeto

O objetivo principal do projeto é proporcionar uma experiência nostálgica e altamente interativa de colecionar figurinhas no navegador. O álbum busca dinamicamente as figurinhas de uma API e "cola" cada imagem no seu respectivo slot de colecionador. A aplicação utiliza animações fluidas, efeitos de relevo/sombra realistas para simular a lombada física do livro e até mesmo efeitos sonoros gerados por código para reproduzir a sensação de folhear páginas de papel reais.

---

## 📂 Estrutura de Arquivos e Funcionalidades

O frontend é composto por três arquivos principais, organizados de forma limpa e modular:

### 1. 📄 `index.html`
* **Função:** Fornece a estrutura de marcação semântica e esqueleto das páginas do álbum.
* **Componentes Principais:**
  * **Capa e Contracapa:** Estruturas estilizadas para a abertura e fechamento do livro.
  * **Páginas de Categoria:** Grades (`.stickers-grid`) compostas por espaços demarcados (`.sticker-slot`) com o número do slot e informações da respectiva figurinha.
  * **Navegação:** Botões de controle lateral para avançar/retroceder páginas e botão de controle de som.
  * **Dependências Externas:** Carrega fontes modernas do Google Fonts (*Inter* e *Outfit*) e importa a biblioteca **Page-Flip** via CDN para gerenciar a física de transição tridimensional das páginas.

### 2. 🎨 `style.css`
* **Função:** Responsável pelo design visual premium, ambientação e animações interativas do álbum.
* **Recursos Destacados:**
  * **Design System:** Definição de uma paleta de cores futurista focada em tons de azul escuro, preto profundo e elementos neon.
  * **Efeito Lombada:** Sombras dinâmicas que simulam a profundidade e a dobra das páginas ao meio quando o livro está aberto.
  * **Estilização de Figurinhas:** Efeitos de borda pontilhada nos slots vazios, transição suave (efeito "fade-in" com zoom) ao colar a imagem e um overlay elegante com o nome do desenvolvedor na base.
  * **Animações Especiais:** Efeito de *Glitch* animado nos títulos da capa, cards flutuantes decorativos em 3D e anéis tecnológicos rotativos.

### 3. ⚡ `app.js`
* **Função:** Implementa toda a lógica comportamental, sons dinâmicos e conexão com o backend.
* **Lógicas Implementadas:**
  * **Integração com API:** Realiza uma chamada assíncrona (`fetch`) à API (`/figurinhas`) para recuperar o banco de figurinhas. Associa os IDs retornados aos respectivos slots e renderiza as imagens dinamicamente.
  * **Física de Folhear:** Inicializa a biblioteca `St.PageFlip` controlando tamanhos, sombras e limites de virada de página. Adiciona controle de arraste nativo por mouse e touch.
  * **Efeito Sonoro Dinâmico:** Utiliza a **Web Audio API** para gerar som sintético de papel folheando (processando ruído branco por filtros de passa-banda e passa-baixa com decaimento exponencial).
  * **Navegação Amigável:** Oculta as setas de navegação automaticamente quando o usuário está na primeira ou na última página e mapeia atalhos das setas do teclado (`←` e `→`) para virar as páginas.

---

## 🛠️ Tecnologias Utilizadas

* **HTML5** (Semântica)
* **CSS3** (Variáveis, Grid/Flexbox, Keyframes e Efeitos Visuais)
* **JavaScript Moderno** (Web Audio API, Fetch API, DOM Manipulation)
* **Page-Flip.js** (Biblioteca para simulação física de folhear livros)

---

## 🚀 Como Executar o Projeto

1. Certifique-se de que o backend de figurinhas está em execução (por padrão na porta `8000`).
2. Abra o arquivo `index.html` em seu navegador.
   * *Dica:* Utilize uma extensão como o **Live Server** (do VS Code) ou sirva os arquivos estáticos via terminal para evitar problemas com requisições CORS de arquivos locais:
     ```bash
     # Usando Python
     python -m http.server 3000
     ```
3. Acesse `http://localhost:3000` no seu navegador e divirta-se!
