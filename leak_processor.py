import os
import argparse
import orjson
import pandas as pd

def process_leak(file_path, keywords, fields, chunk_size):
    output_dir = "extracted_chunks"
    os.makedirs(output_dir, exist_ok=True)

    chunk_counter = 0
    line_counter = 0
    buffer = []
    keyword_hits = []

    print(f"[*] Processando arquivo: {file_path}")
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line_counter += 1
            try:
                obj = orjson.loads(line.strip())
            except Exception:
                continue  # Ignora linhas corrompidas

            buffer.append(obj)

            # Filtro de palavras-chave por campos
            for field in fields:
                if field in obj:
                    content = str(obj[field]).lower()
                    if any(word.lower() in content for word in keywords):
                        keyword_hits.append(obj)
                        break  # Não repete o mesmo objeto várias vezes

            # Salva chunks
            if line_counter % chunk_size == 0:
                save_chunk(buffer, chunk_counter, output_dir)
                chunk_counter += 1
                buffer = []

        if buffer:
            save_chunk(buffer, chunk_counter, output_dir)

    print(f"[+] {chunk_counter + 1} chunks salvos.")
    save_keyword_hits_csv(keyword_hits)
    print("[+] Hits por palavra-chave exportados para keyword_hits_filtered.csv")

def save_chunk(objects, number, output_dir):
    filename = os.path.join(output_dir, f"chunk_{number}.jsonl")
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(orjson.dumps(obj).decode("utf-8") + "\n")
    print(f"[✓] Chunk {number} salvo com {len(objects)} objetos.")

def save_keyword_hits_csv(hits):
    if not hits:
        print("[!] Nenhum hit encontrado para exportar.")
        return
    try:
        df = pd.DataFrame(hits)
        df.to_csv("keyword_hits_filtered.csv", index=False)
    except Exception as e:
        print(f"[x] Falha ao exportar CSV: {e}")

def main():
    parser = argparse.ArgumentParser(description="Processador de leaks em JSONL com busca por palavras-chave.")
    parser.add_argument("--file", required=True, help="Caminho para o arquivo JSONL")
    parser.add_argument("--keywords", required=True, help="Palavras-chave separadas por vírgula (ex: admin,email)")
    parser.add_argument("--fields", required=True, help="Campos do JSON onde buscar as palavras-chave")
    parser.add_argument("--chunk-size", type=int, default=100_000, help="Número de linhas por chunk")
    
    args = parser.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",")]
    fields = [f.strip() for f in args.fields.split(",")]

    process_leak(args.file, keywords, fields, args.chunk_size)

if __name__ == "__main__":
    main()
