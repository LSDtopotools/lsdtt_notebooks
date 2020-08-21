"""Main module and only file?."""
from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.colors as colors # Needed for the discrete colorbars
from mpl_toolkits.axes_grid1 import make_axes_locatable # Help with sizing and locate the colorbars
from pylab import * # we need this for the cm.get_cmap() to work

###############################################################################################
# mkfig functions: functions that create a figure and one or multiple axis objects, preformated.
###############################################################################################


def mkfig_simple_bold(fontsize_major = 12, fontsize_minor = 10, family = "arial" , **kwargs):

  mpl.rcParams["font.weight"] = "bold"
  mpl.rcParams["font.size"] = fontsize_minor
  mpl.rcParams["font.family"] = family
  mpl.rcParams["axes.labelweight"] = "bold"
  mpl.rcParams["axes.labelsize"] = fontsize_major

  fig,ax = plt.subplots(**kwargs)

  return fig,ax


def mkfig_grey_bold(fontsize_major = 12, fontsize_minor = 10, family = "arial" , **kwargs):

  mpl.rcParams["font.weight"] = "bold"
  mpl.rcParams["font.size"] = fontsize_minor
  mpl.rcParams["font.family"] = family
  mpl.rcParams["axes.labelweight"] = "bold"
  mpl.rcParams["axes.labelsize"] = fontsize_major

  fig,ax = plt.subplots(**kwargs)
  ax.set_facecolor('#cccccc')
  ax.grid(ls = '--', color = "w", alpha = 0.5)

  return fig,ax


###############################################################################################
# mod functions: modify an existing axis/figure/text/... object to achieve a new thing
###############################################################################################


def mod_axis_log(fig, ax, x=True, y=True):
  """
    sdfsdfsdfa
  """
  if(x):
    ax.set_xscale('log')
  if(y):
    ax.set_yscale('log')



###############################################################################################
# make functions: functions that create and return something to use in matplotlib (e.g. colorbar, polygon,...)
###############################################################################################

def make_discrete_colormap(use_existing_cmap = True, colormap = "RdBu", n_colors = 4, color_array = None, boundary_array = None):

  # Solution for plotting discrete colorbars with uneven intervals from https://stackoverflow.com/questions/33596491/extract-matplotlib-colormap-in-hex-format
  if use_existing_cmap:
    print("I am making colormap with %s colors from the %s map"%(colormap, n_colors))
    cmap = cm.get_cmap(colormap, n_colors) # Plots n_colour discrete colors
    norm = None
  else:
    print("Using these colours:")
    print(color_array)  
    cmap = colors.ListedColormap(color_array) # set custom colormap
    print("Adding boundaries at:")
    print(boundary_array)
    boundaries = boundary_array # set boundaries between colors, including start and end of colorbar
    norm = colors.BoundaryNorm(boundaries, cmap.N, clip=True)

  return cmap, norm

###############################################################################################
# add functions: functions that add some feature to an existing ax/fig
###############################################################################################


def add_horizontal_colorbar(fig, ax, cb, tick_position = None, tick_labels = None, cbar_label = "I am a label"):
  """
    Makes a horizontal colorbar:
    Arguments:
      fig (matplotlib figure): Default None, in certain cases you may want to add teh basemap plot on the top of an existing. 
      ax (Matplotlib axis): Default None. if custom Figure passed as argument, you also need to pass an axis
      cb: The mappable (e.g. an image) described by this colorbar. 
      tick_position (array): Where do you want your tick labels? Uses matplotlib default if set to None
      tick_labels (array): Tick labels for the colourbar. Uses matplotlib default if set to None
      colorbar_label (str): label of the colorbar if activated.
    Returns:
      Nothing
    Authors:
      Emma Graf
    Date:
      24/07/2020 - last update 24/07/2020
  """
  if(fig is None):
    print("You need to feed me with a figure (add example call here)")

  # This sets the colorbar to the same width as the figure's horizontal axis
  divider = make_axes_locatable(ax)
  cax = divider.new_vertical(size="5%", pad=0.5, pack_start=True)
  fig.add_axes(cax)

  cbar = fig.colorbar(cb, cax=cax, orientation="horizontal")
  if(tick_labels is not None and tick_position is not None):
    cbar.set_ticks(tick_position) # position of the ticks
    cbar.set_ticklabels(tick_labels) # tick labels

  cbar.ax.set_xlabel(cbar_label) # colorbar label