from urllib2 import urlopen
from urllib import urlretrieve
from bs4 import BeautifulSoup as soup

urlToScrape = input('Enter url to scrape for midi files: ')

webPage = urlopen(urlToScrape)

# Store HTML data into page_html. Use BeautifulSoup to parse HTML and store in page_soup
page_html = webPage.read()
webPage.close()
page_soup = soup(page_html, "html.parser")

# Find all HTML attributes
pageItems = page_soup.findAll("a")

# Select all href links
for link in page_soup.select('a[href^="http://"]'):
    href = link.get('href')

    # Validate midi file download link
    if not any(href.endswith(x) for x in ['.mid']):
        continue

    # Download the midi file while printing status
    filename = href.rsplit('/', 1)[-1]
    print("Downloading %s to %s..." % (href, filename))
    urlretrieve(href, filename)
    print("Download complete")
