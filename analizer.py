import tkinter as tk
from tkinter import filedialog
import os
import csv
import re
from collections import Counter

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
    return file_path

def validar_arquivo_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        return header[0] == "message"

def processar_arquivo_csv(file_name, column_index):
    valores = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pular o cabeçalho se houver
        for row in reader:
            if len(row) > column_index:
                cell_value = row[column_index]
                mensagem_formatada = formatar_mensagem(cell_value)
                valores.append(mensagem_formatada)
    return valores

def formatar_mensagem(cell_value):
    resultado = re.search(r'errorMessage:(.*?)statusCode:', cell_value, re.DOTALL)
    if resultado:
        # Remover quebras de linha e espaços extras
        mensagem_formatada = resultado.group(1).strip().replace('\n', ' ')
        if not mensagem_formatada:
            # Extrair a nova string entre 'statusCode:' e 'url:'
            novo_resultado = re.search(r'statusCode:(.*?url:)', cell_value, re.DOTALL)
            if novo_resultado:
                # Incluir 'statusCode:' na nova string extraída
                mensagem_formatada = "statusCode: " + novo_resultado.group(1).strip().replace('\n', ' ')
        if "You don't have permission to access" in mensagem_formatada:
            # Substituir a string específica por "Access Denied"
            mensagem_formatada = "Access Denied"
    else:
        mensagem_formatada = "Nenhuma correspondência encontrada."
    return mensagem_formatada

def escrever_csv(output_file, data):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Valor', 'Ocorrências'])
        for valor, contagem in data:
            writer.writerow([valor, contagem])

if __name__ == "__main__":
    arquivo_csv = selecionar_arquivo()
    if arquivo_csv:
        if validar_arquivo_csv(arquivo_csv):
            indice_coluna = 0
            valores = processar_arquivo_csv(arquivo_csv, indice_coluna)
            contagem_valores = Counter(valores)
            array_ordenado = sorted(contagem_valores.items(), key=lambda x: x[1], reverse=True)
            nome_arquivo_saida = os.path.splitext(arquivo_csv)[0] + "_analisado.csv"
            escrever_csv(nome_arquivo_saida, array_ordenado)
            print(f"Saída gravada em {nome_arquivo_saida}")
        else:
            print("O arquivo CSV selecionado não está no formato desejado. O título da coluna 0 deve ser 'message'.")
    else:
        print("Nenhum arquivo selecionado.")
