FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y openssl curl bash python2.7

CMD ["bash"]
