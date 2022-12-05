# -*- coding: utf-8 -*-
import re

def get_phones(soup):
    for i in soup(['script']):
        i.decompose()
    data = '?'.join(soup.stripped_strings)
    
    phones = []
    tel = soup.find_all(href=re.compile('.*tel:.*', re.IGNORECASE))
    phones.extend(i.text for i in tel)

    match_phones = re.findall(r'[\(\+]?\d{1,3}?[-\)\(]*\s?\(?\d{1,4}?\)?[-\)\(]*\s?\d{1,4}[-\)\(]*\s?\d{1,4}[-\)\(]*\s?\d{1,4}[-\)\(]*\s?\d{1,6}[\)]?', data)
    joined_phones = [''.join(tups) for tups in match_phones]
    phones.extend(joined_phones)
    
    filtered_phones = [x for x in phones if not re.match('^[0-9]+$', x)]
    filtered_phones = [cleanup_phone(i) for i in filtered_phones]
    filtered_phones = [x for x in filtered_phones if x]
    return list(set(filtered_phones))

def cleanup_phone(string):
    clean_pattern = re.compile('[^0-9()+]|_')
    a = re.sub(clean_pattern, ' ', string)
    a = re.sub('(\(\s*\))', '', a)
    a = re.sub('\+ ', '+', a)
    return re.sub(' +', ' ', a).strip()
