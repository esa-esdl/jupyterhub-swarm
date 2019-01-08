FROM jupyter/base-notebook:03b897d05f16
LABEL maintainer="Brockmann Consult GmbH <http://www.brockmann-consult.de>"
LABEL version="0.5.3"

ADD start2.sh /usr/local/bin/start.sh

USER root
RUN sudo apt-get update
RUN sudo apt-get upgrade -y
RUN sudo apt-get install -y git unzip

USER $NB_USER

# Install python modules
RUN conda install --quiet --yes -c conda-forge -c cablab -c anaconda -c numba \
    nomkl \
    ipywidgets=7.2.1 \
    widgetsnbextension \
    pandas \
    numexpr \
    matplotlib=2.0* \
    scipy \
    seaborn \
    scikit-learn \
    scikit-image \
    cython=0.25* \
    numba \
    bokeh \
    hdf5 \
    h5py \
    xarray \
    zarr \
    dask \
    gridtools  \
    basemap=1.0.7 \
    ffmpeg=2.8.6 \
    netcdf4=1.2* \
    pyproj \
    datashader
    
RUN conda list

# Activate ipywidgets extension in the environment that runs the notebook server
# RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix

# Install and activate interactive widget in jupyterlab
RUN jupyter lab clean
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager
RUN jupyter labextension list
RUN jupyter labextension install jupyterlab_bokeh

# Import matplotlib the first time to build the font cache.
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot"

USER root

# Install esdl
WORKDIR /srv/jupyterhub
RUN git clone https://github.com/esa-esdl/esdl-core.git
WORKDIR /srv/jupyterhub/esdl-core
RUN python setup.py install


WORKDIR /tmp
RUN wget https://obs-sdk-download.obs.eu-de.otc.t-systems.com/eSDK_Storage_OBS_V2.1.21_Python.zip
RUN unzip eSDK_Storage_OBS_V2.1.21_Python.zip; \
        cd src && python setup.py install

USER $NB_USER
WORKDIR /home/jovyan/work
