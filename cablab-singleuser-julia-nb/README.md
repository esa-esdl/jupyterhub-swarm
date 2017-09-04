## cablab/julia-nb Dockerfile


This repository contains **Dockerfile** of a single user Jupyter notebook that is pre-configured with Cab-Lab Python and Julia APIs.


### Base Docker Image

* [cablab/python-nb:f2218c9](https://hub.docker.com/r/cablab/python-nb/)

### What's available on the Jupyter Notebook?

* Python3 bundled in Conda installation (more detailed on the included packages can be found in the Dockerfile)

* cablab-core (latest)

* gridtools (latest)

* Julia 0.5.0


### Installation

1. Install [Docker](https://www.docker.com/).

2. `docker build -t cablab/julia-nb .`
