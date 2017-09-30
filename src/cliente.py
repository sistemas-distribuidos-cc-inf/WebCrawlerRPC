#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib
import sys

pagesCrawled = []
url_seed = ''
max_page = 0

def main():

    client = xmlrpclib.ServerProxy('localhost')
    print 'Client started'

    if len( sys.argv ) == 3:

        url_seed = sys.argv[1]
        max_page = sys.argv[2]
        pagesCrawled = client.crawl_web( url_seed, max_page )
        with open("Conteudo Busca.txt", "w") as links_file: links_file.write( str( pagesCrawled ) )
        print 'Success!'

    else:
        print 'Error: Espera-se <programa> <url> <qtd max_page>\n'

if __name__ == "__main__":
    main()
