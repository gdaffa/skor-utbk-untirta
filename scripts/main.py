import os
import sys
import scrap

URL = sys.argv[1]
CURRENT_YEAR = sys.argv[2]

headers = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
   'Accept-Language': 'en,id;q=0.9,en-US;q=0.8,ms;q=0.7',
   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
   'Referer': 'https://www.google.com',
   'Connection': 'keep-alive',
   'Upgrade-Insecure-Requests': '1',
   'Sec-Ch-Ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
   'Sec-Ch-Ua-Mobile': '?0',
   'Sec-Ch-Ua-Platform': '"Linux"',
   'Sec-Fetch-Dest': 'document',
   'Sec-Fetch-Mode': 'navigate',
   'Sec-Fetch-Site': 'none',
   'Sec-Fetch-User': '?1',
}

def main():
   os.makedirs(f'../data/{CURRENT_YEAR}', exist_ok=True)
   file = open(f'../data/{CURRENT_YEAR}/utbk-{CURRENT_YEAR}.csv', 'w')

   content = scrap.get_content(URL, headers)
   parser  = scrap.parse_content(content)
   scrap.write_table(file, parser)

   file.close()

if __name__ == '__main__':
   main()