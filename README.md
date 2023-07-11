# JupyterHub deployment with docker

project forked from https://github.com/defeo/jupyterhub-docker

## Features

- Containerized single user Jupyter servers, using
  [DockerSpawner](https://github.com/jupyterhub/dockerspawner);
- Central authentication to the University CAS server;
- User data persistence;
- HTTPS proxy.


## Uruchomienie
> docker-compose build

> docker-compose run

Traefik sam generuje certyfikaty

/app/jupyterhub/jupyterhub_config.py zawiera plik konfiguracyjny
.env zmienne środowiskowe
