#@Am_Robots **<---FINAL STEP**
import time
import requests
import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urlparse


url = "https://gplinks.co/j0f4K"
# ==============================================

def gplinks_bypass(url):
    scraper = cloudscraper.create_scraper(allow_brotli=False)
    res = scraper.get(url)
    
    h = { "referer": res.url }
    res = scraper.get(url, headers=h)
    
    bs4 = BeautifulSoup(res.content, 'lxml')
    inputs = bs4.find_all('input')
    data = { input.get('name'): input.get('value') for input in inputs }

    h = {
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
    }
    
    time.sleep(5) # !important
    
    p = urlparse(url)
    final_url = f'{p.scheme}://{p.netloc}/links/go'
    res = scraper.post(final_url, data=data, headers=h).json()

    return res

# ==============================================

print(gplinks_bypass(url))

# ==============================================

f'''
SAMPLE OUTPUT:
{
    'Status': 'Bypassed', 
    'Info': 'XXXXXX', 
    'Bypassed URL': 'XXXX' (Bypassed URL)
}
'''
