import requests
def get_preco(url):
    pagina = requests.get(url)
    inicio = pagina.text.find('$')
    preco = float(pagina.text[inicio+1:inicio+5])
return preco

preco_1 = get_preco('http://beans.itcarlow.ie/prices.html')
print(preco_1)


compra =  15

if preco <= compra:
    print('pode comprar')



