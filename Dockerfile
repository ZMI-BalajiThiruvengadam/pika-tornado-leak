FROM alpine:3.3
ENV REFRESHED_AT 2016-03-06

WORKDIR /opt/project/
RUN apk add --update curl-dev gcc musl-dev python python-dev py-pip && \
    pip install --no-cache-dir virtualenv && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /opt/platform/services && \
    virtualenv env && source env/bin/activate

ENV PYTHONPATH /opt/project/
COPY . /opt/project/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]