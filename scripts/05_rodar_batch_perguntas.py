
import csv
import importlib.util
import os

# Carrega dinamicamente o modulo `04_consultar_rag.py`,
# evitando erro de sintaxe por causa do nome que comeca com digitos.
_module_path = os.path.join(os.path.dirname(__file__), "04_consultar_rag.py")
_spec = importlib.util.spec_from_file_location("consultar_rag", _module_path)
_consultar_rag = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_consultar_rag)
gerar_resposta = _consultar_rag.gerar_resposta

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
