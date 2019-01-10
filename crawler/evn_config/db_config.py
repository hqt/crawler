from crawler.utils.parse import parse_env, parse_env_boolean, parse_env_int

DEFAULT_DB_HOST = "0.0.0.0"
DEFAULT_DB_USER = "admin"
DEFAULT_DB_PASS = "password"
DEFAULT_DB_PORT = 3306
DEFAULT_DB_NAME = "book_crawler"
DEFAULT_POOL_SIZE = 15
DEFAULT_IS_LOG_QUERY = False
DEFAULT_IS_LOG_POOL_INFO = True

HOST = parse_env('DB_HOST', DEFAULT_DB_HOST)
USER = parse_env('DB_USER', DEFAULT_DB_USER)
PASS = parse_env('DB_PASS', DEFAULT_DB_PASS)
PORT = parse_env_int('DB_PORT', DEFAULT_DB_PORT)
DB_NAME = parse_env('DB_NAME', DEFAULT_DB_NAME)
POOL_SIZE = parse_env_int('POOL_SIZE', DEFAULT_POOL_SIZE)
IS_LOG_QUERY = parse_env_boolean('IS_LOG_QUERY', DEFAULT_IS_LOG_QUERY)
IS_LOG_POOL_INFO = parse_env_boolean('IS_LOG_POOL_INFO', DEFAULT_IS_LOG_POOL_INFO)
