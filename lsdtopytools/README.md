# `lsdtopytools`: Cross-platform `python` portage of LSDTopoTools

`lsdtopytools` is a `python` package provinding a `python` interface to LSDTopoTools (_i.e_ without the need of running `c++` tools separately, or with `subprocess`). It links behind the scenes and in memory the `c++` codes with `xtensor` and `pybind11` to take full advantage of `c++` speed with `python` flexibility. LSDTopoTools is a topographic analysis research software with a focus of fluvial and hillslope geomorphology. `lsdtopytools` is cross-platform and available on conda-forge (= easy to install). 

## What does this sub-repository contains?

When it comes to using scientific softwares, I believe in a practical approach. In this readme you will find the installation instructions. Use Quickstart if you are comfortable with the principle of `python`, `conda` and `jupyter`. The rest mostly explains these, and may detail quickly what are each notebooks.

The rest of the repo contains practical examples using `lsdtopytools` to produce topographic analysis.

# Quickstart

This Quick start section assumes you are confortable the basics of `python`, `conda` and `jupyter`. See appendices first if you need introduction to these tools.

- Install anaconda environment manager (miniconda is enough) for python 3

- (optional) create a new conda env: `conda create -n lsdtopytools python=3.7` and activate it `conda activate lsdtopytools`

- install `lsdtopytools`: `conda install -c conda-forge lsdtopytools`

- install `jupyter-lab`: `conda install -c conda-forge jupyterlab` 

- clone this repository: `git clone https://github.com/LSDtopotools/lsdtt_notebooks` and `cd` to the `lsdtopytools` directory

- run `jupyter lab` (also work with the older version `jupyter notebook`) and you will have access to the tutorial notebooks

And you are good to go. This repository contains a number of notebooks describing different uses of `lsdtopytools`.


# Appendix A: What is conda and why

The first thing to have in mind to understand the need of `conda` is the concept of _python environment_. One could describe `python` as a _glue_ language: it is an interpreted language, where each line of code is actually calling already compiled routines on C/Fortran/C++/... behind the scene from many different packages unified within its simple syntax. Basically, if you need any numerical thing to be done, it has probably already been coded by someone and you can just use it with `python` without reinventing the wheel. However this raises a problem: your `python` interpreter needs to know where to find this tools you want to use. Moreover, your tools will rely itself on other packages and python needs to find them as well. This is a _python environment_: a box inside your computer where all the different codes you want to use are located and can find each otehr to function properly. 

As a comparison, softwares like QGIS, ArcGIS or MATLAB comes with their own boxes, more or less rigid and can function on their own after installation. `python` is open-source: you can always expand your box with content from anyone in the community, or with a package realesed by a company or whatever. However this also makes the management of this box tricky: there can be dependencies conflict, version issues, some code badly maintain, ... 

That's where `conda` comes being very handy: it automates and manages all of these things for you. It creates box(es) within your computer (not physical boxes eh) and you can install whatever you need within these boxes. It manages conflict, proper installation, and allow scientists install codes easily without the need of computer science knowledge. It also helps scientists develloping codes, _e.g_ for `lsdtopytools`: we do not need to compile our code for every types of computers, `conda-forge` does it for us so we can distribute our code to anyone who needs it.

## Installing conda

You can find the miniconda installers [there](https://docs.conda.io/en/latest/miniconda.html). Miniconda is just a lighter version of Anaconda, both are installing the same tool `conda` but with more or less stuff around (long story short, it does not matter for you). Depending on your platform, follow the instructions either by UI or terminal. At the end of the installation it will guide you on how to activate it within the terminal of your computer. On Windows, you will even install a dedicated terminal called (I think) `conda prompt`.

## Working with environments

An environment is a box within your computer. A `conda` environment only needs to be created once, but will need to be activated each time you open a new terminal and want to use this specific environment.

To create an environment: `conda create -n NameOfYourEnvironment`

To activate your environment: `conda activate NameOfYourEnvironment` the start of the line in your terminal should now display `(NameOfYourEnvironment)`. 

**Anything you install in the environment remains installed, you do not need to reinstall all the packages at each activation. Just at the creation.**


## Installing packages

Installing a package is easy if (like most common packages) they have a conda package. The principle is to pull a package from a channel (_i.e_ a repository containing the binaries). I strongly recommend `conda-forge`, which contains most of what you will need for scientific computing.

The syntax is as follow: `conda install -c conda-forge NameOfPackage`

Multiple packages can be installed at once, for example, if I want `numpy` and `numba`: `conda install -c conda-forge numpy numba`

Dependencies are managed automatically behind the scenes and will be installed if needed.

**Tips to speed up things**: You will realise that if you install a new package in an already busy environment, it takes time. [Quantstack](https://quantstack.net/) is developping a drop-in replacement speeding up the process (drastically). You can install it with conda: `conda install -c conda-forge mamba` and simply replace `conda` with `mamba` when **installing** a package (this is just for installation, not environment management). E.g `mamba install -c conda-forge lsdtopytools`

## Capricious dependencies

In some rare cases, some dependencies can be very unstable (most of the time when `GDAL` is involved). It will install without errors, but will crash at use/import. This may be because the base conda channel and the `conda-forge` channel conflicts. The following practice resolves some of that: at the first activation of the environment, before any installation, run the following commands:

```
conda config --add channels conda-forge
conda config --set channel_priority strict
```

What does it do: it makes sure it prioritises the packages from `conda-forge` before considering the official `anaconda` channel (the default one). Ot makes sure that all the installations come from the same source.

## Unsolvable dependencies

Some heavy/old packages can conflict if they are not maintained anymore, or are relying on many compiled, hard-to-manage dependencies. At installation you will get a nasty message telling you it cannot be installed. Unfortunately there is no easy fix to that. You can start with a clean environment and install the problem-bearing package first, and then hope that it will be fixed. Otherwise you will need to play with the versions of all your packages and downgrade them until it works. **This is very rare**. If the package is available _via_ `pip`, it is worth a try to `pip install NameOfPAckage`, sometimes it works (it is a bad practice but meh).

## Non-conda packages

Some codes are not distributed through `conda-forge`. Having uploaded `lsdtopytools` to `conda-forge`, I understand not everyone can dedicate time to do this, even if the process is nicely documented. In that case you can still install the package within your environment, depending on how it is distributed.

### Case 1: the package is on pip

In that case, `conda` and `pip` can be utilised jointly. Simply run `pip install NameOfPackage` to install it. It will let you know if it succeeded or failed. Pip is another, lighter-but-less-powerful package manager for `python`. It struggles with binaries (when some compiled code needs to be installed) so it might be worth checking if you can install the dependencies with `conda` and then utilise `pip` to install the wanted package.

### Case 2: the package has a setup.py

If the package has a `setup.py` file, it can be installed. The cleanest way is to do the following:

- clone the repository

- in the terminal, with your environment activated, run `pip install .`

- **IF IT FAILS** `python setup.py bdist_wheel` it will create a `dist` folder with a `XXX.whl` file which can be installed with `pip install dist/XXX.whl` (replace with relevant name of course, also note that I did not cd to the dist directory).










































<!-- end of file -->