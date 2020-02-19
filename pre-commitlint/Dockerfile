FROM node:13-alpine

COPY package*.json /work/
COPY commitlint.config.js /work/

WORKDIR /work/

RUN npm ci

ENTRYPOINT ["/work/node_modules/.bin/commitlint", "--config", "/work/commitlint.config.js", "--edit" ]
