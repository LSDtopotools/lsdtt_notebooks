# Notebooks for various lsdtopotools packages

## Getting started

The easiset way to get started is to use our Docker container, which has everything pre-installed.

If you don't have docker, or don't want it, the next best way to install things is through a conda environment.

Both the docker approach and the conda appraoch are problematic for Windows: docker installation on windows is not so easy (and impossible without administrator privileges) and conda will work on windows but the lsdtopotools command line tools do not have a working windows version. We highly reccomend you use a linux emulation system if you are using Windows (Windows Linux Subsystem, for example).

### The docker container

These instructions are for using our [Docker container](https://hub.docker.com/repository/docker/lsdtopotools/lsdtt_pytools_docker). You can look at the readme there to see instructions for installing Docker.

#### Part 1: set up an LSDTopoTools directory on your host machine

1. You will want to be able to see *LSDTopoTools* output on your host operating system, so we will need to create a directory for hosting your *LSDTopoTools* data, code, and scripts.
2. For the purposes of this tutorial, I will assume you are using windows and that you have made a directory `C:\LSDTopoTools`.
  * You can put this directory anywhere you want as long as you remember where it is. You don't need to put anything in this directory yet.

#### Part 2: Download and run the container

_Preamble_: Once you have downloaded docker, you can control how much memory you give the docker containers. The default is 3Gb. If you have even moderate sized DEM data, this will not be enough. You can go into the docker settings (varies by operating system, use a search engine to figure out where they are) and increase the memory.

1. To get the container, go into a terminal (MacOS or Linux) or Powershell window (Windows) that has docker enabled and run:
```console
$ docker pull lsdtopotools/lsdtt_pytools_docker
```
2. Now you need to run the container:
```console
$ docker run -it -v C:\LSDTopoTools:/LSDTopoTools lsdtopotools/lsdtt_pytools_docker
```
  1. The `-it` means "interactive".
  2. The `-v` stands for "volume" and in practice it links the files in the docker container with files in your host operating system.
  3. After the `-v` you need to tell docker where the directories are on both the host operating system (in this case `C:\LSDTopoTools`) and the container (in this case `/LSDTopoTools`). These are separated by a colon (`:`).
3. Once you do this you will get a `#` symbol showing that you are inside the container. You can now do *LSDTopoTools* stuff.



#### Running command line tools

1. Command line tools are ready for use immediately. Try `# lsdtt-basic-metrics`
2. To see what is possible, check out the following documentation:
  * Note: for the below instructions, you will need the example datasets. Grab these with `# sh Get_LSDTT_example_data.sh`
  * https://lsdtopotools.github.io/LSDTT_documentation/LSDTT_basic_usage.html
  * https://lsdtopotools.github.io/LSDTT_documentation/LSDTT_channel_extraction.html
  * https://lsdtopotools.github.io/LSDTT_documentation/LSDTT_chi_analysis.html

#### Installing local python packages

1. We include a script to install some local python packages. To run, use:

```console
# install_lsdtt_python_packages.sh
```
2. This will install `lsdttparamselector`, `lsdttviztools`, and `lsdtopytools`.

#### Running a jupyter notebook from this container

1. The lsdpytools container can also serve as a host for [jupyter notebooks](https://jupyter.org/)
2. You need to open your docker container with a port:

```console
# docker run -it -v C:\LSDTopoTools:/LSDTopoTools -p 8888:8888 lsdtopotools/lsdtt_pytools_docker
```

  * Note that you should update the `C:\LSDTopoTools` to reflect the directory structure on your locak machine.

3. Then, inside the container, start the notebook:

```console
# jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser --allow-root
```

4. When you run this command, it will give you some html addresses. *These will not work from your host computer!!* But these addresses do show you a `token`: you can see it in the address after `token=`.
  1. Instead, go into a browser on your host computer and go to http://localhost:8888/
  2. Then, in the password box, insert the `token` that was shown in the docker container.
  3. Yay, you can now start working with notebooks, using all the fun geospatial stuff that is in this container!

### Installing in a conda environment

1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) on your computer (use the 64 bit python 3.7 version)

2. Start with some conda housekeeping

```console
$ conda install -y -c conda-forge conda
$ conda config --add channels conda-forge
$ conda config --set channel_priority strict
```

3. Make a conda environment. We'll used python 3.8

```console
$ conda create -n lsdtt python=3.8
$ conda activate lsdtt
```

4. Then run these conda commands. Warning! This will take a **LONG** time.

```console
$ conda install -y lsdtopotools
$ conda install -y git python=3
$ conda install -y ipython ipykernel jupyter
$ conda install -y conda-build
$ conda install -y gdal rasterio geopandas matplotlib numpy scipy pytables numba feather-format pandas pip pybind11 xtensor xtensor-python fiona utm pyproj cartopy folium h5py
```

## What is in this repository

The notebooks in this repository work with various components of lsdtopotools, so check the readme in each subdirectory. The subdirectories are named in a way that hopefully explains their contents.
