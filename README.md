# logs_analysis

A project for Udacity fullstack nanodegree creating a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.  Questions being answered are:
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?
  
# requirements

-virtualbox  
-vagrant  
-python3 (code written using python 3.5.2)  

# getting started

-Clone the repository https://github.com/udacity/fullstack-nanodegree-vm to download the virtual machine configuration.  
-Start the virtual machine by running `vagrant up` from inside the vagrant directory and then `vagrant ssh` to log into the virtual machine.  
-Inside the VM, change directory to `/vagrant/logs`  
-Download the data here: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip then unzip and place the file newsdata.sql in the logs directory  
-Load the data by running `psql -d news -f newsdata.sql`  
-Run the file analysis.py in the command line by running `python3 analysis.py`  

# required views
*For question 3 there are 3 views that must be created in the database.
1.  To find the number of errors per day:  
 `CREATE VIEW errors AS SELECT count(date(log."time")) AS errors,
    date(log."time") AS date
   FROM log
  WHERE log.status <> '200 OK'::text
  GROUP BY (date(log."time"));`
2. To find the total number of requests per day:  
   `CREATE VIEW totals AS SELECT count(date(log."time")) AS totals,
    date(log."time") AS date
   FROM log
  GROUP BY (date(log."time"));`
3.  To find the percentage of errors per day:  
   `CREATE VIEW percents AS SELECT errors.errors::double precision / totals.totals::double precision * 100::double precision AS percents,
    errors.date
   FROM errors
     JOIN totals ON errors.date = totals.date
  ORDER BY (errors.errors::double precision / totals.totals::double precision * 100::double precision) DESC;`
# output

The analysis.py file will create a report in the logs directory analysis.txt
