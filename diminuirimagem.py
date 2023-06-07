import cv2

# Carrega a imagem
img = cv2.imread('perfil.png')

# Define o fator de redução da imagem
fator_reducao = 0.2

# Aplica a redução de tamanho
#nova_altura = int(img.shape[0] * fator_reducao)
#nova_largura = int(img.shape[1] * fator_reducao)
nova_altura = int(200)
nova_largura = int(200)
img_reduzida = cv2.resize(img, (nova_largura, nova_altura))

# Exibe a imagem original e a imagem reduzida
cv2.imshow("Imagem Original", img)
cv2.imshow("Imagem Reduzida", img_reduzida)
cv2.imwrite('perfil1.png', img_reduzida)
# Espera por uma tecla ser pressionada para fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
