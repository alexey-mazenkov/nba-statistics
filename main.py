# kek

import urllib.request as ur

url = 'http://www.nfl.com/player/brycepetty/2552369/profile'


f = ur.urlopen(url)
s = f.read()
text = str(s)
part_name = text.find('TOTAL')

name = text[text.find('>', part_name) + 1:text.find('</tr>', part_name)]
name = name.replace('n', '')
name = name.replace('t', '')
name = name.replace('d', '')
name = name.replace('<', '')
name = name.replace('>', '')
name = name.replace('/', ' ')
name = name.replace('\\', '')
name = name.replace(',', '')
name = name.split()

COMP = name[0]
ATT = name[1]
YDS = name[3]
TD = name[5]
INT = name[6]
print(COMP, ATT, YDS, TD, INT)
