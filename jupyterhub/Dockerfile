# Dockerfile for JupyterHub
# JupyterHub version: 3.1.1

#FROM jupyterhub/jupyterhub:3.1.1
FROM jupyterhub/jupyterhub:latest

# Create admin user
RUN useradd -rm -d /home/admin -s /bin/bash -g root -G sudo -u 1001 admin

# Install packages
RUN pip install \
    # Dockerspawner for JupyterHub
    dockerspawner \
    # JupyterHub CAS Authenticator
    jhub_cas_authenticator \
    # JupyterHub Idle Culler
    jupyterhub-idle-culler

# Copy configuration file
COPY ./jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
