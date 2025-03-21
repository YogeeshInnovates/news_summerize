web: gunicorn news_summarization.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn news_summarization.wsgi
