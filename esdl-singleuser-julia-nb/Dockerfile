FROM quay.io/esdc/singleuser-python-nb:0.5.7

LABEL maintainer="Brockmann Consult GmbH <http://www.brockmann-consult.de>"
LABEL version="0.5.7"

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
RUN echo 'Pkg.resolve();Pkg.add("IJulia")' > IJulia.jl
RUN echo 'Pkg.add("ECharts");Pkg.add("PyPlot");Pkg.add("PlotlyJS");Pkg.add("GR");Pkg.add("ProgressMeter");Pkg.clone("https://github.com/slundberg/PmapProgressMeter.jl")' > plotpackages.jl
RUN echo 'using Compose, ESDL, GR, ESDLPlots, ProgressMeter, PmapProgressMeter, ECharts, PyPlot' > precomp.jl

WORKDIR /srv/jupyterhub/julia
USER $NB_USER

RUN mkdir -p /home/jovyan/.julia/v0.6
WORKDIR /home/jovyan/.julia/v0.6
RUN git clone https://github.com/esa-esdl/ESDL.jl ESDL
RUN git clone https://github.com/esa-esdl/ESDLPlots.jl ESDLPlots
WORKDIR /home/jovyan/.julia/v0.6/ESDL
RUN git checkout julia06-compat
WORKDIR /home/jovyan/.julia/v0.6/ESDLPlots
RUN git checkout newjulia06
WORKDIR /srv/jupyterhub/julia

ENV ESDL_WORKDIR /home/jovyan/tmp
RUN rm ~/.condarc
RUN /srv/jupyterhub/julia/bin/julia IJulia.jl
RUN /srv/jupyterhub/julia/bin/julia plotpackages.jl
RUN /srv/jupyterhub/julia/bin/julia precomp.jl

WORKDIR /srv/jupyterhub/julia

USER root

WORKDIR /srv/jupyterhub

RUN wget https://julialang-s3.julialang.org/bin/linux/x64/1.1/julia-1.1.0-linux-x86_64.tar.gz
RUN mkdir julia-1.1 && tar xzf julia-1.1.0-linux-x86_64.tar.gz -C julia-1.1 --strip-components 1
USER $NB_USER
ENV ESDL_WORKDIR /home/jovyan/tmp
ENV JULIA_DEPOT_PATH /home/jovyan/julia_depots
WORKDIR /srv/jupyterhub/julia-1.1
RUN /srv/jupyterhub/julia-1.1/bin/julia -e 'using Pkg;pkg"add WebIO@0.6 ColorTypes MultivariateStats IJulia PackageCompiler ProgressMeter GR ECharts PyPlot CSV"'
RUN /srv/jupyterhub/julia-1.1/bin/julia -e 'using Pkg;pkg"add https://github.com/esa-esdl/ESDL.jl#v0.7 https://github.com/esa-esdl/ESDLPlots.jl"'
RUN /srv/jupyterhub/julia-1.1/bin/julia -e 'using Pkg;pkg"add Zarr"'
RUN /srv/jupyterhub/julia-1.1/bin/julia -e 'using Pkg;pkg"precompile"'
RUN /srv/jupyterhub/julia-1.1/bin/julia -e 'using Pkg;pkg"add MultivariateAnomalies#master";pkg"precompile"'
#The following could work when we have the cube in object store, so that unit tests can generate snoop file
#RUN /srv/jupyterhub/julia-1.1/bin/julia -e 'using PackageCompiler;compile_package("ESDL", "ImageMagick","ESDLPlots", force = true)'
WORKDIR /home/jovyan/work
