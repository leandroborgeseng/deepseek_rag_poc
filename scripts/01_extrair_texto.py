
import os
import pdfminer.high_level
import pytesseract
from pdf2image import convert_from_path

def extrair_texto_pdf(path_pdf):
    try:
        texto = pdfminer.high_level.extract_text(path_pdf)
        if texto.strip():
            return texto
    except Exception:
        pass
    imagens = convert_from_path(path_pdf)
    texto_ocr = ""
    for imagem in imagens:
        texto_ocr += pytesseract.image_to_string(imagem)
    return texto_ocr

def main():
    pasta_pdfs = 'data/pdfs/'
    pasta_textos = 'data/textos/'
    os.makedirs(pasta_textos, exist_ok=True)

    for arquivo in os.listdir(pasta_pdfs):
        if arquivo.endswith('.pdf'):
            caminho_pdf = os.path.join(pasta_pdfs, arquivo)
            texto = extrair_texto_pdf(caminho_pdf)
            nome_txt = arquivo.replace('.pdf', '.txt')
            with open(os.path.join(pasta_textos, nome_txt), 'w', encoding='utf-8') as f:
                f.write(texto)

if __name__ == "__main__":
    main()
