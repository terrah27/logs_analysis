#!/usr/bin/env python

import psycopg2
# pscycopg2 for connecting to database


def get_analysis():

    try:
        # first step connect to database and create cursor
        db = psycopg2.connect(database='news')
        c = db.cursor()

        # Find 3 most popular articles of all time
        c.execute("""SELECT articles.title, count(log.path) as num
            from log, articles where substring(log.path, 10) = articles.slug
            group by articles.title order by num desc limit 3""")
        popular_articles = c.fetchall()

        formatted_articles = ""
        for i in popular_articles:
            formatted_articles += ('"%s" -- %s views\n' % (i[0], i[1]))

        # Find most popular authors of all time
        c.execute("""SELECT count(log.path) as num,
            (select authors.name from authors
            where authors.id = articles.author)
            from log, articles where substring(log.path, 10) = articles.slug
            group by articles.author order by num desc;""")
        popular_authors = c.fetchall()

        formatted_authors = ""
        for i in popular_authors:
            formatted_authors += ("%s -- %s views\n" % (i[1], i[0]))

        # Find days were > 1% of requests led to errors
        c.execute("""SELECT date, round(cast(percents as numeric), 2)
            from percents where percents >= 1;""")
        errors = c.fetchall()

        # close connection to database
        db.close()

        formatted_errors = ""
        for i in errors:
            formatted_errors += ("%s -- %s%%\n" % (i[0], i[1]))

        with open("analysis.txt", "w") as text_file:
            print("Three most popular articles: \n{}".format(
                formatted_articles), file=text_file)
            print("Three most popular authors: \n{}".format(
                formatted_authors), file=text_file)
            print("Days with more that 1% errors: \n{}".format(
                formatted_errors), file=text_file)

        return formatted_articles, popular_articles, formatted_errors

    except psycopg2.Error as e:
        print(e)

if __name__ == '__main__':
    get_analysis()
    print('Report Complete.  See file analysis.txt')
