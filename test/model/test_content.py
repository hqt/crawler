import random
import unittest

from crawler.model.author import Author
from crawler.model.chapter import Chapter
from crawler.model.content import Content


class TestContent(unittest.TestCase):

    def test_create_and_get_content(self):
        name = str(random.randint(1, 1000))
        normalize_name = str(random.randint(1, 1000))
        description = str(random.randint(1, 1000))
        href = str(random.randint(1, 1000))

        author, is_success = Author.create_author(name, normalize_name, description, href)
        self.assertEqual(True, is_success)
        self.assertIsNotNone(author)

        chapter, is_success = Chapter.create_chapter(name, normalize_name, description, href, author.id)
        self.assertEqual(True, is_success)
        self.assertIsNotNone(chapter)

        data = str(random.randint(1, 1000))
        content, is_success = Content.create_content(data, href, chapter.id)
        self.assertEqual(True, is_success)
        self.assertIsNotNone(content)

        new_content = Content.get_content(content.id)
        self.assertEqual(new_content.data, data)
        self.assertEqual(new_content.href, href)
        self.assertEqual(new_content.chapter_id, chapter.id)

    def test_create_content_violate_foreign_key(self):
        content = str(random.randint(1, 1000))
        href = str(random.randint(1, 1000))

        content, is_success = Content.create_content(content, href, 9999)
        # self.assertFalse(is_success)
        self.assertIsNone(content)
