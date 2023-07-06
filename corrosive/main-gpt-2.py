import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_corrosion(image_path):
     # Pré-processamento
    imagem = cv2.imread(image_path)

    imagem_preprocessada = imagem
    if len(imagem.shape) == 2:
        # Realçar contraste com equalização do histograma
        imagem_preprocessada = cv2.equalizeHist(imagem_preprocessada)
    else:
        # Converter para escala de cinza
        canal_b, canal_g, canal_r = cv2.split(imagem)
        # Aplicar equalização do histograma em cada canal
        canal_b_eq = cv2.equalizeHist(canal_b)
        canal_g_eq = cv2.equalizeHist(canal_g)
        canal_r_eq = cv2.equalizeHist(canal_r)
        # Combinar os canais equalizados de volta em uma imagem
        imagem_preprocessada = cv2.merge([canal_b_eq, canal_g_eq, canal_r_eq])

    # Segmentação baseada em cores
    # Converter para espaço de cores HSV
    imagem_hsv = cv2.cvtColor(imagem_preprocessada, cv2.COLOR_BGR2HSV)
    
    # Definir intervalo de cor para corrosão (nesse caso, tons de ferrugem)
    cor_min = np.array([0, 50, 50], dtype=np.uint8)
    cor_max = np.array([30, 255, 255], dtype=np.uint8)

    # Segmentar imagem com base no intervalo de cor
    mascara = cv2.inRange(imagem_hsv, cor_min, cor_max)
    imagem_segmentada = cv2.bitwise_and(imagem_preprocessada, imagem_preprocessada, mask=mascara)

    # Detecção de contornos
    imagem_gray = cv2.cvtColor(imagem_segmentada, cv2.COLOR_BGR2GRAY)
    _, imagem_bin = cv2.threshold(imagem_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(imagem_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    threshold_area = 100
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > threshold_area]

    if filtered_contours:
        # Cria uma máscara preta com o mesmo tamanho da imagem
        mask = np.zeros_like(imagem)

        # Desenha os contornos filtrados na máscara
        cv2.drawContours(mask, filtered_contours, -1, (0, 255, 0), 2)

        # Combina a máscara com a imagem original usando operação bitwise OR
        corrosion_image = cv2.bitwise_or(imagem, mask)

        # Exibe a imagem com os contornos identificados
        plt.imshow(cv2.cvtColor(corrosion_image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()

    else:
        print("Nenhuma área de corrosão foi encontrada.")

# Caminho da imagem a ser analisada
image_path = './data/base/with-corrosion/0.jpg'
image_path = './data/0.jpg'

# Chama a função para detectar a corrosão na imagem
detect_corrosion(image_path)