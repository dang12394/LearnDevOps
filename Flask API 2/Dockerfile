FROM python
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","manage.py","seed_db"]
CMD ["Y"]
CMD ["python","wsgi.py"]