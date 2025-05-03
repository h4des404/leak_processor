# 📂 Splitter de Arquivo JSONL (Divisor de Arquivos JSONL)

Este repositório contém um script Python que divide grandes arquivos JSON em vários arquivos menores no formato JSONL (JSON Lines).  
É útil para manipular grandes volumes de dados, especialmente quando o arquivo excede os limites de tamanho do sistema de arquivos ou quando você precisa dividir os dados em partes menores para facilitar o processamento.

---

## 🎯 Objetivo

O script `split_jsonl.py` lê um arquivo JSON, valida cada linha como JSON e, quando o tamanho do arquivo atinge o limite configurado, grava a linha em um novo arquivo.  
Ele gera arquivos no formato JSONL, dividindo o original em várias partes menores.

---

## 📦 Requisitos

Antes de executar o script, você precisa garantir que as bibliotecas Python necessárias estejam instaladas.

### Bibliotecas necessárias:
- `json`: biblioteca padrão do Python para manipulação de dados JSON.

> ⚠️ Se o script for estendido e depender de outras bibliotecas, elas podem ser listadas em um arquivo `requirements.txt`.

### Como instalar as bibliotecas:
Embora `json` já venha com o Python, para instalar outras dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como rodar o script

### 1. Clone o repositório:

```bash
git clone https://seu-repositorio-url.git
cd seu-repositorio
```

---

### 2. Modifique o nome do arquivo de entrada:

No código, localize a variável `input_file`:

```python
input_file = "twd.json"
```

Altere `"twd.json"` para o caminho do seu arquivo JSON ou coloque o arquivo desejado no mesmo diretório do script.

---

### 3. (Opcional) Alterar o prefixo de saída:

Para mudar o prefixo dos arquivos gerados, edite:

```python
output_prefix = "twd_part"
```

---

### 4. Execute o script:

```bash
python split_jsonl.py
```

---

### 5. Verifique o resultado:

O script dividirá o arquivo original em partes menores de **2 GB** (valor padrão).  
O terminal mostrará:

- Total de linhas lidas
- Linhas válidas salvas
- Linhas corrompidas ignoradas
- Total de arquivos (partes) gerados

---

## ⚙️ Configurações

### Tamanho máximo do arquivo de saída:

```python
max_size_bytes = 2 * 1024 * 1024 * 1024  # 2 GB
```

Você pode ajustar esse valor conforme necessário.

---

## 💡 Exemplo de execução

Se você tiver um arquivo `dados.json` e quiser prefixar as saídas com `parte_dados`, edite:

```python
input_file = "dados.json"
output_prefix = "parte_dados"
```

Depois, execute:

```bash
python split_jsonl.py
```

Arquivos gerados:

```
parte_dados_1.jsonl
parte_dados_2.jsonl
parte_dados_3.jsonl
...
```

---

## 🛠️ Como o Script Funciona

1. **Leitura do arquivo JSON:** linha por linha (espera-se que cada linha seja um JSON válido).
2. **Validação:** cada linha é validada com `json.loads()`. Linhas inválidas são ignoradas.
3. **Divisão:** ao atingir o limite de tamanho, um novo arquivo é iniciado.
4. **Saída:** arquivos `.jsonl` sequenciais com um JSON por linha.

---

## 🗂️ Estrutura de Arquivos

Exemplo após execução:

```text
twd_part_1.jsonl
twd_part_2.jsonl
twd_part_3.jsonl
...
```

---

## 📊 Logs e Relatório

O script mostra no terminal:

- **Total de linhas lidas**: Quantas foram lidas do arquivo de entrada
- **Linhas válidas salvas**: Quantas foram gravadas com sucesso
- **Linhas corrompidas ignoradas**: Quantas falharam na validação
- **Total de partes geradas**: Arquivos `.jsonl` criados

### Exemplo de saída:

```
[✔] Processamento concluído.
[📄] Total de linhas lidas     : 1000000
[+] Linhas válidas salvas     : 998000
[-] Linhas corrompidas ignoradas : 2000
[🧩] Total de partes geradas   : 50
```

---

## ✅ Considerações Finais

Este script foi projetado para facilitar o trabalho com grandes volumes de dados JSON, especialmente quando o tamanho dos arquivos impede seu processamento completo.  
Ele garante que os dados sejam divididos em arquivos menores, facilitando etapas posteriores de análise ou processamento.
