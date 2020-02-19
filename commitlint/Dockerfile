FROM node:13-alpine

WORKDIR /work/

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

COPY package*.json ./
COPY commitlint.config.js ./
COPY commitlint-plugin-tense/ ./commitlint-plugin-tense/
COPY bin/commitlint.sh /usr/local/bin/commitlint

RUN npm ci --production
RUN npm ci --prefix commitlint-plugin-tense --production
RUN rm -rf ~/.npm

ENTRYPOINT ["/usr/local/bin/commitlint"]
