FROM python:3.11.3

WORKDIR /app

# Better practice to copy requirements.txt over to the virtual file system first, that way it'll install dependencies first
COPY requirements.txt /app/

RUN pip3 install --no-cache-dir -r requirements.txt

# Then copy over the rest of the files
COPY *.py /app/

CMD ["python3", "__init__.py"]