import requests, bs4

# https://en.wikipedia.org/wiki/Jonas_Salk
# http://example.com

# res = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")
res = requests.get("http://example.com")

print(type(res))
print(res.text)
print('\n')

soup = bs4.BeautifulSoup(res.text, "lxml")
print(soup)

# Select HTML elements; h1, p, etc...
print(soup.select('title')[0].getText())
site_paragraphs = soup.select('p')
print(type(site_paragraphs))
print(*site_paragraphs)
print(site_paragraphs[0].getText())

print("\n")
# Grabbing all elements of a class
res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(res.text, "lxml")
first_item = soup.select('.toctext')[0].getText()
print(first_item)
for item in soup.select('.toctext'):
    print(item.text)

print('\n')
# Grabbing images
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, "lxml")
img = soup.select('.thumbimage')
computer = soup.select('.thumbimage')[0]
print(type(computer))
print(computer['src'])

# Downloading an image
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/5/52/Chess_Programming.svg', stream=True)
# image_link.content
f = open('my_computer_image.svg', 'wb')
f.write(image_link.content)
f.close()

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/399px-Deep_Blue.jpg', stream=True)
# image_link.content
f = open('my_computer_image.jpg', 'wb')
f.write(image_link.content)
f.close()

