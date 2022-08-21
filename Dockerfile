FROM ubuntu:22.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl \
    wget \
    git \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    python3-pip \
    flatbuffers-compiler \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*    
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN mkdir -p /tmp
WORKDIR /tmp

# Install Capnproto (for schema compiler)
# RUN wget http://capnproto.org/capnproto-c++-0.10.2.tar.gz \
#     && tar zxf capnproto-c++-0.10.2.tar.gz \
#     && cd capnproto-c++-0.10.2 \
#     && ./configure \
#     && make -j6 \
#     && make install \
#     && cd .. \
#     && rm -r capnproto-c++-0.10.2

RUN mkdir protoc && cd protoc \
    && wget wget https://github.com/protocolbuffers/protobuf/releases/download/v21.5/protoc-21.5-linux-x86_64.zip \
    && unzip protoc-21.5-linux-x86_64.zip \
    && cp -f bin/protoc /usr/bin \
    && cd .. \
    && rm -r protoc

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /opt/work