import getopt
import sys
import numpy
from scipy import misc


def freq_abs_acumulada(img, largura, altura):
    tamanho = 256
    frequencia = numpy.zeros(tamanho)

    for i in xrange(altura):
        for j in xrange(largura):
            frequencia[img[i][j]] += 1

    acumulado = 0
    for i in xrange(tamanho):
        acumulado += frequencia[i]
        frequencia[i] = acumulado

    return frequencia


def equalize(x, frequencia, xmin, tamanho):
    return round(((frequencia[x] - xmin) / (tamanho - xmin)) * 256)


def convolution(x, y, img, factor):
    value = img[x][y]
    for s in xrange(-1, 2):
        for t in xrange(-1, 2):
            value += img[x + s][y + t] * factor

    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value


def soften_avg(x, y, img):
    value = img[x][y]
    factor = 0
    for s in xrange(-1, 2):
        for t in xrange(-1, 2):
            if s + t == -2 or s + t == 2 or (s + t == 0 and (s, t) != (0, 0)):
                factor = 1 / 16
            elif (s, t) != (0, 0):
                factor = 2 / 16
            else:
                factor = 4 / 16
            value += img[x + s][y + t] * factor

    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value


class Transformation(object):

    def __init__(self, img):
        self.img = img
        self.largura = img.shape[0]
        self.altura = img.shape[1]
        self.out = numpy.zeros((self.altura, self.largura))

    def contrast(self):
        frequencia = freq_abs_acumulada(self.img, self.largura, self.altura)
        xmin = numpy.amin(frequencia)
        for i in xrange(self.altura):
            for j in xrange(self.largura):
                self.out[i][j] = equalize(self.img[i][j], frequencia, xmin,
                                          (self.largura * self.altura))

    def blur(self):
        for x in xrange(1, self.altura - 1):
            for y in xrange(1, self.largura - 1):
#                self.out[x][y] = convolution(x, y, self.img, 0.1)
                self.out[x][y] = soften_avg(x, y, self.img)

    def sharpen(self):
        pass


def main():
    (optlist, args) = getopt.getopt(sys.argv[1:], '',
                                    ['contrast', 'blur', 'sharpen'])
    filename = sys.argv[-1]
    filename_out = filename.split('.')[0] + '-final.' + filename.split('.')[-1]
    img = misc.imread(filename)
    transformation = Transformation(img)

    # Roda o metodo
    method = optlist[0][0][2:]
    getattr(transformation, method)()

    # Saida
    misc.imsave(filename_out, transformation.out)


if __name__ == '__main__':
    main()