FROM python:3.8

RUN pip install bs4 requests joblib

COPY main.py phone_scraper.py logo_scraper.py ./

CMD ["python3", "./main.py"]