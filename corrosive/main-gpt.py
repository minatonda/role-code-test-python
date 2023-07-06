import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_corrosion(image_path):
    # Faz o download da imagem a partir do URL
    # response = requests.get(image_url)
    # image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)
    image = cv2.imread(image_path)

    # Converte a imagem para tons de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    # Aplica a limiarização adaptativa para destacar as áreas de corrosão
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    # Encontra os contornos na imagem limiarizada
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtra os contornos com área menor que um limiar
    threshold_area = 100
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > threshold_area]

    if filtered_contours:
        # Cria uma máscara preta com o mesmo tamanho da imagem
        mask = np.zeros_like(image)

        # Desenha os contornos filtrados na máscara
        cv2.drawContours(mask, filtered_contours, -1, (0, 255, 0), 2)

        # Combina a máscara com a imagem original usando operação bitwise OR
        corrosion_image = cv2.bitwise_or(image, mask)

        # Classificação dos tipos e graus de corrosão (substitua com o modelo treinado)
        classification_result = classify_corrosion(corrosion_image)

        # Exibe a imagem com os contornos identificados
        plt.imshow(cv2.cvtColor(corrosion_image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()

        # Imprime o resultado da classificação
        print("Resultado da classificação: ", classification_result)
    else:
        print("Nenhuma área de corrosão foi encontrada.")

def classify_corrosion(corrosion_image):
    # Implementação fictícia de classificação para fins ilustrativos
    # Aqui você pode substituir por um modelo treinado ou algoritmo de classificação adequado

    # Exemplo de classificação fictícia
    return "Tipo: Pitting, Grau: Moderado"

# Caminho da imagem a ser analisada
image_path = "./data/base/with-corrosion/0.jpg"
image_path = "./data/base/with-corrosion/1.jpg"
image_path = "./data/base/with-corrosion/2.jpg"
# image_path = './data/0.jpg'

# Chama a função para detectar a corrosão na imagem
detect_corrosion(image_path)