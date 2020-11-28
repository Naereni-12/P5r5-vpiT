import pandas as pd
import pretty_html_table
import requests
import random
from bs4 import BeautifulSoup
from urllib3 import disable_warnings, exceptions
disable_warnings(exceptions.InsecureRequestWarning)

# you can change tokens from https://user-agents.net/random
fake_user_agent = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.103 YaBrowser/18.7.1.855 Yowser/2.5 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.103 YaBrowser/18.7.1.855 Yowser/2.5 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.42 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 OPR/55.0.2994.37',
'Mozilla/5.0 (Linux; Android 5.1; MI PAD 2 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.2; SM-T520 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.109 Safari/537.36',
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0E)',
'Mozilla/5.0 (Linux; Android 4.4.2; Air_Pro10 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.4; SM-G318H Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0E; .NET4.0C)',
'Puffin/15867 CFNetwork/758.5.3 Darwin/15.6.0',
'Mozilla/5.0 (iPad; CPU OS 11_4_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/55.0.2883.79 Mobile/15G77 Safari/602.1',
'Mozilla/5.0 (Linux; Android 7.1.1; General Mobile 4G Build/N0F27E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-J810F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; Lenovo TB-X304L Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 4 Build/OPM6.171019.030.H1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:38.9) Gecko/20100101 Goanna/2.1 Firefox/38.9 PaleMoon/26.3.3',
'Mozilla/5.0 (Linux; Android 7.1.1; SM-T380 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; ZTE BLADE A0622 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; N9560 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36']

class Recorder:
    def get_html(self, url):
        r = requests.get(url, verify=False, headers={
            'User-Agent': random.choice(fake_user_agent)})
        r.encoding = 'utf8'
        return r.text

    # this def write data in HTML table
    # with "pretty_html_table"
    # but you can choose any method of recording
    def write_result_file(self, data):
        with open(f"Your path", 'a') as file:
            df = pd.DataFrame.from_dict(data)
            file.write(pretty_html_table.build_table(df, 'grey_light'))


class Content:
    # Sample of adding a site for parsing

    def maybe_abbreviation_website(self):
        url = ''
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')

        # the most important part
        # write you html path
        date = soup.find('', class_='').find_all('')
        href = soup.find('', class_='').find_all('')
        head = soup.find('', class_='').find_all('')

        dates = ['']
        links = ['']
        heads = ['']
        for i in date:
            j = str(i).split('>')[1]
            dates.append(j.split('<')[0])
        for i in href:
            j = str(i).split('href="')[1]
            links.append('' + j.split('">')[0])
        for i in head:
            k = str(i).split('">')[1]
            heads.append(k.split('<')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)



if __name__ == "__main__":
    # Executive part of the code

    try:
        Content().maybe_abbreviation_website()
    except requests.exceptions.ConnectionError:
        print("\nRequestsError: Response error from the requested site\n")
    except FileNotFoundError:
        print('\nFileError: Failed to find the final path to save the report\n')
        print('Forced execution stop')
        raise SystemExit
