from urlparse import urlparse
import scrapy
from scrapy import Selector
from scrapy_splash import SplashRequest

from crawler.enums.parse_type import ParseType
from crawler.utils.file import create_directory, is_file_existed
from crawler.utils.string import normalize


def get_chapter_path(book_path, chapter_name):
    return book_path + '/' + chapter_name + '.txt'


def get_domain(url):
    parsed_uri = urlparse(url)
    result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return result


author_urls = [
    {'name': 'nguyen_nhat_anh', 'url': 'http://sstruyen.com/doc-truyen/tac-gia/nguyen-nhat-anh.html'},
]

book_urls = [
    {'name': 'con_chut_gi_de_nho', 'url': 'http://sstruyen.com/doc-truyen/con-chut-gi-de-nho/10784.html'},
    {'name': 'bo_cau_khong_dua_thu', 'url': 'http://sstruyen.com/doc-truyen/bo-cau-khong-dua-thu/2636.html'},
]


class SSTruyenSpider(scrapy.Spider):
    name = "ss"

    parse_type = ParseType.AUTHOR
    debug = True

    def start_requests(self):
        if self.parse_type == ParseType.AUTHOR:
            fn = self.crawl_authors_job
        elif self.parse_type == ParseType.BOOK:
            fn = self.crawl_books_job
        elif self.parse_type == ParseType.CHAPTER:
            pass

        data = fn()
        for value in data:
            yield value

    def parse(self, response):
        pass

    def crawl_authors_job(self):
        for url_info in author_urls:
            author_directory = 'data' + '/' + url_info['name']
            create_directory(author_directory)
            yield SplashRequest(
                url_info['url'],
                self.parse_author_cb,
                args={
                    'wait': 1,
                },
                meta={
                    'book_name': url_info['name'],
                    'current_directory': author_directory,
                }
            )

    def crawl_books_job(self):
        for url_info in author_urls:
            author_directory = 'data' + '/' + url_info['name']
            create_directory(author_directory)
            yield SplashRequest(
                url_info['url'],
                self.parse_author_cb,
                args={
                    'wait': 1,
                },
                meta={
                    'book_name': url_info['name'],
                    'book_directory': author_directory,
                }
            )

    def parse_author_cb(self, response):
        authors = self.parse_author_info(response)

        filename = '/books.txt'
        f = open(response.meta['current_directory'] + filename, "w+")
        domain = get_domain(response.url)

        for author in authors:
            f.write(author['title'] + "\n")
            f.write(author['href'] + "\n")

            directory = response.meta['current_directory'] + '/' + author['title']
            yield SplashRequest(
                domain + author['href'],
                self.parse_book_cb,
                args={
                    'wait': 1,
                },
                meta={
                    'current_directory': directory,
                }
            )

            if self.debug:
                break

        f.close()

    def parse_author_info(self, response):
        author_nodes = Selector(text=response.body).css('.storyinfo .listTitle')
        authors = []
        for author_node in author_nodes:
            href = author_node.css('::attr(href)').get()
            title = author_node.css('::attr(title)').get()
            authors.append({
                'title': normalize(title),
                'href': normalize(href),
            })

        return authors

    def parse_book_cb(self, response):
        books = self.parse_book_info(response)
        domain = get_domain(response.url)

        create_directory(response.meta['current_directory'])
        filename = '/chapter.txt'
        f = open(response.meta['current_directory'] + filename, "w+")

        for book in books:
            f.write(book['chapter_name'] + "\n")
            f.write(book['href'] + "\n")

            yield SplashRequest(
                domain + book['href'],
                self.parse_chapter_cb,
                args={
                    'wait': 1,
                },
                meta={
                    'current_directory': response.meta['current_directory'],
                    'chapter_name': book['chapter_name'],
                }
            )

            if self.debug:
                break

        f.close()

    def parse_book_info(self, response):
        books = []
        chapter_nodes = Selector(text=response.body).css('.chuongmoi  a')
        for chapter_node in chapter_nodes:
            chapter_name = chapter_node.css('::attr(title)').get()
            href = chapter_node.css('::attr(href)').get()
            books.append({
                'chapter_name': normalize(chapter_name),
                'href': normalize(href),
            })
        return books

    def parse_chapter_cb(self, response):
        content = Selector(text=response.body).css('#chapt-content div').get()
        content = normalize(content)
        chapter_path = get_chapter_path(response.meta['current_directory'], response.meta['chapter_name'])
        with open(chapter_path, 'w+') as f:
            f.write(content)
