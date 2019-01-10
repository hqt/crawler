# Book Crawler

## Setup database

- Start MariaDB docker container
  ```bash
  docker run --name mariadb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mariadb
  ```

- Create database and user
  ```bash
  docker exec -it mariadb mysql -u root -p
  ```
  - Run following SQL commands:
  ```sql
  CREATE SCHEMA IF NOT EXISTS book_crawler DEFAULT CHARACTER SET utf8;
  CREATE USER IF NOT EXISTS 'admin' IDENTIFIED BY 'password';
  GRANT ALL ON book_crawler.* TO 'admin';
  \q
  ```

- Access database with the created user
  ```bash
  docker exec -it mariadb mysql book_crawler -u admin -p
  ```
  - Some SQL commands:
  ```sql
  SELECT DATABASE();
  SHOW TABLES;
  SELECT DISTINCT table_name, index_name FROM information_schema.statistics WHERE table_schema = 'book_crawler';
  SHOW COLUMNS FROM authors;
  \q
  ```

## Install packages
- Install python 2.7. Recommendation: using [pyenv](https://github.com/pyenv/pyenv) to manage python version. [Tutorial](https://gist.github.com/hqt/2ffd4b9ef818aa2d760d07c5c5022f56)

- Install virtualenv to create isolated Python environment.
  ```bash
  pip install virtualenv
  ```
- Initialize virtualenv:
  ```bash
  virtualenv venv
  ```
- Every time running project or testing:
  ```bash
  source venv/bin/activate
  ```
- Install python packages:
  ```bash
  pip install -r requirements.txt
  ```
- Every time install new package:
  ```bash
  pip install library_name===version
  pip freeze > requirements.txt
  ```
 
## Running crawler job
- Before running job, start [scrapy_splash](https://github.com/scrapy-plugins/scrapy-splash)
  ```bash
  docker run -p 8050:8050 scrapinghub/splash
  ```
  
- Run a specific job:
  ```bash
  scrapy crawl [job_name]
  ```
 
- Example, run job on ss_truyen:
  ```bash
  scrapy crawl ss
  ```

## Run tests
- Run all tests:
  ```bash
   chmod +x test.sh
   ./test.sh
  ```
