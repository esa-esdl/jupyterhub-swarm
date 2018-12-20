## quay.io/esdc/singleuser-r-nb Dockerfile


This repository contains **Dockerfile** of a single user Jupyter Lab that is pre-configured with ESDL Python, Julia, and R APIs


### Base Docker Image

* [quay.io/esdc/singleuser-julia-nb:0.5.2](https://quay.io/repository/esdc/singleuser-julia-nb/)

### What's available on the Jupyter Lab?

* Python3 bundled in Conda installation (more detailed on the included packages can be found in the Dockerfile)

* esdl-core (latest)

* gridtools (latest)

* Julia 0.6.2

* R 3.5


### Installation

1. Install [Docker](https://www.docker.com/).
 
2. `docker build -t esdc/r-nb .` or `docker pull quay.io/esdc/singleuser-r-nb`
