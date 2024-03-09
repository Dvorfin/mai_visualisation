FROM python

COPY subscriber.py /

COPY requirements.txt /

RUN pip install -r requirements.txt && rm requirements.txt

#EXPOSE 1883

CMD ["python", "./subscriber.py"]