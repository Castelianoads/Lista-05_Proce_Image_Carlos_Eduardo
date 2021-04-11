from PIL import Image

imagemOriginal = Image.open('imagens/natureza_original.jpg')

matriz = imagemOriginal.load()

for y in range(imagemOriginal.size[0]):
    for x in range(imagemOriginal.size[1]):
        r = 255 - matriz [y,x][0]
        g = 255 - matriz [y,x][1]
        b = 255 - matriz [y,x][2]
        matriz [y,x] = (r, g, b)

imagemOriginal.save('imagens/natureza_negativo.jpg')




