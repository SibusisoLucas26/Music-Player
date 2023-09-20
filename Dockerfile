FROM python:3.8
WORKDIR /app
COPY Muziq Player.py /app/
RUN pip install kivy
CMD ["python", "Muziq Player.py"]

