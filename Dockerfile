FROM python:3.11.3

COPY *.py /app/

WORKDIR /app

RUN pip3 install PySimpleGUI

CMD ["python3", "__init__.py"]