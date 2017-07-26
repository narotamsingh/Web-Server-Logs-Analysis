#!/usr/bin/env python2
import psycopg2
'''
Code for the Log Analysis Project: A reporting tool that prints out
reports (in plain text) based on the data in the database, this program
using the psycopg2 module to connect to the database.
'''


def connect(db_name=“news”):
    """Connect to database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname={}".format(db_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print "Unable to connect to the database",db_name

def fetch_query(query):
    """
    Connect to the database, query, fetch results, close connection, return results
    """
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

        
def article():
    """Fetch and prints most popular three articles of all time"""
    Query = """
        SELECT articles.title, count(log.path) AS num
        FROM articles, log
        WHERE log.path=CONCAT('/article/', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3
        """
    result = fetch_query(Query)
    print "\nMost popular three articles of all time:"
    for item in result:
        print '\"{}\" - {} views'.format(item[0], item[1])


def author():
    """Fetch and prints most popular article authors of all time"""
    Query = """
        SELECT authors.name, count(log.path) AS num
        FROM authors, articles, log
        WHERE (log.path=CONCAT('/article/', articles.slug))
        AND (authors.id = articles.author)
        GROUP BY authors.name
        ORDER BY num DESC
    """
    result = fetch_query(Query)
    print "\nMost popular article authors of all time:"
    for item in result:
        print '{} - {} views'.format(item[0], item[1])


def error():
    """Fetch and print days on which more than 1% of requests lead to errors"""
    Query = """
        SELECT DATE(time),
        round(SUM(CASE
                    WHEN status ='404 NOT FOUND' THEN 1 ELSE 0
                    END) * 100.00 / count(status),2) AS One
        FROM log
        GROUP BY DATE(time)
        HAVING SUM(CASE
                    WHEN status ='404 NOT FOUND' THEN 1 ELSE 0
                    END) * 100.00 / count(status) > 1.00
        ORDER BY One DESC
        """
    result = fetch_query(Query)
    print "\nOn which days did more than 1% of requests lead to errors:"
    for item in result:
        """Formating date here, save database time"""
        print '{:%B %d, %Y} - {}% errors\n'.format(item[0], item[1])


if __name__ == '__main__':
    article()
    author()
    error()

