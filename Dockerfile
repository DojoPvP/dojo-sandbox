FROM --platform=linux/amd64 ubuntu:22.04 as base

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y ca-certificates

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    g++ \
    gcc \
    git \
    make \
    pkg-config \
    curl \
    libssl-dev \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*
