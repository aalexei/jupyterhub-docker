#Configuration file for JupyterHub

# JupyterHub version: 3.1.1
# Dockerspawner version: 12.1.0
# JupyterHub CAS Authenticator version: 1.0.2

import os
import sys
from dockerspawner import DockerSpawner

c = get_config()


c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
c.JupyterHub.active_server_limit = int(os.environ.get("ACTIVE_SERVER_LIMIT", 60))
c.JupyterHub.activity_resolution = int(os.environ.get("ACTIVITY_RESOLUTION", 30))
c.DockerSpawner.mem_limit = os.environ.get("MEM_LIMIT", "4G")
c.DockerSpawner.cpu_limit = int(os.environ.get("CPU_LIMIT", 1))
c.DockerSpawner.image = os.environ.get("DOCKER_NOTEBOOK_IMAGE", "notebook_img")
c.DockerSpawner.cmd = os.environ.get("DOCKER_SPAWN_CMD", "start-singleuser.sh")
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = os.environ.get("DOCKER_NETWORK_NAME")
c.DockerSpawner.remove = True # Remove containers once they are stopped
c.DockerSpawner.debug = True # For debugging arguments passed to spawned containers
c.JupyterHub.hub_ip = "jupyterhub" # User containers will access hub by container name on the Docker network
c.JupyterHub.hub_port = 9090
c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret" # Persist hub data on volume mounted inside container
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

notebook_dir = os.environ.get("DOCKER_NOTEBOOK_DIR", "/home/user")
c.DockerSpawner.notebook_dir = notebook_dir

c.DockerSpawner.extra_create_kwargs = {'user': 'root'}



c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}


    

# debug = os.environ.get("DEBUG", False)
# if debug:
#     c.Authenticator.admin_users = {"admin"}
#     c.JupyterHub.authenticator_class = "dummy"
#     c.DockerSpawner.debug = True
# else:
c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
#c.PAMAuthenticator.open_sessions = False
c.Authenticator.admin_users = {'admin'}
    

## ----------------------------------------
# JupyterHub Idle Culler
# adapted config from GitHub jupyterhub/jupyterhub-idle-culler
c.JupyterHub.load_roles = [
    {
        "name": "jupyterhub-idle-culler-role",
        "scopes": [
            "list:users",
            "read:users:activity",
            "read:servers",
            "delete:servers",
            # "admin:users", # if using --cull-users
        ],
        # assignment of role's permissions to:
        "services": ["jupyterhub-idle-culler-service"],
    }
]

c.JupyterHub.services = [
    {
        "name": "jupyterhub-idle-culler-service",
        "command": [
            sys.executable,
            "-m", "jupyterhub_idle_culler",
            "--timeout={0}".format(os.environ.get("JUPYTERHUB_IDLE_CULLER_TIMEOUT", "3600")),
        ],
    }
]
