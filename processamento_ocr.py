import pytesseract
from PIL import Image
import os

# Caminho para o Tesseract OCR (se necessário)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def realizar_ocr(imagem_path):
    """Função para realizar OCR em uma imagem e salvar o texto em um arquivo"""
    try:
        # Abrir a imagem
        imagem = Image.open(imagem_path)

        # Realizar OCR na imagem
        texto = pytesseract.image_to_string(imagem)

        # Salvar o texto extraído em um arquivo de texto
        output_path = f'output/{os.path.basename(imagem_path).replace(".jpg", ".txt").replace(".png", ".txt")}'
        with open(output_path, 'w') as arquivo_output:
            arquivo_output.write(texto)
        print(f"Texto extraído e salvo em: {output_path}")
    except Exception as e:
        print(f"Erro ao processar a imagem {imagem_path}: {e}")

# Caminho da pasta de imagens
input_folder = 'inputs/'

# Processar todas as imagens na pasta inputs
for imagem_file in os.listdir(input_folder):
    if imagem_file.endswith(".jpg") or imagem_file.endswith(".png"):
        imagem_path = os.path.join(input_folder, imagem_file)
        realizar_ocr(imagem_path)
