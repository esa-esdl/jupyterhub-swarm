# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Configuration file for JupyterHub
import os

c = get_config()

# We rely on environment variables to configure JupyterHub so that we
# avoid having to rebuild the JupyterHub container every time we change a
# configuration parameter.

network_name = os.environ['DOCKER_NETWORK_NAME']
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
#notebook_dir = '/home/' + os.environ.get('NB_USER') + '/work'
notebook_image = os.environ['DOCKER_NOTEBOOK_IMAGE']
notebook_spawn_cmd = os.environ['DOCKER_SPAWN_CMD']
user_workspaces_dir = os.environ['USER_WORKSPACES_DIR']
datacube_dir = os.environ['DATACUBE_DIR']
sample_notebooks_dir = os.environ['SAMPLE_NOTEBOOKS_DIR']

c.JupyterHub.spawner_class = 'cassinyspawner.SwarmSpawner'

#c.JupyterHub.services = [
#    {
#        'name': 'cull-idle',
#        'admin': True,
#        'command': 'python3 cull_idle_servers.py --timeout=300'.split(),
#    }
#]

c.SwarmSpawner.jupyterhub_service_name = os.environ['JUPYTERHUB_SERVICE_NAME']
c.SwarmSpawner.networks = [network_name]
c.SwarmSpawner.placement = ["node.role == worker"]
c.SwarmSpawner.notebook_dir = notebook_dir
mounts = [
     {
        'type' : 'bind',
        'source' : user_workspaces_dir,
        'target' : '/home/esdc'
    },
    {                                                      
    	'type' : 'bind',
    	'source' : datacube_dir,
    	'target' : notebook_dir + '/datacube',
	'read_only': True
    },
    {
        'type' : 'bind',
        'source' : sample_notebooks_dir,
        'target' : notebook_dir + '/shared-nb',
	'read_only': True
    }
]
c.SwarmSpawner.container_spec = {
    # The command to run inside the service
    'args' : [notebook_spawn_cmd],
    'Image' : notebook_image,
    'mounts' : mounts,
# ideally the following parameters can be passed. At the moment produces an error when changing home directory,
# look here https://github.com/jupyter/docker-stacks/issues/442
#    'env': {'NB_UID': 52000, 'NB_GID': 52000, 'NB_USER': 'esdc', 'DOCKER_NOTEBOOK_DIR': notebook_dir},
    'env' : {'JUPYTER_ENABLE_LAB':1},
    'user' : 'root'
}

c.SwarmSpawner.resource_spec = {
	'mem_limit' : int(32 * 1000 * 1000 * 1000),
	'mem_reservation' : int(8 * 1000 * 1000 * 1000)
}
c.SwarmSpawner.start_timeout = 60 * 5
c.SwarmSpawner.http_timeout = 60 * 2
c.SwarmSpawner.service_prefix = os.environ['JUPYTER_NB_PREFIX']

c.MappingKernelManager.cull_idle_timeout = 200
c.NotebookApp.shutdown_no_activity_timeout = 100

# User containers will access hub by container name on the Docker network
c.JupyterHub.hub_ip = '0.0.0.0'

# TLS config
c.JupyterHub.port = 443
c.JupyterHub.ssl_key = os.environ['SSL_KEY']
c.JupyterHub.ssl_cert = os.environ['SSL_CERT']

# Authenticate users with GitHub OAuth
c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'
c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

# Persist hub data on volume mounted inside container
data_dir = os.environ.get('DATA_VOLUME_CONTAINER', '/data')
c.JupyterHub.db_url = os.path.join('sqlite:///', data_dir, 'jupyterhub.sqlite')
c.JupyterHub.cookie_secret_file = os.path.join(data_dir,
    'jupyterhub_cookie_secret')

# Whitlelist users and admins
c.Authenticator.whitelist = whitelist = set()
c.Authenticator.admin_users = admin = set()
c.JupyterHub.admin_access = True
pwd = os.path.dirname(__file__)
with open(os.path.join(pwd, 'userlist')) as f:
    for line in f:
        if not line:
            continue
        parts = line.split()
        name = parts[0]
        whitelist.add(name)
        if len(parts) > 1 and parts[1] == 'admin':
            admin.add(name)
