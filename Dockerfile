FROM python:3.11.3

COPY src /app

WORKDIR /app

RUN pip3 install PySimpleGUI

CMD ["python3", "main.py"]