import requests
import bs4
import sys
import json

vimtips_url = 'http://zzapper.co.uk/vimtips.html'

response = requests.get(vimtips_url)
soup = bs4.BeautifulSoup(response.text, 'lxml')

if type(soup.pre) != bs4.element.Tag:
    print "Can't find pre Tag!"
    sys.exit()

# pre_tags = soup.select('pre')
# text = pre_tags[0].get_text()
text = soup.pre.get_text()
raw_lines = text.split('\n')

lines = []
for i, line in enumerate(raw_lines):
    items = line.split(' : ')

    if '----------' in line:
        lines.append({'line': '.' * 100})
        lines.append({'line': '.' * 100})
    else:
        lines.append({'line': line})

#json_str = json.dumps(lines, indent=4, separators=(',', ': '))
json_str = json.dumps(lines)

f = open('vimtips.json', 'w')
f.write(json_str)
f.close()
