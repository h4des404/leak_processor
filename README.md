# 📁 Splitter de Arquivo JSONL com Menu Interativo

Este projeto contém um script Python que divide grandes arquivos `.json` ou `.jsonl` em partes menores no formato JSONL (JSON Lines), com **interface de menu interativo colorido** via terminal.  
Ideal para manipular grandes volumes de dados de forma simples e prática.

---

## 🎯 Objetivo

O script `split_jsonl.py` lê um arquivo JSON linha por linha, valida seu conteúdo e cria múltiplos arquivos de saída menores, cada um com um tamanho máximo definido pelo usuário.  
O processo é todo realizado por um menu interativo no terminal.

---

## 🖥️ Funcionalidades do Menu

- ✅ Alterar nome do arquivo de entrada  
- ✅ Alterar prefixo de saída dos arquivos  
- ✅ Definir tamanho máximo de arquivo (em GB)  
- ✅ Rodar o script  
- ✅ Sair do menu  

---

## 📦 Requisitos

Antes de executar o script, você precisa ter o Python instalado e as bibliotecas listadas abaixo:

### Bibliotecas necessárias:

- `json` (nativa do Python)
- `colorama` (para colorir o terminal)

### Instalação das dependências:

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

Instale as dependências com:

```bash
pip install -r requirements.txt
```

#### `requirements.txt` recomendado:

```
colorama
```

---

## 🚀 Como rodar o script

### 1. Clone o repositório

```bash
git clone https://seu-repositorio-url.git
cd seu-repositorio
```

### 2. Configure o arquivo de entrada e outras opções pelo menu

Execute o script:

```bash
python split_jsonl.py
```

Você verá o seguinte menu:

```
Menu de Opções:
1. Alterar nome do arquivo de entrada
2. Alterar prefixo de saída
3. Definir tamanho máximo de arquivo (em GB)
4. Rodar o script
5. Sair
```

Siga as instruções e selecione as opções desejadas.

---

## ⚙️ Exemplo de uso

Se quiser dividir um arquivo `dados.json` em arquivos menores de até 1 GB com prefixo `saida`, basta configurar:

```
Arquivo de entrada: dados.json
Prefixo de saída: saida
Tamanho máximo: 1
```

O script gerará arquivos como:

```
saida_1.jsonl
saida_2.jsonl
saida_3.jsonl
...
```

---

## 📊 Relatório final no terminal

Ao final do processo, será exibido:

```text
[✔] Processamento concluído.
[📄] Total de linhas lidas     : 1000000
[+] Linhas válidas salvas     : 998000
[-] Linhas corrompidas ignoradas : 2000
[🧩] Total de partes geradas   : 50
```

---

## ✅ Considerações Finais

Este script foi desenvolvido para facilitar a divisão de arquivos JSON grandes em partes menores com um menu interativo amigável.  
A biblioteca `colorama` garante uma visualização mais clara e interativa no terminal.

Contribuições são bem-vindas. 👾  
By **h4des404 - D34THSEC**