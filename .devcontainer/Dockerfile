FROM ubuntu:22.04

# Base tools & python
RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y \
    curl git vim nano wget build-essential \
    python3 python3-pip \
    htop zram-tools docker.io tlp jq unzip nodejs npm cmake \
    cron tzdata

# Enable zram and docker on boot
RUN echo 'ALGO=lz4' > /etc/default/zramswap && \
    echo 'PERCENT=50' >> /etc/default/zramswap && \
    systemctl enable zramswap && \
    systemctl enable docker

# Set working directory (auto cd here on launch)
WORKDIR /workspaces/codespace-tracker

# Final cleanup for a tidy image
RUN apt clean && rm -rf /var/lib/apt/lists/*

# Set working directory (auto cd here on launch)
WORKDIR /workspaces/codespace-tracker

# Default shell
CMD ["/bin/bash"]