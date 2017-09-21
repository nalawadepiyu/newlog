#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def main():
    """Return most popular three articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    firstquery = """select article_details.view , article_details.title
    from article_details order by article_details.view desc limit 3"""
    c.execute(firstquery)
    firstsolution = c.fetchall()
    print "Answer 1:"
    for each in firstsolution:
        print " Article :" each[1] " -- Views :" each[0]

    secondquery = """select SUM(article_details.view) as count ,
    article_details.name from article_details group by
    article_details.name order by count desc"""
    c.execute(secondquery)
    secondsolution = c.fetchall()
    print "======================================================"
    print "Answer 2: "
    for each in secondsolution:
        print "Author: " each[1] "--views: "each[0]

    thirdquery = """select * from rate_err_view where
    rate_err_view.percentage > 1 order by rate_err_view.percentage desc"""
    c.execute(thirdquery)
    thirdsolution = c.fetchall()
    print "======================================================="
    print "Answer 3:"
    for each in thirdsolution:
        print "date : " each[0] "percentage: " each[1]
    db.close()
if __name__ == '__main__':
    main()
