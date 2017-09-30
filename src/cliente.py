#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib
import sys

pagesCrawled = []
url_seed = ''
max_page = 0

def main():

    proxy = xmlrpclib.ServerProxy('http://localhost:8000')
    print 'Client started'

    if len( sys.argv ) == 3:

        url_seed = sys.argv[1]
        max_page = sys.argv[2]
        try:
            with open( "ResultBusca.txt", "wb" ) as handle:
                handle.write( proxy.crawl( url_seed, max_page ).data )
            handle.close()
            print 'Success!'
        except:
            print 'Call failed.'
    else:
        print 'Error: Espera-se <programa> <url> <qtd max_page>\n'

if __name__ == "__main__":
    main()
