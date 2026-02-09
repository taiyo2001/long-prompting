## setup
```bash
# submodule settings
git submodule update --init --recursive

# docker build
docker build \
--build-arg USER_NAME=$(whoami) \
-t $(whoami)-nvidia-devel-server:latest .

# docker run
docker run -it --gpus all \
--user $(id -u):$(id -g) \
-v /home/$(whoami):/home/$(whoami) \
-v /etc/passwd:/etc/passwd:ro \
-v /etc/group:/etc/group:ro \
-e "TERM=xterm-256color" \
--name $(whoami)-devel \
$(whoami)-nvidia-devel-server:latest zsh
```

## docker
```bash
docker exec -it $(whoami)-devel zsh

# root user login for system maintenance / setup
# Non-root users should use 'brew install' for packages (no sudo required).
docker exec -it --user root $(whoami)-devel zsh
```

## conda
※ check Makefile
