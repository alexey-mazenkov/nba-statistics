#

import urllib.request as ur


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
    COMP = float(stats[0].replace(',', ''))
    ATT = float(stats[1].replace(',', ''))
    YDS = float(stats[3].replace(',', ''))
    TD = float(stats[5].replace(',', ''))
    INT = float(stats[6].replace(',', ''))
    a = (COMP / ATT - 0.3) * 5
    b = (YDS / ATT - 3) * 0.25
    c = (TD / ATT) * 20
    d = 2.375 - (INT / ATT * 25)
    PR = format((((a + b + c + d) / 6) * 100), '.2f')

    return ATT, COMP, YDS, TD, INT, PR


def output(name, ATT, COMP, YDS, TD, INT, PR):
    all_stats = [name, ATT, COMP, YDS, TD, INT, PR]
    with open('output.txt', 'a') as outp:
        for i in range(len(all_stats)):
            if i == 0:
                outp.write('Player name: ')
            elif i == 1:
                outp.write('Number of passing attempts: ')
            elif i == 2:
                outp.write('Number of completions: ')
            elif i == 3:
                outp.write('Passing yards: ')
            elif i == 4:
                outp.write('Touchdown passes: ')
            elif i == 5:
                outp.write('Interceptions: ')
            else:
                outp.write('Passer rating: ')
            outp.write(str(all_stats[i]) + '\n')


def main():
    
    with open('players.txt', 'r') as players:
        for i in players:
            address = players.readline()

            print(parse_name(get_page(address)))
            print(stats(parse_stat(get_page(address))))


main()
