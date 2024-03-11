# Dockerfile for JupyterLab
# base version

FROM quay.io/jupyter/base-notebook:lab-4.1.4

LABEL maintainer="Tarun Chadha, tarunchadha23@gmail.com"

# JupyterHub Version
ARG JUPYTERLAB_VERSION=4.1.4

USER root

# APT packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_UID

COPY environment.yml /tmp/environment.yml

# Install packages
# Conda packages
RUN conda env update --name base --file /tmp/environment.yml && \
    conda clean --all -y && \
    fix-permissions $CONDA_DIR

ENV CPATH=$CONDA_DIR/include

RUN fix-permissions $CONDA_DIR

# Add conda env hook
COPY ./conda-activate.sh /usr/local/bin/before-notebook.d/