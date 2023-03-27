# Stage 1: Copy the built Angular application
FROM node:14 AS build
WORKDIR /app
COPY . .

# Stage 2: Serve the built application using Nginx
FROM nginx:1.21.0-alpine
COPY --from=build /app/dist/distributed-front /usr/share/nginx/html
COPY ./nginx-custom.conf /etc/nginx/conf.d/default.conf
