FROM python:3.9.7-slim

# Install package
WORKDIR /code
COPY . .
RUN pip3 install .

ENV EXPORTER_CONFIG="/config/config.yml"
ENV EXPORTER_PORT=9000
ENV USE_MULTI_PORTS=false

ENTRYPOINT downloader-exporter -c ${EXPORTER_CONFIG} -p ${EXPORTER_PORT} --multi ${USE_MULTI_PORTS}
