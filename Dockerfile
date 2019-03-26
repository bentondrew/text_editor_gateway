FROM alpine:3.9
RUN apk add --no-cache python3 libcap build-base musl-dev linux-headers python3-dev && \
    pip3 install --upgrade pip && \
    pip3 install flask requests uwsgi && \
    apk del build-base musl-dev linux-headers python3-dev && \
    addgroup -S -g 1000 python_user && \
    adduser -u 1000 -S -G python_user -h /home/python_user -s /sbin/nologin -D python_user && \
    chown -R python_user:python_user /home/python_user && \
    setcap CAP_NET_BIND_SERVICE=+eip /usr/bin/uwsgi
WORKDIR /home/python_user
COPY service/ .
EXPOSE 80
USER python_user
ENTRYPOINT ["uwsgi"]
CMD ["--http-socket", "0.0.0.0:80", "--wsgi-file", "server.py"]
