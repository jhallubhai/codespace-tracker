FROM ubuntu:22.04

# Base tools
RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y \
    curl git vim nano wget python3 python3-pip build-essential \
    htop zram-tools docker.io tlp jq unzip nodejs npm cmake \
    cron tzdata \
    && apt clean && rm -rf /var/lib/apt/lists/*

# Enable zram and docker
RUN echo 'ALGO=lz4' > /etc/default/zramswap && \
    echo 'PERCENT=50' >> /etc/default/zramswap && \
    systemctl enable zramswap && \
    systemctl enable docker

# Set working dir
WORKDIR /workspaces/C93

# Default command
CMD ["/bin/bash"]
