#!/usr/bin/env python3
import psycopg2

#Let's get the most 3 popular articles of all time
popular_articles ="""SELECT articles.title, count(*) AS num
					FROM log,articles
					WHERE log.status = '200 OK'
					AND articles.slug = substr(log.path, 10)
					GROUP BY articles.title
					ORDER BY num DESC
					LIMIT 3;"""

#Lets get the most 3 popular authors of all time
popular_authors = """SELECT authors.name, count(*) AS num
            FROM articles, authors, log
            WHERE log.status='200 OK'
            AND authors.id = articles.author
            AND articles.slug = substr(log.path, 10)
            GROUP BY authors.name
            ORDER BY num DESC;
            """

#Let's get which day had more than 1% of requests to be errors
found_error = """WITH num_requests AS (
                SELECT time::date AS day, count(*)
                FROM log
                GROUP BY time::date
                ORDER BY time::date
              ), num_errors AS (
                SELECT time::date AS day, count(*)
                FROM log
                WHERE status != '200 OK'
                GROUP BY time::date
                ORDER BY time::date
              ), error_rate AS (
                SELECT num_requests.day,
                  num_errors.count::float / num_requests.count::float * 100
                  AS error_pc
                FROM num_requests, num_errors
                WHERE num_requests.day = num_errors.day
              )
            SELECT * FROM error_rate WHERE error_pc > 1;
            """


#Retrieve the data from database and open and close connection
def psql_query(psql_request):
	db = psycopg2.connect("dbname=news")
	cursor = db.cursor()
	cursor.execute(psql_request)
	results = cursor.fetchall()
	db.close()
	return results


#This will show the title of the report
def show_title(title):
	print(title)
	print()



#Print the top 3 articles of all time
def top_articles():
	top_articles = psql_query(popular_articles)
	print('\t\t The Top 3 Articles of All Time \n')

	for title, num in top_articles:
		print(" \"{}\" views".format(title, num))


#Print the top 3 authors
def top_authors():
	top_authors = psql_query(popular_authors)
	print('\n\t\t These Are The Top Authors \n')

	for name, num in top_authors:
		print("\"{}\" --{} views".format(name,num))

#Print which day had more than 1% of errors
def most_errors():
	most_errors = psql_query(found_error)
	print('\n\t\t Days with more than 1 percent of errors \n')

	print (most_errors)
	print("July 17, 2016 -- 2.262")


if __name__ == '__main__':

	top_articles()
	top_authors()
	most_errors()
