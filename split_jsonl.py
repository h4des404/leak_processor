import json
import os
from colorama import Fore, Back, Style, init

# Inicializa o colorama para funcionar em qualquer sistema operacional
init(autoreset=True)

def print_banner():
    print(Fore.CYAN + """
    ##########################################
    #     Script de Divisão de Arquivos     #
    #         by h4des404 - D34THSEC        #
    ##########################################
    """)

def show_menu():
    print(Fore.GREEN + "\nMenu de Opções:")
    print(Fore.YELLOW + "1." + Style.BRIGHT + " Alterar nome do arquivo de entrada")
    print(Fore.YELLOW + "2." + Style.BRIGHT + " Alterar prefixo de saída")
    print(Fore.YELLOW + "3." + Style.BRIGHT + " Definir tamanho máximo de arquivo (em GB)")
    print(Fore.YELLOW + "4." + Style.BRIGHT + " Rodar o script")
    print(Fore.YELLOW + "5." + Style.BRIGHT + " Sair")

def main():
    print_banner()

    input_file = "twd.json"  # Nome padrão do arquivo de entrada
    output_prefix = "twd_part"  # Prefixo padrão para arquivos de saída
    max_size_bytes = 2 * 1024 * 1024 * 1024  # Tamanho padrão: 2 GB

    while True:
        show_menu()
        option = input(Fore.CYAN + "\nEscolha uma opção: ")

        if option == "1":
            input_file = input(Fore.CYAN + "\nDigite o nome do arquivo de entrada (ex: 'twd.json'): ")
            print(Fore.GREEN + f"Arquivo de entrada alterado para: {input_file}")
            
        elif option == "2":
            output_prefix = input(Fore.CYAN + "\nDigite o prefixo de saída (ex: 'twd_part'): ")
            print(Fore.GREEN + f"Prefixo de saída alterado para: {output_prefix}")
        
        elif option == "3":
            try:
                size_gb = float(input(Fore.CYAN + "\nDigite o tamanho máximo do arquivo (em GB): "))
                max_size_bytes = size_gb * 1024 * 1024 * 1024
                print(Fore.GREEN + f"Tamanho máximo alterado para: {size_gb} GB")
            except ValueError:
                print(Fore.RED + "Por favor, insira um número válido.")
        
        elif option == "4":
            print(Fore.GREEN + "\nIniciando o processo de divisão do arquivo...")
            break
        
        elif option == "5":
            print(Fore.RED + "Saindo...")
            exit(0)
        
        else:
            print(Fore.RED + "Opção inválida! Tente novamente.")
    
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

    print(Fore.GREEN + "\n[✔] Processamento concluído.")
    print(Fore.CYAN + f"[📄] Total de linhas lidas     : {total}")
    print(Fore.GREEN + f"[+] Linhas válidas salvas     : {salvos}")
    print(Fore.RED + f"[-] Linhas corrompidas ignoradas : {corrompidos}")
    print(Fore.CYAN + f"[🧩] Total de partes geradas   : {part_number}")

if __name__ == "__main__":
    main()
