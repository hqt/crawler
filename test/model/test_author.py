import random
import unittest

from crawler.model.author import Author


class TestAuthor(unittest.TestCase):

    def test_create_and_get_author(self):
        name = str(random.randint(1, 100))
        normalize_name = str(random.randint(1, 100))
        description = str(random.randint(1, 100))
        href = str(random.randint(1, 100))

        author, is_success = Author.create_author(name, normalize_name, description, href)
        self.assertEqual(True, is_success)
        self.assertIsNotNone(author)

        new_author = Author.get_author(author.id)
        self.assertEqual(new_author.name, name)
        self.assertEqual(new_author.normalize_name, normalize_name)
        self.assertEqual(new_author.description, description)
        self.assertEqual(new_author.href, href)

    def test_create_author_violate_unique_key(self):
        name = str(random.randint(1, 100))
        normalize_name = str(random.randint(1, 100))
        description = str(random.randint(1, 100))
        href = str(random.randint(1, 100))

        author, is_success = Author.create_author(name, normalize_name, description, href)
        self.assertEqual(True, is_success)
        self.assertIsNotNone(author)

        author, is_success = Author.create_author(name, normalize_name, description, href)
        self.assertFalse(is_success)
        self.assertIsNone(author)
