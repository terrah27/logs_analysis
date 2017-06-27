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
