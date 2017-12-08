import click
import requests
from PIL import Image
from StringIO import StringIO
from bs4 import BeautifulSoup

@click.command()
@click.argument('name', required=False)
def main(name):
    	URL='https://www.mancity.com/teams/first-team'
	html=requests.get(URL)
	b=BeautifulSoup(html.content,'html.parser')
	search=b.find_all('div',{'class','squad-listing--person--image-inner feed-section--grey'})
	for x in range(len(search)):
		
		S=str(search[x].picture.img['alt']).lower()
		#print(S)
		if name.lower()==S:
			url=search[x].picture.img['data-src']
			break
	req=requests.get(url)
    	img = Image.open(StringIO(req.content))
    	img.show()
