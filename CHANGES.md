## Version 0.6.1

* Added latest [xcube version](https://github.com/dcs4cop/xcube)
* Including aws.s3

## Version 0.6.1.dev1

* Creation of Docker Baseimage: jupyter/datascience-notebook:eb149a8c333a to minimise build time
* Update of jupyterhub and jupyterlab to version 1.0.0
* Including rgdal, reticulate, aws.s3 and rgeos into dependencies
* fix julia build. Replaced json package version by removing dependency 
  Gadfly and explicitly installing latest version of package JSON
* Set PYTHONPATH and PYTHONUSERBASE to $HOME/work/workspace/.local allowing persistent user installs



## Version 0.6.0

* Using the data science notebook now
* Added a Julia package that allows to read and write zarrs to an object store

## Version 0.5.2

* Julia - new packages ECharts, PyPlot, ProgressMeter


## Version 0.5.1

* Use ipywidgets 7.2.1 and install the jupyterlab extension

## Version 0.5.0

* Python - add zarr conda package
* R - use R version 3.5 after an update of ubuntu OS to bionic