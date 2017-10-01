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
            with open( "SearchResult.txt", "wb" ) as handle:
                handle.write( proxy.crawl( url_seed, max_page ).data )
            handle.close()
            print 'Operation completed successfully!'
        except xmlrpclib.Fault as err:
            print 'A fault ocurred'
            print 'Fault code: %d' % err.faultCode
            print 'Fault string: %s' % err.faultString
    else:
        print 'Error: Espera-se <programa> <url> <qtd max_page>\n'

if __name__ == "__main__":
    main()
