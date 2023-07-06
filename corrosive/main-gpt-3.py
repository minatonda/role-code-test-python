import cv2
from matplotlib import pyplot as plt
import numpy as np

def encontrar_corrosao(imagem):
    # Carregar a imagem
    img = cv2.imread(imagem)

    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar um filtro de suavização para reduzir ruídos
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Aplicar a detecção de bordas usando o operador de Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Aplicar uma operação morfológica de dilatação para conectar as bordas
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(edges, kernel, iterations=1)

    # Encontrar os contornos na imagem dilatada
    contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Inicializar uma lista para armazenar os pontos de corrosão
    pontos_corrosao = []

    # Iterar sobre os contornos encontrados
    for contour in contours:
        # Calcular a área do contorno
        area = cv2.contourArea(contour)

        # Filtrar contornos pequenos (ruídos)
        if area > 100:
            # Encontrar o centro do contorno
            M = cv2.moments(contour)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Adicionar o ponto de corrosão à lista
            pontos_corrosao.append((cx, cy))

            # Desenhar um círculo no ponto de corrosão na imagem original
            cv2.circle(img, (cx, cy), 3, (0, 255, 0), -1)

    # Exibir a imagem com os pontos de corrosão destacados
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

    # Retornar os pontos de corrosão encontrados
    return pontos_corrosao

# Caminho para a imagem de entrada
imagem = "./data/base/with-corrosion/0.jpg"
imagem = "./data/base/with-corrosion/1.jpg"
imagem = "./data/base/with-corrosion/2.jpg"
# imagem = './data/0.jpg'

# Encontrar os pontos de corrosão na imagem
pontos_corrosao = encontrar_corrosao(imagem)

# Exibir os pontos de corrosão encontrados
print("Pontos de Corrosão:")
for ponto in pontos_corrosao:
    print(ponto)