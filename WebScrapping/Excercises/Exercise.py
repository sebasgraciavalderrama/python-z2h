import bs4, requests

base_url = 'https://quotes.toscrape.com'

res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup)

print('\n')
authors = []
my_authors = soup.select(".author")
for author in my_authors:
    authors.append(author.text)

print("Authors are: ", *authors, sep='\n')

print('\n')

quotes = []
my_quotes = soup.select(".quote")
for quote in my_quotes:
    quotes.append(quote.select(".text")[0].text)

print("Quotes are: ", *quotes, sep='\n')

print('\n')
tags = []
my_tags = soup.select(".tag-item")
#print(my_tags[0].select(".tag")[0].text)
for tag in my_tags:
    tags.append(tag.select(".tag")[0].text)

print("Top 10 tags are: ", *tags, sep='\n')

print('\n')
unique_authors = []
counter = 1
base_url = 'https://quotes.toscrape.com/page/{}/'
res = requests.get(base_url.format(counter))
while 'class="next"' in res.text:
    my_authors = soup.select(".author")
    for author in my_authors:
        unique_authors.append(author.text)
    res = requests.get(base_url.format(counter))
    counter +=1

print("Authors are: ", *list(set(unique_authors)), sep='\n')