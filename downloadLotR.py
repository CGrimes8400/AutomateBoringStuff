import requests, os, bs4


url = "https://www.shamusyoung.com/twentysidedtale/?p=1331"

os.makedirs('DMoftheRings',exist_ok=True)


finishedflag = False


while not finishedflag:
    print ("Downloading Page: %s" % url)
    result = requests.get(url)
    result.raise_for_status()
    
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    
    mydivs = soup.find_all("div", {"class": "entry-text"})
    myimgs = mydivs[0].find_all("img")
    for currentimg in myimgs:
        comicUrl = currentimg.get("src")
        if comicUrl.endswith("jpg"):
            print("Downloading image: %s" % comicUrl)
            result = requests.get(comicUrl)
            result.raise_for_status()

            imageFile = open(os.path.join("DMoftheRings", os.path.basename(comicUrl)), "wb")

            for chunk in result.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    if url.endswith('612'):
        finishedflag = True
    myprev = soup.find_all("div", {"class": "prev-next-container"})[0]
    prevLink = myprev.find_all('a')[0]
    url = "https://www.shamusyoung.com/twentysidedtale/" + prevLink.get("href")
    

print("Done")