FROM python:3.9


EXPOSE 6363
# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./terminusApp /code/terminusApp

# 
CMD ["uvicorn", "terminusApp.main:app", "--host", "0.0.0.0", "--port", "80"]