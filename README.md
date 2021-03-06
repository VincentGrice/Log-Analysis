# Logs Analysis Project
Building an informative summary from logs and interacting with a live database that has over one million rows both from the command line and from python code. Build and refine complex queries and use them to draw business conclusions from data. This project is a part of the Udacity's Full Stack Web Developer Nanodegree.

## Technologies used
1. PostgreSQL
2. Writing Python code with DB-API
3. Linux-based virtual machine (VM) Vagrant

## Project Requirements
Reporting tool should answer the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

* Project follows good SQL coding practices.  
* The code is error free. 
* The code presents its output in plain text.

## System setup and how to view this project
This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.
1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install. 
3. Clone this repository to a directory of your choice.
4. Download the **newsdata.sql** (extract from **newsdata.zip** (not provided here though)) and **newsdata.py** files from the respository and move them to your **vagrant** directory within your VM.

#### Run these commands from the terminal in the folder where your vagrant is installed in: 
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```python newsdata.py``` to run the reporting tool.
