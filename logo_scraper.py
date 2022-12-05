# -*- coding: utf-8 -*-
import re
from urllib.parse import urljoin

def get_logo(url, soup):

    logo_regex = re.compile('.*logo.*', re.IGNORECASE)
    link_regex = re.compile(r'https?://\S+?/\S+?\.(?:jpg|jpeg|svg|png)', re.IGNORECASE)
    link_regex_2 = re.compile(r'.(?:jpg|jpeg|svg|png)', re.IGNORECASE)
    
    try:
        images = soup.find_all(class_=logo_regex, src=link_regex)
        logo = images[0]['src']
    except:
        try:
            blocks = soup.find_all(class_=logo_regex)
            images = [block.find_all(src=[link_regex, link_regex_2]) for block in blocks]
            logo = images[0][0]['src']
            if (logo.startswith('http') == False):
                logo = urljoin(url, logo)
        except:
            logo = ''
    return logo
