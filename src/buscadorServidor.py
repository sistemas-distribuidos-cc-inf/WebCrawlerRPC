#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib
import urllib

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

def get_page( url ):
    try:
        return urllib.urlopen( url ).read()
    except:
        return ""

def get_next_target( page ):
    start_link = page.find( '<a href=' )

    if ( start_link == -1 ):
        return None, 0

    start_quote = page.find( '"', start_link )
    end_quote   = page.find( '"', start_quote + 1 )
    url = page[start_quote+1:end_quote]
    return url, end_quote

def get_all_links( page ):
    links = []
    while True:
        url,endpos = get_next_target( page )
        if url:
            links.append( url )
            page = page[endpos:]
        else:
            break
    return links

def union( p, q ):
    for e in q:
        if e not in p:
            p.append( e )

def lookup( index, keyword ):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_to_index( index, keyword, url ):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append( url )
            return
    index.append( [ keyword, [url] ] )

def add_page_to_index( index, url, content ):
    words = content.split()
    for word in words:
        add_to_index( index, word, url )

def crawl_web( seed, max_page ): # argumento opcional 'max_page'

    tocrawl = [seed]
    crawled = []
    index   = []

    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len( tocrawl ) < max_page:
            content_page = get_page( page )
            #add_page_to_index( index, page, content_page )
            union( tocrawl, get_all_links( content_page ) )
            crawled.append( page )
    with open("Search.txt", "wb") as links_file: links_file.write( str( crawled ) )
    links_file.close()

def returnFile( url, max_page ):

    crawl_web( url, max_page )
    try:
        with open( 'Search.txt', 'rb' ) as handle:
            return xmlrpclib.Binary( handle.read() )
    except:
            return 'error'

def main():

    server = SimpleXMLRPCServer(("localhost", 8000))
    print "Listening on port 8000..."

    server.register_function( returnFile, 'crawl' )
    server.serve_forever()

if __name__ == "__main__":
    main()
