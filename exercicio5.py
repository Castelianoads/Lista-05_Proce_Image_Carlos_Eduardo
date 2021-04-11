from PIL import Image

imagemOriginal = Image.open('imagens/arara_original.jpg')

matriz = imagemOriginal.load()

for y in range(imagemOriginal.size[0]):
    for x in range(imagemOriginal.size[1]):
        r = matriz [y,x][0]
        g = matriz [y,x][1]
        b = matriz [y,x][2]
        matriz [y,x] = (0, 0, b)

imagemOriginal.save('imagens/arara_camada_b.jpg')