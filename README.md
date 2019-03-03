# Log Analysis Project
This is the source code for the log analysis project.

## Installation
1) Please **clone** the project's repository running the following command on a **terminal**:
```
git clone https://github.com/thiagothalison1/log-analysis-project.git
```
2) Install the project's dependencies:
```
sudo pip install prettytable
```
3) Create the used **views** on the **news** database:
```
CREATE VIEW authorship AS SELECT articles.slug AS article, authors.name AS author FROM authors, articles WHERE articles.author = authors.id;
```
```
CREATE VIEW DailyStatus AS SELECT TO_CHAR(time, 'dd/mm/yyyy') AS day, COUNT(status)::float AS tStatus FROM log GROUP BY day;
```
```
CREATE VIEW DailyStatusErr AS select TO_CHAR(time, 'dd/mm/yyyy') AS day, COUNT(status)::float AS tStatusErr FROM log WHERE status LIKE '%404%' GROUP BY day;
```

## Execution
To execute the project, please run the following command on a terminal:
```
python reports.py
```
**NOTE**: A reports folder will be created on the projects root directory. There will be three reports, one per question.
Question 1 - <log-analysis-project>/report_popular_articles.txt
Question 2 - <log-analysis-project>/report_popular_authors.txt
Question 3 - <log-analysis-project>/report_risk_days.txt

## License
This project is distributed under [MIT License](https://opensource.org/licenses/MIT)
