#!/usr/bin/python2

import reports_db_helper
import reports_file_helper

if __name__ == "__main__":
    reports_db_helper.connect()

    result = reports_db_helper.get_popular_articles()
    reports_file_helper.create_popular_articles_report(result)

    result = reports_db_helper.get_popular_authors()
    reports_file_helper.create_popular_authors_report(result)

    result = reports_db_helper.get_risk_days()
    reports_file_helper.create_risk_days_report(result)
    