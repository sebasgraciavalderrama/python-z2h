import bs4, requests

# Get title of every book with a 2 star rating
# https://books.toscrape.com/catalogue/page-1.html

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
'''
res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
#print(len(soup.select(".product_pod")))
products = soup.select(".product_pod")
example = products[0]
# Check if a book is 2-star rated
print('star-rating Three' in str(example))
print(example.select(".star-rating.Three"))
print([] == example.select(".star-rating.Two"))
# Grab the title of a book
print(example.select('a')[1]['title'])
'''
two_star_titles = []

for n in range(1,51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:
        # if 'star-rating Two' in str(book)
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)
print("2-star rated books: ", *two_star_titles, sep='\n')