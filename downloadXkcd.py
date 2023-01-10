import requests, os, bs4


url = "https://xkcd.com"

os.makedirs('xkcd',exist_ok=True)

while not url.endswith('#'):
    print ("Downloading Page: %s" % url)
    result = requests.get(url)
    result.raise_for_status()
    
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("No comic image found")
    else:
        comicUrl = 'https:' + comicElem[0].get("src")
        print("Downloading image: %s" % comicUrl)
        result = requests.get(comicUrl)
        result.raise_for_status()
        
        imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
        
        for chunk in result.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prevLink.get("href")
print("Done")