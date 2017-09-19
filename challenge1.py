#!/usr/bin/env python
from jenkinsapi.jenkins import Jenkins
import sqlite3
from datetime import datetime

def get_server_instance(jenkins_url,username,password):
    server = Jenkins(jenkins_url, username, password)
    return server

"""Get job details of each job that is running on the Jenkins instance"""
def get_job_details():
  url=raw_input("enter jenkins url ")
  username=raw_input("enter jenkins username") 
  password=raw_input("enter jenkins password")    
  server = get_server_instance(url,username,password)
  conn=databaseConnection()
  cursor = conn.cursor()
  now=datetime.now()
  for j in server.get_jobs():
    job_instance = server.get_job(j[0])
    print 'Job Name:%s' %(job_instance.name)
    print 'Job Description:%s' %(job_instance.get_description())
    print 'Is Job running:%s' %(job_instance.is_running())
    print 'Is Job enabled:%s' %(job_instance.is_enabled())
    cursor.execute("INSERT INTO jobs(name, status,date) VALUES(?, ?)",(job_instance.name, job_instance.is_running(),now)
        
  conn.commit()
  conn.close()


def databaseConnection():
  conn = sqlite3.connect('my_base.db') 
  cursor = conn.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     status INTERGER,
     date TEXT
)
""")
  conn.commit()
  return conn


get_job_details()