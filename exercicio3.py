from PIL import Image

imagemOriginal = Image.open('imagens/natureza_original.jpg')

matriz = imagemOriginal.load()

#gamma = 0.3
gamma = 1.8

for y in range(imagemOriginal.size[0]):
    for x in range(imagemOriginal.size[1]):
      r = int ((matriz[y, x][0]/255) ** gamma * 255)
      g = int ((matriz[y, x][1]/255) ** gamma * 255)
      b = int ((matriz[y, x][2]/255) ** gamma * 255)
      matriz[y, x] = (r, g, b)

imagemOriginal.save('imagens/natureza_gamma_1pt8.jpg')