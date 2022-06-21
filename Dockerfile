FROM ubuntu

WORKDIR /app

RUN apt update
RUN apt install -y nodejs
RUN apt install -y python3
RUN apt install -y npm

COPY package.json /app

RUN npm install -g mapshaper
RUN npm install

COPY . .

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
#CMD ["python3", "test.py"]