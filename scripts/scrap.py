import requests
from bs4 import BeautifulSoup

def get_content(url, headers):
   response = requests.get(url, headers=headers)
   content = response.content.decode()
   return content

def parse_content(content):
   return BeautifulSoup(content, 'html.parser')

def write_table(file, parser):
   table_rows = parser.select_one('table').select('tr')

   for table_row in table_rows:
      table_data = table_row.select('th,td')
      table_data = [td.get_text().strip() for td in table_data]
      file.write(';'.join(table_data) + '\n')