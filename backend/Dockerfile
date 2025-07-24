FROM python:3.10

# Creating base image
RUN apt-get -y update --fix-missing && \
    # Installing common packages
    apt-get -y install \
        vim \
        git \
        bash \
        wget \
        curl \
        unzip \
        tzdata \
        openssl \
        locales \
        build-essential \
        net-tools \
        libpq-dev \
        musl-dev \
        libc-dev \
        uvicorn \
        pkg-config \
        libffi-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        zlib1g \
        zlib1g-dev \
        liblapack-dev && \
    rm -rf /tmp/* /var/cache/apk/*

# Creating working directory
WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

# Installing public dependencies
RUN pip install --upgrade poetry
