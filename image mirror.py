from  PIL import  Image
imag= Image.open("C:/Users/Asadul/Downloads/joker.jpg.jpg") ## Input Your image Location
imag.show()
Mirror_image =imag.transpose(Image.FLIP_LEFT_RIGHT)
Mirror_image.save('joker_mirror.png') ##Type new file name
p2 = Image.open("joker_mirror.png") ##open your image
p2.show()
