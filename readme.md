# Notebooks for various lsdtopotools packages

## Getting started

The easiest way to get started is to use our [Docker](https://www.docker.com/) container, which has everything pre-installed.

If you don't have Docker, or don't want it, the next best way to install things is through a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

Both the Docker approach and the conda approach are problematic for Windows: Docker installation on Windows is not so easy (and impossible without administrator privileges) and conda will work on windows but the lsdtopotools command line tools do not have a working windows version. We highly recommend you use a Linux emulation system if you are using Windows ([Windows Linux Subsystem](https://docs.microsoft.com/en-us/windows/wsl/install-win10), for example).

### The Docker container

These instructions are for using our [Docker container](https://hub.docker.com/repository/docker/lsdtopotools/lsdtt_pytools_docker). You can look at the readme there to see instructions for installing Docker.

#### Part 1: set up an LSDTopoTools directory on your host machine

1. You will want to be able to see *LSDTopoTools* output on your host operating system, so you will need to create a directory for hosting your *LSDTopoTools* data, code, and scripts.
2. For the purposes of this tutorial, I will assume you are using Windows and that you have made a directory `C:\LSDTopoTools`.
  * You can put this directory anywhere you want as long as you remember where it is. You don't need to put anything in this directory yet.

#### Part 2: Download and run the container

_Preamble_: Once you have downloaded docker, you can control how much memory you give the docker containers. The default is 3Gb. If you have even moderate sized DEM data, this will not be enough. You can go into the docker settings (varies by operating system, use a search engine to figure out where they are) and increase the memory.

1. To get the container, go into a terminal (MacOS or Linux) or Powershell window (Windows) that has docker enabled and run:
```console
$ docker pull lsdtopotools/lsdtt_pytools_docker
```

2. You need to open your docker container with a port: this port will host the [jupyter notebooks](https://jupyter.org/):

```console
# docker run -it -v C:\LSDTopoTools:/LSDTopoTools -p 8888:8888 lsdtopotools/lsdtt_pytools_docker
```

  1. The `-it` means "interactive".
  2. The `-v` stands for "volume" and in practice it links the files in the docker container with files in your host operating system.
  3. After the `-v` you need to tell docker where the directories are on both the host operating system (in this case `C:\LSDTopoTools`) and the container (in this case `/LSDTopoTools`). These are separated by a colon (`:`). Note that you should update the `C:\LSDTopoTools` to reflect the directory structure on your local machine.
  4. the `-p` stand for port. `8888:8888` is the default.
  5. Once you do this you will get a `#` symbol showing that you are inside the container. You can now do *LSDTopoTools* stuff.

3. Two of our packages are already installed in the container, these are `lsdviztools` and `lsdtopytools`. You might also want to install `lsdttparamselector` which includes an interface for running *lsdtopotools* analyses (Warning: the interface is still basic and does not have all the *lsdtopotools* analysis options.)

```console
# pip install lsdttparamselector
```

4. Then, inside the container, start the notebook:

```console
# jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser --allow-root
```

5. When you run this command, it will give you some html addresses. *These will not work from your host computer!!* But these addresses do show you a `token`: you can see it in the address after `token=`.
  1. Instead, go into a browser on your host computer and go to http://localhost:8888/
  2. Then, in the password box, insert the `token` that was shown in the docker container.
  3. Yay, you can now start working with notebooks, using all the fun geospatial stuff that is in this container!


#### Running command line tools

1. The package `lsdttparamselector` allows you to select parameters for the `lsdtopotools` command line tools. These can be run from an ipython notebook using `lsdviztools`. But you can also run the command line tools straight from a terminal window.
1. The command line tools are already install in the docker container. Try `# lsdtt-basic-metrics`
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
2. This will install `lsdttparamselector`, `lsdttviztools`, and `lsdtopytools` from local repositories that the script downloads. This means that you will get the latest version of the tools.
  * Alternatively, you can install some of the tools with the latest tagged version:
  ```console
  $ pip install lsdviztools
  $ pip install lsdttparamselector
  ```
  These tools will then be installed via the `pypi` repository.


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
$ conda install -y gdal rasterio geopandas matplotlib numpy scipy pytables numba feather-format pandas pip pybind11 xtensor xtensor-python fiona utm pyproj cartopy folium h5py lsdtopytools
$ pip install lsdttparamselector lsdviztools
```


### Running the code on google colab

You can set up the tools in google colab as well. Please see the `lsdtopotools_on_colab.ipynb` file in this repository.

## What is in this repository

The notebooks in this repository work with various components of lsdtopotools, so check the readme in each subdirectory, or if that doesn't exist, just open the notebook. The subdirectories are named in a way that hopefully explains their contents.
