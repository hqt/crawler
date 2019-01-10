import pymysql.cursors
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from crawler.evn_config import db_config
from crawler.evn_config.db_config import IS_LOG_QUERY, POOL_SIZE, IS_LOG_POOL_INFO


def connection():
    return pymysql.connect(
        host=db_config.HOST,
        port=db_config.PORT,
        user=db_config.USER,
        password=db_config.PASS,
        db=db_config.DB_NAME,
        charset='utf8mb4',
    )


# Configure pool option
# http://docs.sqlalchemy.org/en/latest/core/pooling.html
engine = create_engine(
    'mysql+pymysql://',
    creator=connection,
    echo=IS_LOG_QUERY,
    pool_size=POOL_SIZE,
    max_overflow=0,
    echo_pool=IS_LOG_POOL_INFO,
    pool_pre_ping=True,
)

# using scope_session to keep one session for each request
# ref: http://docs.sqlalchemy.org/en/latest/orm/contextual.html
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
