FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf && rm /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d
COPY nginx.conf  /etc/nginx/nginx.conf