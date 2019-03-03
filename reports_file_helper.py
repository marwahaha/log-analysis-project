#!/usr/bin/python2

import os
from prettytable import PrettyTable

REPORTS_FOLDER = "./reports/"

REPORT_POPULAR_ARTICLES_FILE = "report_popular_articles.txt"
REPORT_POPULAR_AUTHORS_FILE = "report_popular_authors.txt"
REPORT_RISK_DAYS_FILE = "report_risk_days.txt"

POPULAR_ARTICLES_COLUMNS = ["Article Name", "Total of Views"]
POPULAR_AUTHORS_COLUMNS = ["Author Name", "Total of Views"]
RISK_DAYS_COLUMNS = ["Day", "Errors Percentage"]

def create_reports_dir():
    try:  
        os.mkdir(REPORTS_FOLDER)
    except OSError:  
        print ("Creation of the directory %s failed" % REPORTS_FOLDER)


def save_report(report, fileName):
    if not os.path.isdir(REPORTS_FOLDER):
        create_reports_dir()

    report_path = REPORTS_FOLDER + fileName
    with open(report_path, 'w') as reportFile:
        reportFile.write(str(report))
        reportFile.close()


def create_report(columns, rows):
    report = PrettyTable()
    report.field_names = columns
    report.align[columns[0]] = "l"

    for record in rows:
        report.add_row(record)
    
    return report


def create_popular_articles_report(popularArticles):
    report = create_report(POPULAR_ARTICLES_COLUMNS, popularArticles)
    save_report(report, REPORT_POPULAR_ARTICLES_FILE)

def create_popular_authors_report(popularAuthors):
    report = create_report(POPULAR_AUTHORS_COLUMNS, popularAuthors)
    save_report(report, REPORT_POPULAR_AUTHORS_FILE)


def create_risk_days_report(riskDays):
    report = create_report(RISK_DAYS_COLUMNS, riskDays)
    save_report(report, REPORT_RISK_DAYS_FILE)