FROM python:3.13-slim

WORKDIR /src

COPY requirements.txt /src/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /src/

EXPOSE 5000

CMD ["python", "app.py"]

ENTRYPOINT ["python", "app.py"]



