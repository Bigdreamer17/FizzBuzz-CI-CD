FROM python:3.11

# Set the working directory
RUN mkdir /app

WORKDIR /app

COPY requirements.txt .


RUN pip install -r requirements.txt


COPY . .


CMD [ "python3", "main.py", "python" ]