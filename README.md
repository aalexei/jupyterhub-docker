# JupyterHub deployment with docker

project forked from https://github.com/pavlsnak/jupyterhub-docker
which was originally forked from https://github.com/defeo/jupyterhub-docker

## Features

- Containerized single user Jupyter servers, using
  [DockerSpawner](https://github.com/jupyterhub/dockerspawner);
- User data persistence;
- HTTPS proxy;
- Auto culling of inactive user-servers after 3600 seconds

# Deployment steps

- Install Docker: https://docs.docker.com/engine/install/
- Add user to the docker group. NOTE: This user will be the admin of the deployed jupyter hub
- For HTTPS ssl keys are required. If you do not have keys, self-signed keys can be generated using openssl

```
openssl genrsa 2048 > host.key
openssl req -new -x509 -sha256 -days 365 -key host.key -out host.crt
```

The generated key-certificate pair must be copied into the following location:
```
cp host* ./reverse-proxy/certs/
```

- In [`.env`](.env), set the variable `HOST` to the name of the server you
  intend to host your deployment on.
- In [`reverse-proxy/tls.yml`](reverse-proxy/tls.yml), edit
  the paths in `certFile` and `keyFile` and point them to your own TLS
  certificates. Possibly edit the `volumes` section in the
  `reverse-proxy` service in
  [`docker-compose.yml`](docker-compose.yml).

```
certFile: "/etc/certs/host.crt" -> certFile: "/etc/certs/YOUR_CERTIFICATE.crt"
keyFile: "/etc/certs/host.key" ->  keyFile: "/etc/certs/YOUR_KEY.key"
```
- In
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py),
  edit the *"Authenticator"* section according to your institution
  authentication server.  If in doubt, [read
  here](https://jupyterhub.readthedocs.io/en/stable/getting-started/authenticators-users-basics.html).

Other changes you may like to make:

- Edit [`jupyterlab/Dockerfile`](jupyterlab/Dockerfile) to include the
  software you like. Do not forget to change
  [`jupyterhub/jupyterhub_config.py`](jupyterhub/jupyterhub_config.py)
  accordingly, in particular the *"user data persistence"* section.


## Learn more

This deployment is described in depth in [this blog
post](https://opendreamkit.org/2018/10/17/jupyterhub-docker/).


### Run!

Once you are ready, build and launch the application with

```
docker-compose build --no-cache
docker-compose up -d
```

Read the [Docker Compose manual](https://docs.docker.com/compose/) to
learn how to manage your application.

