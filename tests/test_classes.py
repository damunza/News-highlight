import unittest
from app.models import Source,Article


class SourceTest(unittest.TestCase):
    '''
    testing the behaviour of source
    '''
    def setUp(self):
        '''
        method runs before each test
        '''
        self.new_source = Source('abc-news','ABC News', 'blabla blabla', 'en')

    def test_source_instance(self):
        '''
        testing whether the sources instantiate correctly
        '''
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        '''
        testing the instance created called new_source
        '''
        self.assertEqual(self.new_source.id, 'abc-news')
        self.assertEqual(self.new_source.name, 'ABC News')
        self.assertEqual(self.new_source.description, 'blabla blabla')
        self.assertEqual(self.new_source.language, 'en')

class ArticleTest(unittest.TestCase):
    '''
    testing the behaviour of article
    '''
    def setUp(self):
        '''
        runs before each test
        '''
        self.new_article = Article('a','b','c','d','e','f')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        testing whether the instances of article are started correctly
        '''
        self.assertEqual(self.new_article.author,'a')
        self.assertEqual(self.new_article.title, 'b')
        self.assertEqual(self.new_article.description, 'c')
        self.assertEqual(self.new_article.url, 'd')
        self.assertEqual(self.new_article.image, 'e')
        self.assertEqual(self.new_article.time, 'f')
