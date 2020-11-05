FROM node:current-alpine as build

WORKDIR /build

ADD public ./public
ADD src ./src
ADD package.json .
ADD tsconfig.json .

RUN yarn install --silent
RUN yarn build

FROM nginx:alpine as prod

ADD conf/default.conf /etc/nginx/conf.d
COPY --from=build /build/build /etc/nginx/html