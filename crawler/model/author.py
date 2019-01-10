from sqlalchemy import Column, Integer, String, Text

from crawler.model import AlchemyBase
from crawler.utils.database import Session


class Author(AlchemyBase):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    normalize_name = Column('normalize_name', String, nullable=False)
    description = Column('description', Text, nullable=True)
    href = Column('href', String, nullable=False)

    def __init__(self, name, normalize_name, description, href):
        self.name = name
        self.normalize_name = normalize_name
        self.description = description
        self.href = href

    def __repr__(self):
        return "<Author(name='%s', normalize_name='%s', description='%s', href='%s')>" \
               % (self.name, self.normalize_name, self.description, self.href)

    @staticmethod
    def get_author(author_id):
        """
        Get author model. (Also SQLAlchemy object)
        :param author_id: database id
        :return: author object
        """
        author = Session.query(Author).filter_by(id=author_id).first()
        return author

    @staticmethod
    def create_author(name, normalize_name, description, href):
        """
        Create author model
        :return: object itself and boolean value
                True for success, exception will be None. False otherwise.
        """
        try:
            author = Author(name, normalize_name, description, href)
            Session.add(author)
            Session.commit()
            return author, True
        except Exception as e:
            Session.rollback()
            print(e)
            return None, False
