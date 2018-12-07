import PIL.Image
import glob
import colorsys

colour_map = {
    range(0, 20): "Vermelho",
    range(20, 40): "Laranja",
    range(40, 75): "Amarelo",
    range(75, 175): "Verde",
    range(175, 255): "Azul",
    range(255, 290): "Roxo",
    range(290, 335): "Rosa",
    range(335, 361): "Vermelho"
}

def define_colour(hue, avg_colour):
    if hue == "Vermelho" and avg_colour[1] < 40 and avg_colour[2] > 80:
        print("Rosa")
    else:
        print(hue)

def detect(path, x, y, width, height):
    img = PIL.Image.open(path)
    npix = width * height
    avg_colour = [0, 0, 0]

    for i in range(y, y + height):
        for j in range(x, x + width):
            temp = img.getpixel((j,i))
            for k in range(3):
                avg_colour[k] += temp[k]

    for l in range(3):
        avg_colour[l] /= npix

    avg_colour = list(map(float, colorsys.rgb_to_hsv(avg_colour[0], avg_colour[1], avg_colour[2])))
    avg_colour[0] *= 360
    avg_colour[0] = int(avg_colour[0])
    avg_colour[1] *= 100

    if avg_colour[1] < 20:
        if avg_colour[2] < 30:
            print("Preto")
        elif avg_colour[2] < 80:
            print("Cinza")
        else:
            print("Branco")

    else:
        for key in colour_map.keys():
            if avg_colour[0] in key:
                define_colour(colour_map[key], avg_colour)
