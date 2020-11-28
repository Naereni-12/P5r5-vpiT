import os
import datetime as dt
from random import choice
from time import sleep

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
from pretty_html_table import build_table
from urllib3 import disable_warnings, exceptions

print('''Запуск программы...
Подготовка системных настроек
''')


disable_warnings(exceptions.InsecureRequestWarning)


class Recorder:
    @staticmethod
    def get_html(url):
        fake_user_agent = [
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.103 YaBrowser/18.7.1.855 Yowser/2.5 Safari/537.36',
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
        r = requests.get(url, verify=False, headers={
            'User-Agent': choice(fake_user_agent)})
        r.encoding = 'utf8'
        return r.text

    @staticmethod
    def write_result_file(data):
        print("Происходит запись скачанных и обработанных данных в файл")
        def today_date():
            raw_date = dt.datetime.utcnow() + dt.timedelta(hours=3)
            msk_time = raw_date.strftime("%D в %H")
            list_date = str(msk_time).split('/')
            today_date_res = '_'.join(list_date)
            return today_date_res
        
        if not os.path.isdir("D:/!Агрегатор новостей"):
            os.mkdir("D:/!Агрегатор новостей")

        with open(f"D:/!Агрегатор новостей/Отчёт по новостям от {today_date()}.00.html", 'a') as file:
            df = DataFrame.from_dict(data)
            file.write(build_table(df, 'grey_light'))


class Content:
    # Лекало добавления
    # def ():
    #     url = ''
    #     print(f"Проходит скачивание данных с сайта {url}")
    #     soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
    #     date = soup.find('', class_='').find_all('')
    #     href = soup.find('', class_='').find_all('')
    #     head = soup.find('', class_='').find_all('')
    #     dates = ['']
    #     links = ['']
    #     heads = ['']
    #     for i in date:
    #         j = str(i).split('>')[1]
    #         dates.append(j.split('<')[0])
    #     for i in href:
    #         j = str(i).split('href="')[1]
    #         links.append('' + j.split('">')[0])
    #     for i in head:
    #         k = str(i).split('">')[1]
    #         heads.append(k.split('<')[0])
    #     res = dates, links, heads
    #     Recorder().write_result_file(res)

    # Ставропольский аграрный
    def StGAU(self):
        url = 'http://www.stgau.ru/news/'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find('div', class_='col-xs-12 col-sm-8 col-md-9 col-lg-9 cont').find_all('div',
                                                                                             class_='news-line-date')
        head = soup.find('div', class_='col-xs-12 col-sm-8 col-md-9 col-lg-9 cont').find_all('div',
                                                                                             class_='news-line-title')
        dates = ['']
        # универ в ссылках, для обозначения принадлежности таблицы
        links = ['Ставропольский аграрный университет']
        heads = ['']
        for i in date:
            j = str(i).split('>')[1]
            dates.append(j.split('<')[0])
        for i in head:
            j = str(i).split('href="')[1]
            links.append('http://www.stgau.ru/' + j.split('">')[0])
            k = j.split('">')[1]
            heads.append(k.split('<')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    # Северо-кавказкий федеральный уник
    def SСFU(self):
        url = 'https://www.ncfu.ru/home/index1.html'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find('div', class_='news').find_all(
            'p', class_='news__date')
        href = soup.find('div', class_='news').find_all(
            'a', class_='news__item')
        head = soup.find('div', class_='news').find_all(
            'p', class_='news-text')
        dates = ['']
        links = ['Северо-Кавказский федеральный университет']
        heads = ['']
        for i in date:
            j = str(i).split('>')[1]
            dates.append(j.split('<')[0])
        for i in href:
            j = str(i).split('href="')[1]
            links.append('https://www.ncfu.ru' + j.split('">')[0])
        for i in head:
            k = str(i).split('">')[1]
            heads.append(k.split('<')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    # Кабарданский гос уник
    def KBSU(self):
        url = 'https://kbsu.ru/news/'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find('ul', class_='category-list__list').find_all('p',
                                                                      class_='category-list__item__date')
        href = soup.find('ul', class_='category-list__list').find_all('a',
                                                                      class_='category-list__item__title hyphenate')
        head = soup.find('ul', class_='category-list__list').find_all('a',
                                                                      class_='category-list__item__title hyphenate')
        dates = ['']
        links = ['Кабардино-Балкарский государственный университет']
        heads = ['']
        for i in date:
            j = str(i).split('>')[1]
            dates.append(j.split('<')[0])
        for i in href:
            j = str(i).split('href="')[1]
            links.append('https://kbsu.ru/news/' + j.split('">')[0])
        for i in head:
            k = str(i).split('">')[1]
            heads.append(k.split('<')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def KGNCRAN(self):
        url = 'http://www.kbncran.ru/'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find(
            'div', class_='column span-8').find_all('span', class_='meta-item meta-date')
        href = soup.find(
            'div', class_='column span-8').find_all('h1', class_='heading')
        head = soup.find(
            'div', class_='column span-8').find_all('h1', class_='heading')
        dates = ['']
        links = ['Кабардино-Балкарский научный центр РАН']
        heads = ['']
        for i in date:
            j = str(i).split('</i> ')[1]
            dates.append(j.split('</span>')[0])
        for i in href:
            j = str(i).split('href="')[1]
            links.append(j.split('">')[0])
        for i in head:
            k = str(i).split('/">')[1]
            heads.append(k.split('</a>')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def NCSA(self):
        url = 'http://ncsa.ru/page/content/novosti.html'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find('div', class_='col-sm-8').find_all('p')
        href = soup.find('div', class_='col-sm-8').find_all('h5')
        head = soup.find('div', class_='col-sm-8').find_all('h5')
        dates = ['']
        links = ['Северо-Кавказская государственная академия']
        heads = ['']
        for i in date:
            j = str(i).split(' | ')[1]
            dates.append(j.split('  |')[0])
        for i in href:
            j = 'http://ncsa.ru' + str(i).split('href="')[1]
            links.append(j.split('">')[0])
        for i in head:
            k = str(i).split('">')[1]
            heads.append(k.split('</a>')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def SKQMI(self):
        url = 'http://www.skgmi-gtu.ru/ru-ru/news'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find('div', class_='edn_690_article_list_wrapper').find_all(
            'div', class_='date_box')
        href = soup.find('div', class_='edn_690_article_list_wrapper').find_all(
            'h1', class_='title')
        head = soup.find('div', class_='edn_690_article_list_wrapper').find_all(
            'h1', class_='title')
        dates = ['']
        links = ['Северо-Кавказский горно-металлургический институт']
        heads = ['']
        for i in date:
            j = str(i).split('<p>')[1]
            dates.append(j.split('</p>')[0])
        for i in href:
            j = '' + str(i).split('href="')[1]
            links.append(j.split('" ')[0])
        for i in head:
            k = str(i).split('target="_self">')[1]
            heads.append(k.split('</a>')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def VNСRAN(self):
        url = 'http://vncran.ru/ru/press-center/news/'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find('div', class_='sf-viewbox position-relative').find_all('p',
                                                                                class_='t--1 c-text-secondary mb-2')
        href = soup.find('div', class_='sf-viewbox position-relative').find_all('h3',
                                                                                class_='t-1 my-2 t-title с-text-primary l-inherit l-hover-primary l-hover-underline-none transition')
        head = soup.find('div', class_='sf-viewbox position-relative').find_all('h3',
                                                                                class_='t-1 my-2 t-title с-text-primary l-inherit l-hover-primary l-hover-underline-none transition')
        dates = ['']
        links = ['Владикавказский научный центр РАН']
        heads = ['']
        for i in date:
            j = str(i).split('</i>')[1]
            dates.append(j.split(', ')[0])
        for i in href:
            j = '' + str(i).split('href="')[1]
            links.append('http://vncran.ru' + (j.split('">')[0]))
        for i in head:
            k = str(i).split('/">')[1]
            heads.append(k.split('</a>')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def NOSU(self):
        url = 'http://www.nosu.ru/'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find(
            'div', class_='news-list current').find_all('div', class_='date')
        href = soup.find(
            'div', class_='news-list current').find_all('div', class_='title')
        head = soup.find(
            'div', class_='news-list current').find_all('div', class_='title')
        dates = ['']
        links = ['Северо-Осетинский государственный университет']
        heads = ['']
        for i in date:
            j = str(i).split('">')[1]
            dates.append(j.split('</')[0])
        for i in href:
            j = '' + str(i).split('href="')[1]
            links.append(j.split('">')[0])
        for i in head:
            k = str(i).split('/">')[1]
            heads.append(k.split('</a>')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def SOQPI(self):
        url = 'https://sogpi.org/ru/news'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find('div', class_='edn_414_article_list_wrapper').find_all(
            'div', class_='meta_text')
        href = soup.find(
            'div', class_='edn_414_article_list_wrapper').find_all('h1')
        head = soup.find(
            'div', class_='edn_414_article_list_wrapper').find_all('h1')
        dates = ['']
        links = ['Северо-Осетинский государственный педагогический институт']
        heads = ['']
        for i in date:
            j = str(i).split('>')[1]
            dates.append(j.split('<')[0])
        for i in href:
            j = str(i).split('href="')[1]
            links.append('' + j.split('" target="_self')[0])
        for i in head:
            k = str(i).split('">')[1]
            heads.append(k.split('<')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def INQQU(self):
        url = 'http://inggu.ru/about_the_university/news/'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find(
            'div', class_='news-list').find_all('div', class_='news-item-date')
        href = soup.find('div', class_='news-list').find_all('h3',
                                                             class_='news-item-header')
        head = soup.find('div', class_='news-list').find_all('h3',
                                                             class_='news-item-header')
        dates = ['']
        links = ['Ингушский государственный университет']
        heads = ['']
        for i in date:
            j = str(i).split('>')[1]
            dates.append(j.split('<')[0])
        for i in href:
            j = str(i).split('href="')[1]
            links.append('http://inggu.ru' + j.split('">')[0])
        for i in head:
            k = str(i).split('/">')[1]
            heads.append(k.split('</a>')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def KCHGU(self):
        url = 'http://kchgu.ru/'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find('div', id="content").find_all('span', class_='onDate')
        href = soup.find('div', id="content").find_all(
            'h2', class_='entry-title')
        head = soup.find('div', id="content").find_all(
            'h2', class_='entry-title')
        dates = ['']
        links = ['Карачаево-Черкесский государственный университет']
        heads = ['']
        for i in date:
            j = str(i).split('rel="bookmark">')[1]
            dates.append(j.split(' - ')[0])
        for i in href:
            j = str(i).split('href="')[1]
            links.append('' + j.split('" rel')[0])
        for i in head:
            k = str(i).split('Permalink to ')[1]
            heads.append(k.split('">')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def DSTU(self):
        url = 'http://dstu.ru/'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find(
            'div', class_='news-list-container').find_all('span', class_='news-list-date')
        href = soup.find('div', class_='news-list-container').find_all('a')
        head = soup.find('div', class_='news-list-container').find_all('a')
        dates = ['']
        links = ['Дагестанский государственный технический университет']
        heads = ['']
        for i in date:
            j = str(i).split('>')[1]
            dates.append(j.split('<')[0])
        for i in href:
            j = str(i).split('href="')[1]
            links.append('http://dstu.ru/' + j.split('title="')[0])
        for i in head:
            k = str(i).split('title="')[1]
            heads.append(k.split('">')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def DNCRAN(self):
        url = 'http://www.dncran.ru/News'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        href = soup.find('div', class_='contentblock').find_all(
            'a', class_='newshead')
        head = soup.find('div', class_='contentblock').find_all(
            'a', class_='newshead')
        links = ['Дагестанский федеральный исследовательский центр РАН']
        heads = ['']
        for i in href:
            j = str(i).split('href="')[1]
            links.append('http://www.dncran.ru' + j.split('">')[0])
        for i in head:
            t = str(i).split('">')[1]
            w = t.split('\n<span>')
            q = ''.join(w)
            k = q.split('</span>')
            del k[-1]
            k = ''.join(k)
            heads.append(k)
        res = links, heads
        Recorder().write_result_file(res)

    def PGU(self):
        url = 'https://pgu.ru/'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find(
            'div', class_='news-list').find_all('span', class_='news-date-time')
        href = soup.find(
            'div', class_='news-list').find_all('li', class_='newscontent')
        head = soup.find(
            'div', class_='news-list').find_all('li', class_='newscontent')
        dates = ['']
        links = ['Пятигорский государственный университет']
        heads = ['']
        for i in date:
            j = str(i).split('>')[1]
            dates.append(j.split('<')[0])
        for i in href:
            j = str(i).split('href="')[1]
            links.append('https://pgu.ru' + j.split('">')[0])
        for i in head:
            k = str(i).split('<b>')[1]
            k = k.split('</b>')[0]
            k = k.split('\t\t\t\t\t\t\t\t\t\t\t\t\t')[1]
            k = k.split('\t\t\t\t\t\t\t\t\t\t\t')[0]
            heads.append(k)
        res = dates, links, heads
        Recorder().write_result_file(res)

    def GORSKIGAU(self):
        url = 'https://gorskigau.com/О-ВУЗе'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        href = soup.find(
            'div', id='dnn_ctr476_ViewEasyDNNNewsMain_ctl00_pnlListArticles').find_all('h2')
        head = soup.find(
            'div', id='dnn_ctr476_ViewEasyDNNNewsMain_ctl00_pnlListArticles').find_all('h2')
        links = ['Горский государственный аграрный университет']
        heads = ['']
        for i in href:
            j = str(i).split('href="')[1]
            links.append('' + j.split('">')[0])
        for i in head:
            k = str(i).split('">')[1]
            heads.append(k.split('<')[0])
        res = links, heads
        Recorder().write_result_file(res)

    def DGU(self):
        url = 'http://www.dgu.ru/'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find('td', valign="top").find_all(
            'span', class_='createdate')
        href = soup.find('td', valign="top").find_all(
            'h2', class_='contentheading')
        head = soup.find('td', valign="top").find_all(
            'h2', class_='contentheading')
        dates = ['']
        links = ['Дагестанский государственный университет']
        heads = ['']
        for i in date:
            j = str(i).split(' ')[1]
            dates.append(j.split('\n\t\t')[1])
        for i in href:
            j = str(i).split('href="')[1]
            links.append('http://www.dgu.ru/' + j.split('">')[0])
        for i in head:
            k = str(i).split('.html">')[1]
            k = k.split('	</a>')[0]
            heads.append(k.split('\n\t\t')[1])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def CHESU(self):
        url = 'https://www.chesu.ru/news'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        date = soup.find(
            'div', class_='ma-blog-list').find_all('div', class_='ma-blog-date')
        href = soup.find(
            'div', class_='ma-blog-list').find_all('h5', class_='ma-blog-title')
        head = soup.find(
            'div', class_='ma-blog-list').find_all('h5', class_='ma-blog-title')
        dates = ['']
        links = ['Чеченский государственный университет']
        heads = ['']
        for i in date:
            j = str(i).split('>')[1]
            dates.append(j.split(' в ')[0])
        for i in href:
            j = str(i).split('href="')[1]
            links.append('https://www.chesu.ru' + j.split('">')[0])
        for i in head:
            k = str(i).split('">')[2]
            heads.append(k.split('</a>')[0])
        res = dates, links, heads
        Recorder().write_result_file(res)

    def GSTOU(self):
        url = 'https://gstou.ru/news.php'
        print(f"Проходит скачивание данных с сайта {url}")
        soup = BeautifulSoup(Recorder().get_html(url), 'lxml')
        href = soup.find('div', class_='news_all_block').find_all('a')
        head = soup.find('div', class_='news_all_block').find_all('h4')
        links = ['Грозненский государственный нефтяной технический университет']
        heads = ['']
        for i in href:
            j = str(i).split('href="')[1]
            links.append('https://gstou.ru/' + j.split('">')[0])
        for i in head:
            k = str(i).split('<h4>')[1]
            heads.append(k.split('</h4>')[0])
        res = links[::2], heads
        Recorder().write_result_file(res)


if __name__ == "__main__":
    # Такая конструкция сделана для тех случаев,
    # когда на сайт одного из вузов ложится,
    # но при этом итоговый отчёт всё-таки сформировывается

    Content = Content()

    try:
        Content.SСFU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')
    except FileNotFoundError:
        print('\nFileError: Не найден конченый путь сохранения отчёта\n')
        print('Принудительная остановка выполнения')
        sleep(2)
        raise SystemExit

    try:
        Content.StGAU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.PGU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.KBSU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.KGNCRAN()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.SKQMI()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.VNСRAN()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.NOSU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.GORSKIGAU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.SOQPI()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.DGU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.DSTU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.DNCRAN()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.KCHGU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.NCSA()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.INQQU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.CHESU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')

    try:
        Content.GSTOU()
    except requests.exceptions.ConnectionError:
        print("\nFatalError: Ошибка ответа от запрошенного сайта\n")
        sleep(2)
    except AttributeError:
        print('\nContentError: Владельцы изменили структуру сайта, для устронения проблемы обратитесь к Эдуарду\n')
    except UnicodeEncodeError:
        print('\nUnicodeEncodeError: В какой-то из статей присутствует буква "ё" (невозможно заскодировать)\n')
        sleep(3)  # ожидание 2сек, чтобы пользователь увидел ошибку

    print("\nПроверяется правильность записанных файлов")
    print("Парсинг прошёл успешно")
    print('Для завершения работы закройте программу')
    while True:
        pass
