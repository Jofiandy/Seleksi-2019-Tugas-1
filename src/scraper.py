from bs4 import BeautifulSoup
from requests import get
import wget
import datetime
import json


def get_manga_latest_chapter():
    # Get Latest Manga Chapter
    manga_name = input('Enter Manga Name:')
    try:
        manga_name = str(manga_name.replace(" ", "-").lower())
        url = 'http://mangafull.xyz/manga/' + manga_name
        response = get(url)
        url_html = BeautifulSoup(response.content, 'html.parser')
        manga_latest_html = url_html.find_all('div', class_='total-chapter')
        manga_latest_list = manga_latest_html[0].find_all('h4')
        for manga_chapter in manga_latest_list:
            print(manga_chapter.a.text + manga_chapter.span.text)
        return manga_name
    except Exception:
        raise Exception('Manga not Found')


def get_manga_chapter_images(manga_name):
    # Download Images for Particular Manga Chapter
    manga_chapter = input('Enter Chapter:')
    try:
        manga_name_with_chapter = str(
            manga_name + '/chapter-' + str(manga_chapter))
        url = 'http://mangafull.xyz/' + manga_name_with_chapter
        response = get(url)

        url_html = BeautifulSoup(response.content, "html.parser")

        chapter_pages = url_html.find_all(
            'div', class_='col-md-12 paddfixboth-mobile')
        chapter_images = chapter_pages[0].p.text.split(',')
        for image in chapter_images:
            wget.download(image, 'screenshots')
        return manga_chapter, chapter_images
    except Exception:
        raise Exception('Error')

if __name__ == '__main__':
    try:
        manga_name = get_manga_latest_chapter()
        manga_chapter, chapter_images = get_manga_chapter_images(manga_name)
        data = {}
        data['Name'] = manga_name
        data['Chapter'] = manga_chapter
        data['Time Downloaded'] = datetime.datetime.now().strftime('%d %b %Y (%H:%M:%S)')
        data['Images Downloaded'] = chapter_images
        with open('data/result.json', 'w') as f:
            json.dump(data, f)
    except Exception:
        raise Exception('Error')
