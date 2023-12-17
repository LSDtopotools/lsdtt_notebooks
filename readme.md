# Notebooks for various lsdtopotools packages

## Getting started

`lsdtopotools` has two components: a command line tool that has very few dependencies, and a python wrapper. 

If you work in linux the command line tool is very stable. You can run it on a rasberry pi if you want. 

The python tools (and geospatial python in general) are not that stable because the packages `gdal` and `proj` are constantly breaking every time some core python module is updated (and that happens a lot). 

If you work in geospatial python and keep your environment maintained so `gdal` is working, then installing `lsdtopotools` and `lsdviztools` in your environment will be a breeze. 

If you do not do that, I suggest either our Docker container or use on Google Colab. The latter has the same problem of `gdal` breaking all the time, but the author of the readme spends 4 hours fixing it every 6 months, so you don't have to. 

### If you use conda/mamba (for WSL, Linux, MacOS)

I'm going to use `mamba` for this since it is faster than `conda`.

1. Make an environment

2. `mamba install lsdtopotools`

3. `pip install lsdviztools`

### If you are in Linux

```console
$ wget https://pkgs.geos.ed.ac.uk/geos-jammy/pool/world/l/lsdtopotools2/lsdtopotools2_0.9-1geos~22.04.1_amd64.deb
$ sudo apt install ./lsdtopotools2_0.9-1geos~22.04.1_amd64.deb
$ pip install lsdviztools
```

### Google colab

Go into the `lsdtopotools` directory and use the button at the top to open one of the many example notebooks in Google colab. 

If you really want to  bootstrap and analysis you need the following cells at the top:

```console
!wget https://pkgs.geos.ed.ac.uk/geos-jammy/pool/world/l/lsdtopotools2/lsdtopotools2_0.9-1geos~22.04.1_amd64.deb  &> /dev/null
!apt install ./lsdtopotools2_0.9-1geos~22.04.1_amd64.deb  &> /dev/null
```

```console
!pip install lsdviztools  &> /dev/null
```


### Microsift Planetary Computer

1. Wait a long time for MPC to give you a server. 
2. `!pip install lsdviztools &> /dev/null`
3. `!mamba install -y lsdtopotools &> /dev/null`
4. I do not know why but this take a very long time. 
4. You should be ready to go. MPC takes longer to spin up. But it has ~32 GB of memory vs ~ 12GB on Google Colab. 

### The Docker container

These instructions are for using our [Docker container](https://hub.docker.com/repository/docker/lsdtopotools/lsdtt_pytools_docker). You can look at the readme there to see instructions for installing Docker.

#### Part 1: set up an LSDTopoTools directory on your host machine

1. You will want to be able to see *LSDTopoTools* output on your host operating system, so you will need to create a directory for hosting your *LSDTopoTools* data, code, and scripts.
2. For the purposes of this tutorial, I will assume you are using Windows and that you have made a directory `C:\LSDTopoTools`.
  * You can put this directory anywhere you want as long as you remember where it is. You don't need to put anything in this directory yet.

#### Part 2: Download and run the container

_Preamble_: The new versions of Docker desktop use winsows linux subsystem to manage memory. The default is to use up all your memory, which is not ideal. To stop this you need to make a little file, called `.wsclonfig`, and put it in your user directory (mine is `C:\Users\smudd`). The file looks like this:
```
[wsl2]
memory=6GB   # Limits VM memory in WSL 2 up to 3GB
processors=1 # Makes the WSL 2 VM use two virtual processors
```
+
you should adjust the memory accordingly. Now, we can run the container. 

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


## Running command line tools

Once you install `lsdtopotools` you will have access to the command line tools. 

Pick one of them (`lsdtt-basic-metrics`, `lsdtt-chi-mapping`, `lsdtt-cosmo-tool`, there are a few others), and fun it with a `-h` flag. For example:

```console
$ lsdtt-basic-metrics -h
```

You will get both a .`csv` and an `.html` with a list of the options. 

## What is in this repository

The notebooks in this repository work with various components of lsdtopotools, so check the readme in each subdirectory, or if that doesn't exist, just open the notebook. The subdirectories are named in a way that hopefully explains their contents.
