FROM python:3.9.13

RUN curl -O http://capnproto.org/capnproto-c++-0.5.0.tar.gz \
    && tar zxf capnproto-c++-0.5.0.tar.gz \
    && cd capnproto-c++-0.5.0 \
    && ./configure \
    && make -j6 check \
    && make install

RUN pip install flatbuffer pycapnp numpy