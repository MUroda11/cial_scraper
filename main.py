# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from joblib import Parallel, delayed
import json
import requests
import sys

from logo_scraper import get_logo
from phone_scraper import get_phones

def main(url):
    try:
        page = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(page.content, "html.parser")
    
        logo = get_logo(url, soup)
        phones = get_phones(soup)
        results = {} 
        results['logo'] = logo
        results['phones'] = phones
        results['website'] = url
        return results
    except Exception as e:
            sys.stderr.write(str(e) + '\n')
            return {}
        
if __name__ == '__main__':
    urls = [line.rstrip() for line in sys.stdin]
    results = Parallel(n_jobs=-1, prefer='threads')([delayed(main)(url) for url in urls])
    for res in results:
        sys.stdout.write(f'{json.dumps(res)}\n')
        