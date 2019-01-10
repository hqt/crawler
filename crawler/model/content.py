from sqlalchemy import Column, Integer, String, Text

from crawler.model import AlchemyBase
from crawler.utils.database import Session


class Content(AlchemyBase):
    __tablename__ = 'contents'

    id = Column(Integer, primary_key=True)
    data = Column('data', Text, nullable=False)
    href = Column('href', String, nullable=False)
    chapter_id = Column('chapter_id', Integer, nullable=False)

    def __init__(self, data, href, chapter_id):
        self.data = data
        self.href = href
        self.chapter_id = chapter_id

    def __repr__(self):
        return "<Content(data='%s', href='%s', chapter_id='%s')>" \
               % (self.data, self.href, self.chapter_id)

    @staticmethod
    def get_content(content_id):
        """
        Get chapter model. (Also SQLAlchemy object)
        :param content_id: database id
        :return: author object
        """
        content = Session.query(Content).filter_by(id=content_id).first()
        return content

    @staticmethod
    def create_content(data, href, chapter_id):
        """
        Create content model
        :return: object itself and boolean value
                True for success, exception will be None. False otherwise.
        """
        try:
            content = Content(data, href, chapter_id)
            Session.add(content)
            Session.commit()
            return content, True
        except Exception as e:
            Session.rollback()
            print(e)
            return None, False
