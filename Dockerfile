                                                                                                                                                                         
#   docker build -t fullfastapi .                                                                                                                                         
#   docker run --rm -p 80:80 fullfastapi

FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY src /code/src

EXPOSE 80

 # fastapi run src/main.py --port 80.
CMD ["fastapi", "run", "src/main.py", "--port", "80"] 
          
