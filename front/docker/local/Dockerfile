ARG NODE_VERSION=16.14-alpine

FROM node:${NODE_VERSION} as node

FROM node as front-local-build

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

COPY ./package*.json .
RUN npm install
RUN mkdir node_modules/.cache && chmod -R 777 node_modules/.cache

COPY . .

CMD ["npm", "run", "start"]
