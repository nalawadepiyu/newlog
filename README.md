# UdacityLogAnalysis

<h1> Questions: </h1>
<h3> What are the most popular three articles of all time?  </h3>
<h3> Who are the most popular article authors of all time?  </h3>
<h3> On which days did more than 1% of requests lead to errors?  </h3>

<h3> What is the purpose of this project? </h3>
<h4>Print reports based on data from database </h4>
<br>
<h3> What are the essential software components needed to set up the run-time environment?</h3>
<h4>Python 2.7</h4>
<h4>Sqlite </h4>
<br>
<h3> Where can you download the newsdata.sql file from? </h3>
<h4>psql -d news -f newsdata.sql</h4>
<br>
<br>
<h1> Steps </h1>
<h4> 1. load database </h4>
<h4>psql -d news -f newsdata.sql</h4>
<br>
<h4> 2. Creat Views :</h4>
<h4> CREATE VIEW author_details AS SELECT articles.title, articles.slug ,authors.name FROM authors , articles WHERE articles.author = authors.id ORDER BY authors.name; </h4>
<br>
<h4> CREATE VIEW path_details AS SELECT path, COUNT(*) AS view FROM log GROUP BY path ORDER BY path;   </h4>
<br>
<h4> CREATE VIEW article_details AS SELECT author_details.name, author_details.title, path_details.view FROM author_details, path_details WHERE path_details.path = CONCAT('/article/', author_details.slug) ORDER BY author_details.name;
 </h4>
 <br>
<h4>create view total as select count(*) AS views, date(time) from log group by date(time) order by date(time); </h4>
 <br>
<h4> create view error as select count(*) as allerrors , date(time) from log where status = '404 NOT FOUND' group by date(time) order by date(time); </h4>
 <br>
<h4>create view rate_err_view as select total.date, (error.allerrors*100.0/total.views) as percentage from total, error where total.date = error.date order by total.date;</h4>
 <br>
<h4> 3. Run loganalysis.py</h4>
<br>
<h4> 4. Output is in attached text file </h4>
