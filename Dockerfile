FROM node

WORKDIR /app

COPY package.json /app

RUN npm install

VOLUME ["D:/ATD-simplifier/node_modules/mapshaper/data:/app/node_modules/mapshaper/data"]
VOLUME ["app/node_modules"]

CMD ["node", "mapshaper.js"]