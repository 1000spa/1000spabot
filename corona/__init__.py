import requests
import bs4

def call():
    res = requests.get('https://coronamap.site/')
    soup = BeautifulSoup(res.content, 'html.parser')
    data1 = soup.findAll('div', 'content')
    data2 = soup.findAll('div', 'content1 clear')

    data1_list = []
    data2_list = []
    for item in data1:
        data1_list.append(item.get_text().replace('\n', '').replace(' ', ''))
    for item in data2:
        data2_list.append(item.get_text().replace('\n', '').replace(' ', ''))

    confirmedPatient = data1_list[0]
    suspectedPatient = data1_list[1]

    x = data2_list[0].find('사망')
    curedPatient = data2_list[0][2:4]
    diedPatient = data2_list[0][x + 2:]
