from time import sleep
import os
import schedule


def job_login():
    os.system('python -m unittest ./Test/Login.py')


def job_new_persons():
    os.system('python -m unittest ./Test/New_Persons.py')


def job_main():
    os.system('python -m unittest ./main.py')


# schedule.every(30).seconds.do(job)
schedule.every().day.at("15:34").do(job_main)
schedule.every(10).minutes.do(job_login)
schedule.every(12).minutes.do(job_new_persons)


while True:
    schedule.run_pending()
    sleep(1)
