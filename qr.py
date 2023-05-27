import qrcode

img = qrcode.make( input('Introducir dirección: '))
img.save( input('Nombra el archivo: ') + '.jpg')
img.show()
