FROM kumatea/pyrogram:latest

# Install packages
RUN set -ex && \
    wget https://github.com/KumaTea/docker/tarball/master -O /tmp/kuma-docker.tar.gz && \
    mkdir -p /tmp/docker && \
    tar -xzf /tmp/kuma-docker.tar.gz -C /tmp/docker --strip-components 1 && \
    bash /tmp/docker/scripts/install-packages.sh "pillow requests" "apscheduler" && \
    rm -rf /tmp/docker && \
    rm /tmp/kuma-docker.tar.gz

# Set entrypoint
ENTRYPOINT ["/bin/bash", "/home/kuma/bots/dra/docker/run-docker.sh"]
