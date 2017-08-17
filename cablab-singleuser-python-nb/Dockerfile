From jupyterhub/singleuser
MAINTAINER Brockmann Consult GmbH <http://www.brockmann-consult.de>

USER root
RUN useradd -m $NB_USER
RUN usermod -u $NB_UID $NB_USER
RUN groupmod -g $NB_GID $NB_USER

USER $NB_USER

# Install python modules
RUN conda install --quiet --yes xarray dask
RUN conda install -c cablab gridtools
RUN conda install -c anaconda --yes basemap=1.0.7
RUN conda install -c conda-forge ffmpeg=2.8.6
USER root
# Install cablab
WORKDIR /srv/jupyterhub
RUN git clone https://github.com/CAB-LAB/cablab-core.git
WORKDIR /srv/jupyterhub/cablab-core
RUN python setup.py install

USER $NB_USER
WORKDIR $DOCKER_NOTEBOOK_DIR
