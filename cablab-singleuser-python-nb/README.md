## cablab/python-nb Dockerfile


This repository contains **Dockerfile** of a single user Jupyter notebook that is pre-configured with Cab-Lab python API.


### Base Docker Image

* [jupyter/base-notebook:8f56e3c47fec](https://hub.docker.com/r/jupyter/base-notebook/)

### What's available on the Jupyter Notebook?

* Python3 bundled in Conda installation (more detailed on the included packages can be found in the Dockerfile)

* cablab-core (latest)

* gridtools (latest)


### Installation

1. Install [Docker](https://www.docker.com/).
 
2. `docker build -t cablab/python-nb .`
