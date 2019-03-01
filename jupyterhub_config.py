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

# Authenticate users with GitHub OAuth
# c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'
# c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

c.JupyterHub.spawner_class = 'wrapspawner.ProfilesSpawner'
c.Spawner.http_timeout = 120

c.ProfilesSpawner.profiles = [
               ( "Host process", 'local', 'jupyterhub.spawner.LocalProcessSpawner', {'ip':'0.0.0.0'} ),
                      ('Docker Python 2/3', 'systemuser', 'dockerspawner.SystemUserSpawner', dict(container_image="jupyterhub/systemuser")),
                             ('Docker Python 2/3,R,Julia', 'datasciencesystemuser', 'dockerspawner.SystemUserSpawner', dict(container_image="jupyterhub/datasciencesystemuser")),
                              ]


c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'


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


c.template_vars = {'announcement': 'some_text'}
