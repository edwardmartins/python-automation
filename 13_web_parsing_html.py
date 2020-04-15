# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import bs4, requests

# Probably blocking the requests because it doesn't come from browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

res = requests.get('https://surf3.es/tienda/surf/tablas-de-surf/tablas-de-surf-torq/\
     tablas-torq-funboard/tabla-de-surf-torq-fun-7-2-pinline-blue/',headers=headers)

# Control everything went right
print('Error: ' + str(res.raise_for_status()))

# Stored the html document in a soup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Select the price in the html document
elems = soup.select('h3.price > span:nth-child(1)')
print(elems[0].text.strip())

# Function to get a price of a product in a surf webpage
def get_product_price(product_url):
     res = requests.get(product_url)
     res.raise_for_status()
     soup = bs4.BeautifulSoup(res.text, 'html.parser')
     elems = soup.select('h3.price > span:nth-child(1)')
     return elems[0].text.strip()


price = get_product_price('https://surf3.es/tienda/surf/tablas-de-surf/\
     tablas-de-surf-torq/tablas-torq-fish/tabla-de-surf-torq-tec-gokart-5-8-white/')

print('The price is: ' + price)