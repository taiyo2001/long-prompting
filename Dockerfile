# INFO: `nvidia-smi`と一致
# WAN: required devel for nvcc
FROM nvidia/cuda:12.2.2-devel-ubuntu22.04

ARG USER_NAME

ENV TZ=Asia/Tokyo

# --- System & Package Installation ---
RUN apt-get update && apt-get install -y \
    git \
    git-lfs \
    gh \
    curl \
    wget \
    tree \
    vim \
    gnupg2 \
    libgl1-mesa-glx \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    zsh \
    && rm -rf /var/lib/apt/lists/*

# --- Tools Install (as root) ---
## Homebrew
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && \
    chown -R root:root /home/linuxbrew/.linuxbrew && \
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /root/.bashrc && \
    eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" && \
    apt-get update && \
    apt-get install build-essential -y

RUN eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" && \
    brew install gh starship direnv asdf

## Conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    chmod +x miniconda.sh && \
    ./miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh && \
    /opt/conda/bin/conda init bash

# --- User Configuration (as non-root) ---
WORKDIR /home/${USER_NAME}/workspace/research

CMD ["/bin/bash"]
