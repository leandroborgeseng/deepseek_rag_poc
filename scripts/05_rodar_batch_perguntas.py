
import csv
from scripts.04_consultar_rag import gerar_resposta

def main():
    with open('data/perguntas.txt', 'r', encoding='utf-8') as f:
        perguntas = f.readlines()
    perguntas = [p.strip() for p in perguntas if p.strip()]

    with open('outputs/perguntas_respostas.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Pergunta', 'Resposta'])
        for pergunta in perguntas:
            resposta = gerar_resposta(pergunta)
            writer.writerow([pergunta, resposta])

if __name__ == "__main__":
    main()
