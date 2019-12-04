import requests
import datetime
from bs4 import BeautifulSoup
import os
import json


def parser_for_1_page(page=0, days=1):
    now = datetime.datetime.now()
    day = now.strftime("%d")
    days = [int(day)-i for i in range(days)]
    req = requests.get("http://www.niknews.mk.ua/novosti/skip/{}/".format(page*15))
    if req.status_code == 200:
        sp = BeautifulSoup(req.text, 'html.parser')
        start = sp.find("ul", class_="items")
        all_links = start.find_all("li")
        for link in all_links:
            a = link.find("a").attrs.get("href")
            if a:
                b = a.split("/")
                if int(b[3]) in days:
                    yield a
                else:
                    break


def news_to_dict_parser(link):
    dict1 = {}
    page = requests.get("http://www.niknews.mk.ua{}".format(link))
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        news_id = link.split("/")[-2]
        dict1['source'] = link
        dict1['id'] = news_id
        dict1['title'] = soup.find("h1", class_=None).text.strip()
        dict1['news_date'] = soup.find("time").text.strip()
        text = soup.find("div", class_="col-main")
        group_text = text.find_all("p")
        strtext = ""
        for i in group_text:
            strtext += i.text + " "
        dict1['fulltext'] = strtext
        image_folder = soup.find("aside")
        all_imgs = image_folder.find_all("img")
        for i in range(len(all_imgs)):
            all_imgs[i] = all_imgs[i].attrs.get("src")
        for i in range(len(all_imgs)):
            all_imgs[i] = str("http://www.niknews.mk.ua") + str(all_imgs[i])
        dict1["imgs"] = all_imgs
    return dict1


def current_day_news(days):
    bbb = {}
    counter1 = 1

    def inside(days, counter_fd, i=0):
        counter = 0
        for link in parser_for_1_page(i, days):
            a = news_to_dict_parser(link)
            bbb[counter_fd] = a
            counter += 1
            counter_fd += 1
        if counter == 15:  # 15 - максимальное количество новостей на странице
            i += 1
            inside(days, counter_fd, i)
    inside(days, counter1)

    return bbb


if __name__ == "__main__":
    a = current_day_news(2)
    # with open("file.json", "a+", encoding='utf-8') as f1:
    #     json.dump(a, f1, ensure_ascii=False)