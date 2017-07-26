#!/usr/bin/env python2
import psycopg2
'''
Code for the Log Analysis Project: A reporting tool that prints out
reports (in plain text) based on the data in the database, this program
using the psycopg2 module to connect to the database.
'''


def article():
    """Run query and prints most popular three articles of all time"""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    Query = """
        SELECT articles.title, count(log.path) AS num
        FROM articles, log
        WHERE log.path=CONCAT('/article/', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3
        """
    c.execute(Query)
    print "\nMost popular three articles of all time:"
    for item in c.fetchall():
        print '\"{}\" - {} views'.format(item[0], item[1])
    db.close()


def author():
    """Run query and prints most popular article authors of all time"""
    db = psycopg2.connect(database="news")
    c = db.cursor()
    Query = """
        SELECT authors.name, count(log.path) AS num
        FROM authors, articles, log
        WHERE (log.path=CONCAT('/article/', articles.slug))
        AND (authors.id = articles.author)
        GROUP BY authors.name
        ORDER BY num DESC
    """
    c.execute(Query)
    print "\nMost popular article authors of all time:"
    for item in c.fetchall():
        print '{} - {} views'.format(item[0], item[1])
    db.close()


def error():
    """Query and print days on which more than 1% of requests lead to errors"""
    db = psycopg2.connect(database="news")
    """Connect to the PostgreSQL database."""
    c = db.cursor()
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
    c.execute(Query)
    print "\nOn which days did more than 1% of requests lead to errors:"
    for item in c.fetchall():
        """Formating date here, save database time"""
        print '{:%B %d, %Y} - {}% errors\n'.format(item[0], item[1])
    db.close()


article()
author()
error()
