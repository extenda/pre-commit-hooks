FROM node:13-alpine

WORKDIR /work/

COPY package*.json ./
COPY commitlint.config.js ./
COPY commitlint-plugin-tense/ ./commitlint-plugin-tense/

RUN npm ci --production
RUN npm ci --prefix commitlint-plugin-tense --production

ENTRYPOINT ["/work/node_modules/.bin/commitlint", "--config", "/work/commitlint.config.js"]
