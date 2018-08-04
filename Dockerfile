FROM indicoio/alpine:3.9.3

LABEL author="Chris Lee"
LABEL email="chrisl@bigseren.com"

ARG EXTRAS="[test]"
ENV PATH=/bigserene_sdk/bin:${PATH}

COPY . /bigserene_sdk
WORKDIR /bigserene_sdk

RUN pip3 install --find-links=/root/.cache/pip/wheels -e .${EXTRAS} && \
    python3 setup.py develop --no-deps

CMD ["bash"]
