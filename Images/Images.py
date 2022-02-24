from PIL import Image
mac = Image.open('example.jpeg')
print(type(mac))
#mac.show()
print(mac.size)
print(mac.filename)
print(mac.format_description)

# Cropping images
cropped_image = mac.crop((0, 0, 100, 100))
cropped_image.show()

#Cropping penciles
pencils = Image.open('pencils.jpeg')
print(pencils.size)
#Bottom pencils
x = 0
y = 1100
w = 1950/3
h = 1300
cropped_pencils = pencils.crop((x, y, w, h))
cropped_pencils.show()

#Compuer of example.jpeg
halfway = 1993/2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
computer = mac.crop((x, y, w, h))
computer.show()

#Copying images
mac.paste(im=computer, box=(0,0))
mac.show()

#Resize image
mac.resize((3000, 500))

#Rotate images
mac.rotate(90)

#Transparency
#RGBA - Red Green Blue Alpha
red = Image.open('red_color.jpeg')
blue = Image.open('blue_color.png')
blue.putalpha(255)
blue.paste(im=red, box=(0, 0), mask=red)
blue.show()
