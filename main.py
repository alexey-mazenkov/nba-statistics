# kek

import urllib.request as ur

address = 'http://www.nfl.com/player/brycepetty/2552369/profile'


def get_page(url):
    f = ur.urlopen(url)
    return f.read()


def parse_name(page):
    text = str(page)
    part_name = text.find("player-name")
    name = text[text.find('>', part_name) + 1:text.find('&', part_name)]
    return name


def parse_stat(page):
    text = str(page)
    part_name = text.find('TOTAL')
    stat = text[text.find('>', part_name) + 1:text.find('</tr>', part_name)]
    stat = stat.replace('\\t', '').replace('\\n', '').replace('<td>', '').replace('</td>', ' ')
    return stat.split()


def stats(stats):
    COMP = stats[0]
    ATT = stats[1]
    YDS = stats[3].replace(',', '')
    TD = stats[5]
    INT = stats[6]
    a = (COMP / ATT - 0.3) * 5
    b = (YDS / ATT - 3) * 0.25
    c = (TD / ATT) * 20
    d = 2.375 - (INT / ATT * 25)
    passer_rating = ((a + b + c + d) / 6) * 100

    print(COMP, ATT, YDS, TD, INT, passer_rating)


def main():

    print(parse_name(get_page(address)))
    stats(parse_stat(get_page(address)))


main()
