import pandas
from time import sleep
import re
from bs4 import BeautifulSoup as bs
import requests

class Maoyan:
    url = 'https://maoyan.com/films?showType=3'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36hi'
    cookies = '__mta=176608922.1597632903839.1597922990182.1597934907124.45; uuid_n_v=v1; uuid=0B849BF0E03511EABADBF5D4F95847E7CCA4DD73CBDB44599E704D9CBB3B4CC1; _lxsdk_cuid=173fa57775bc8-098fb41f4d3c05-31657301-1fa400-173fa57775bc8; _lxsdk=0B849BF0E03511EABADBF5D4F95847E7CCA4DD73CBDB44599E704D9CBB3B4CC1; mojo-uuid=cd8d1354e7b864ff6d9c87fbe9a24c56; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _csrf=71bb420d086a3d4e0ee0078415a835910d55e0db3003192d2359a8d2b1ed9905; mojo-session-id={"id":"824d6316fbfa5ccbb4f799588b0820eb","time":1597967185857}; mojo-trace-id=1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1597729928,1597817974,1597921463,1597967186; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1597967186; __mta=176608922.1597632903839.1597934907124.1597967186639.46; _lxsdk_s=1740e44380d-443-125-c55%7C%7C2'
    header = {
        'User-Agent': user_agent,
        'cookie':cookies
    }

    #获取所有电影的url
    def maoyan_movie_url(self):
        re = requests.get(self.url, headers=self.header)
        print(re.status_code)
        movies = bs(re.text, 'html.parser')
        movies_list = []
        for urls in movies.find_all('div', attrs={'class': 'movie-item film-channel'}):
            for url in urls.find_all('a'):
                movie_url = 'https://maoyan.com' + url.get('href')
                movies_list.append(movie_url)
        return movies_list

    #取出前10个url，并解析电影内容
    def top_10(self):
        url_lists = self.maoyan_movie_url()
        movies_list_1 = []
        for i in range(10):
            res = requests.get(url_lists[i*2], headers=self.header)
            print(res.status_code)
            movies_1 = bs(res.text, 'html.parser')
            movies_2 = {}
            for urls in movies_1.find_all('div', attrs={'class': 'movie-brief-container'}):
                movies_2['film_name'] = urls.find('h1').text
                movies_2['film_type'] = re.sub('\s+','',urls.find('li').text)
                movies_2['film_date'] = urls.find_all('li',limit=3)[2].text
            movies_list_1.append(movies_2)
            print(movies_list_1)
            sleep(1)


        return movies_list_1


if __name__ == '__main__':
    maoyan = Maoyan()
    # print(maoyan.maoyan_movie_url())
    movie_dict = pandas.DataFrame(data=maoyan.top_10())
    movie_dict.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)