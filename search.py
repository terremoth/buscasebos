import string
from scraper_parser import get_page_html_parser
from argparse import ArgumentParser
import urllib.parse

book_struct = {
    'name': None,
    'price': None,
    'author': None,
    'url': None,
    'image': None,
    'condition': None,
    'year': None,
    'publisher': None,
    'category': None,
}

argparser = ArgumentParser(description='Buscador de livros em Sebos')
argparser.add_argument('--title', '-t', type=str, help='Titulo do livro', required=True)
argparser.add_argument('--max-results', '-m', type=int, default=10, help='Numero maximo de resultados a buscar', required=False)
argparser.add_argument('--debug', '-d', help='Habilita Debug (prints com informacoes)', required=False)
args = argparser.parse_args()

pacobello_url = lambda url: 'https://pacobello.com.br/produtos/buscar/?s={}&categoria%5B%5D=LIVRO'.format(urllib.parse.quote_plus(url))

if args.title is not None:

    ''' 
    .items-grid .product-item
        img.img-produto-cod src
        .product-details 
            .product-title
            .product_meta
                span a 0 = author
                span a 1 = publisher
            p span = price

            .text attr

    '''

    pacobello_parsed = get_page_html_parser(pacobello_url(args.title))
    # items = pacobello_parsed.select_one('.product-item')
    items = pacobello_parsed.select('.product-item')
    # print(items)
    # print(items.select('.img-produto-cod'))

    for item in items[0:args.max_results]:
        # print(item)
        img = item.select_one('.img-produto-cod')['src']
        url = item.select_one('.link-img-produto-cod')['href']
        meta = item.select('.product_meta span a')
        author = 'Nao identificado'
        publisher = 'Nao identificado'
        print(len(meta))
        if len(meta) == 1:
            publisher = meta[1].text.replace('(', '').replace(')', '')
        elif len(meta) == 2:
            author = meta[0].text.replace('(', '').replace(')', '')
        
        price = item.select_one('.product-details p span').text.replace('|', '').strip()
        title = item.select_one('.product-details .product-title').text.strip()

        print(" title:\t\t{} \n url:\t\t{} \n img:\t\t{} \n author:\t{} \n publisher:\t{} \n price:\t\t{}\n".format(title,url,img,author,publisher,price))
        print("--------------------------------------------------------------------------------------")


