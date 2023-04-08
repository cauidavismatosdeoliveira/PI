import math
import numpy as np
import cv2
angle = 0
def rotate_direct(image, angle):
    # Calculando as dimensões da nova imagem
    height, width = image.shape[:2]
    center_x, center_y = width/2, height/2
    radians = math.radians(angle)
    cos_theta = math.cos(radians)
    sin_theta = math.sin(radians)

    # Criando uma nova imagem
    new_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Rotação dos pixels da imagem original na nova imagem
    for y in range(height):
        for x in range(width):
            new_x = int(cos_theta * (x - center_x) + sin_theta * (y - center_y) + center_x)
            new_y = int(-sin_theta * (x - center_x) + cos_theta * (y - center_y) + center_y)
            if 0 <= new_x < width and 0 <= new_y < height:
                new_image[new_y, new_x] = image[y, x]

    return new_image


def rotate_inverse(image, angle):
    # Calculando as dimensões da nova imagem
    height, width = image.shape[:2]
    center_x, center_y = width/2, height/2
    radians = math.radians(angle)
    cos_theta = math.cos(radians)
    sin_theta = math.sin(radians)
   

    # Criando uma nova imagem
    new_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Rotação dos pixels da nova imagem na imagem original
    for y in range(height):
        for x in range(width):
            new_x = int(cos_theta * (x - center_x) - sin_theta * (y - center_y) + center_x)
            new_y = int(sin_theta * (x - center_x) + cos_theta * (y - center_y) + center_y)
            if 0 <= new_x < width and 0 <= new_y < height:
                new_image[y, x] = image[new_y, new_x]

    return new_image

image = cv2.imread('ifma-caxias.jpg')

while(True): 
    
    direct = rotate_direct(image, angle)
    inverse = rotate_inverse(image, angle)
    cv2.imshow("direta", direct)
    cv2.imshow("inversa", inverse)
    
    if angle > 360: angle = 0
    
    k=cv2.waitKey(20)
    
    if k == ord('r'):
        angle = angle + 5
    if k == ord('l'):
        angle = 0
    if k == ord('q'):
        break
cv2.destroyAllWindows()