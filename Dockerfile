# app/Dockerfile

FROM python:3.9

WORKDIR /app

COPY . /app 

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "Home.py"]