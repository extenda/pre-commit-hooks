FROM node:13-alpine

WORKDIR /work/

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

COPY package*.json ./
COPY commitlint.config.js ./
COPY commitlint-plugin-tense/ ./commitlint-plugin-tense/

RUN npm ci --production
RUN npm ci --prefix commitlint-plugin-tense --production
RUN rm -rf ~/.npm

RUN ln -s /work/node_modules/.bin/commitlint /usr/local/bin/commitlint
ENV COMMITLINT_CONFIG=/work/commitlint.config.js

ENTRYPOINT ["/usr/local/bin/commitlint", "--config", "/work/commitlint.config.js"]
CMD ["--edit"]
