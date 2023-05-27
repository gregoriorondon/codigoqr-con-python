import qrcode

img = qrcode.make( input('introducir direccion: '))
img.save( input('nombra el archivo: ') + '.jpg')
img.show()
