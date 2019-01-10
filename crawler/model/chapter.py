from sqlalchemy import Column, Integer, String, Text

from crawler.model import AlchemyBase
from crawler.utils.database import Session


class Chapter(AlchemyBase):
    __tablename__ = 'chapters'

    id = Column(Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    normalize_name = Column('normalize_name', String, nullable=False)
    description = Column('description', Text, nullable=True)
    href = Column('href', String, nullable=False)
    author_id = Column('author_id', Integer, nullable=False)

    def __init__(self, name, normalize_name, description, href, author_id):
        self.name = name
        self.normalize_name = normalize_name
        self.description = description
        self.href = href
        self.author_id = author_id

    def __repr__(self):
        return "<Chapter(name='%s', normalize_name='%s', description='%s', href='%s', author_id='%s')>" \
               % (self.name, self.normalize_name, self.description, self.href, self.author_id)

    @staticmethod
    def get_chapter(chapter_id):
        """
        Get chapter model. (Also SQLAlchemy object)
        :param chapter_id: database id
        :return: author object
        """
        author = Session.query(Chapter).filter_by(id=chapter_id).first()
        return author

    @staticmethod
    def create_chapter(name, normalize_name, description, href, author_id):
        """
        Create chapter model
        :return: object itself and boolean value
                True for success, exception will be None. False otherwise.
        """
        try:
            chapter = Chapter(name, normalize_name, description, href, author_id)
            Session.add(chapter)
            Session.commit()
            return chapter, True
        except Exception as e:
            Session.rollback()
            print(e)
            return None, False
