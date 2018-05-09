From quay.io/esdc/singleuser-python-nb:0.3
LABEL maintainer="Brockmann Consult GmbH <http://www.brockmann-consult.de>"

# Install Julia
USER root
WORKDIR /srv/jupyterhub
RUN apt-get update
RUN apt-get -y install apt-utils
RUN apt-get -y install r-base r-recommended libcurl4-gnutls-dev libssl-dev libnetcdf-dev libudunits2-dev udunits-bin libhdf5-dev libzmq3-dev cmake libmagickwand-dev
RUN wget https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.2-linux-x86_64.tar.gz
RUN mkdir julia && tar xzf julia-0.6.2-linux-x86_64.tar.gz -C julia --strip-components 1
RUN PATH="/srv/jupyterhub/julia/bin:$PATH"
WORKDIR /srv/jupyterhub/julia
RUN echo 'Pkg.add("IJulia")' > IJulia.jl
RUN echo 'Pkg.clone("https://github.com/CAB-LAB/CABLAB.jl");Pkg.clone("https://github.com/CAB-LAB/CABLABPlots.jl")' > installcablab.jl
RUN echo 'Pkg.add("PlotlyJS");Pkg.add("GR")' > plotpackages.jl
RUN echo 'using Compose; using CABLAB; using PlotlyJS; using GR; using CABLABPlots' > precomp.jl

WORKDIR /srv/jupyterhub/julia
USER $NB_USER
RUN export CABLAB_WORKDIR="/home/jovyan/work/tmp"
RUN /srv/jupyterhub/julia/bin/julia IJulia.jl
RUN /srv/jupyterhub/julia/bin/julia installcablab.jl
RUN /srv/jupyterhub/julia/bin/julia plotpackages.jl

WORKDIR /srv/jupyterhub/julia
RUN /srv/jupyterhub/julia/bin/julia precomp.jl

USER $NB_USER
WORKDIR /home/jovyan/work
