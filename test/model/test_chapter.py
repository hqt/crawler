import random
import unittest

from crawler.model.author import Author
from crawler.model.chapter import Chapter


class TestChapter(unittest.TestCase):

    def test_create_and_get_chapter(self):
        name = str(random.randint(1, 100))
        normalize_name = str(random.randint(1, 100))
        description = str(random.randint(1, 100))
        href = str(random.randint(1, 100))

        author, is_success = Author.create_author(name, normalize_name, description, href)
        self.assertEqual(True, is_success)
        self.assertIsNotNone(author)

        chapter, is_success = Chapter.create_chapter(name, normalize_name, description, href, author.id)

        new_chapter = Chapter.get_chapter(chapter.id)
        self.assertEqual(new_chapter.name, name)
        self.assertEqual(new_chapter.normalize_name, normalize_name)
        self.assertEqual(new_chapter.description, description)
        self.assertEqual(new_chapter.href, href)

    def test_create_chapter_violate_foreign_key(self):
        name = str(random.randint(1, 100))
        normalize_name = str(random.randint(1, 100))
        description = str(random.randint(1, 100))
        href = str(random.randint(1, 100))

        chapter, is_success = Chapter.create_chapter(name, normalize_name, description, href, 9999)
        self.assertFalse(is_success)
        self.assertIsNone(chapter)
