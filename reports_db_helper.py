#!/usr/bin/python2

import psycopg2

DATABASE_NAME = "news"

# Query to retrieve the 3 most viewed articles
POPULAR_ARTICLES_QUERY = """
    SELECT articles.title, count(articles.slug) AS total
    FROM log, articles
    WHERE log.path LIKE CONCAT('%', articles.slug, '%')
    GROUP BY articles.title ORDER BY total DESC LIMIT 3;"""

# Query to retrieve the 3 most viewed articles
POPULAR_AUTHORS_QUERY = """
    SELECT authorship.author, COUNT(authorship.article) AS views
    FROM authorship, log
    WHERE log.path LIKE CONCAT('%', authorship.article, '%')
    GROUP BY authorship.author ORDER BY views DESC;"""

# Query to retrieve the most risk days according with to the number of errors
# in requests to the server.
RISK_DAYS_QUERY = """
    SELECT day, percentageErrors
    FROM (
        SELECT DailyStatus.day,
               ((DailyStatusErr.tStatusErr / DailyStatus.tStatus) * 100)
               AS percentageErrors
        FROM DailyStatus, DailyStatusErr
        WHERE DailyStatus.day = DailyStatusErr.day) AS riskDays
        WHERE percentageErrors > 1.0;"""

db_connection = None


def connect():
    global db_connection
    db_connection = psycopg2.connect("dbname="+DATABASE_NAME)


def apply_query(query):
    cur = db_connection.cursor()
    cur.execute(query)
    return cur.fetchall()


def get_popular_articles():
    return apply_query(POPULAR_ARTICLES_QUERY)


def get_popular_authors():
    return apply_query(POPULAR_AUTHORS_QUERY)


def get_risk_days():
    return apply_query(RISK_DAYS_QUERY)
