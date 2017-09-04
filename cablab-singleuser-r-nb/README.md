## cablab/r-nb Dockerfile


This repository contains **Dockerfile** of a single user Jupyter notebook that is pre-configured with Cab-Lab Python, Julia, and R APIs


### Base Docker Image

* [cablab/julia-nb:695e8dd](https://hub.docker.com/r/cablab/julia-nb/)

### What's available on the Jupyter Notebook?

* Python3 bundled in Conda installation (more detailed on the included packages can be found in the Dockerfile)

* cablab-core (latest)

* gridtools (latest)

* Julia 0.5.0

* R


### Installation

1. Install [Docker](https://www.docker.com/).
 
2. `docker build -t cablab/r-nb .`
