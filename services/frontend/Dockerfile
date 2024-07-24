FROM node:18-alpine as build

WORKDIR /app

COPY package.json /app

RUN yarn install

COPY . /app

RUN yarn build                 


EXPOSE 3000/tcp


