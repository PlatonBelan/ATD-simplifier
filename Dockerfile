FROM node

WORKDIR /app

COPY . .
EXPOSE 3000

CMD [ "node", "./node_modules/mapshaper/mapshaper.js" ]