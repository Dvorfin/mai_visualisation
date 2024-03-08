FROM python

COPY publisher.py /

COPY requirements.txt /

RUN pip install -r requirements.txt && rm requirements.txt

#EXPOSE 1883


CMD ["python", "./publisher.py"]