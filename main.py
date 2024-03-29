from bs4 import BeautifulSoup

with open( 'home.html' , "r") as arquivo:
    conteudo = arquivo.read()


#BeautifulSoup(<arquivo usado> , <metodo de parsing>)
soup = BeautifulSoup(conteudo, 'lxml')
#print(soup.prettify())

#it finds the first element in the page
tags = soup.find('h5')
#now it founds all
tags = soup.find_all('h5')

for course in tags:
    print(course.text)