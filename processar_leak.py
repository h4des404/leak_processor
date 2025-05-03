import json
import os

input_file = "twd.json"
output_prefix = "twd_part"
max_size_bytes = 2 * 1024 * 1024 * 1024  # 2 GB

part_number = 1
current_size = 0
total = 0
salvos = 0
corrompidos = 0

output_file = f"{output_prefix}_{part_number}.jsonl"
f_out = open(output_file, "w", encoding="utf-8")

with open(input_file, "r", encoding="utf-8") as f_in:
    for line in f_in:
        total += 1
        try:
            obj = json.loads(line.strip())  # Valida JSON
            json_line = json.dumps(obj) + "\n"
            line_size = len(json_line.encode("utf-8"))

            if current_size + line_size > max_size_bytes:
                f_out.close()
                part_number += 1
                output_file = f"{output_prefix}_{part_number}.jsonl"
                f_out = open(output_file, "w", encoding="utf-8")
                current_size = 0

            f_out.write(json_line)
            current_size += line_size
            salvos += 1

        except json.JSONDecodeError:
            corrompidos += 1
            continue

f_out.close()

print("\n[✔] Processamento concluído.")
print(f"[📄] Total de linhas lidas     : {total}")
print(f"[+] Linhas válidas salvas     : {salvos}")
print(f"[-] Linhas corrompidas ignoradas : {corrompidos}")
print(f"[🧩] Total de partes geradas   : {part_number}")
