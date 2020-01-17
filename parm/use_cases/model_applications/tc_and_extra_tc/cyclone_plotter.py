"""
Cyclone Plotter Use case
==================================================================
This use case generates a plot of tropical cyclone tracks using output from
the MET tc-pairs tool.  The CyclonePlotter wrapper does not directly wrap a
specific MET tool.  This is a data visualization written entirely in Python.

"""
##############################################################################
# Scientific Objective
# --------------------
# Provide visualization of storm tracks using output from the MET tc-pairs tool.
# The date and hour associated with each storm track indicates the first time
# the storm was tracked in the model.

##############################################################################
# Datasets
# --------
#
#
#  * Forecast dataset: ADeck non-ATCF tropical cyclone data
#  * Observation dataset: non-ATCF tropical cyclone "best track"(BDeck) cyclone data
#

##############################################################################
# METplus Components
# ------------------
#
# This use case first runs TcPairs and then generates the storm track plot
# for all storm tracks found in the .tcst output file created by the MET tc-pairs tool.
#

##############################################################################
# METplus Workflow
# ----------------
#
# The following tools are used for each run time:
#  TcPairs
#
# To generate TcPairs output, this example loops by initialization time for every 6 hour period that is available
# in the data set for 20150301. The output is then used to generate the plot of all cyclone tracks.
#

##############################################################################
# METplus Configuration
# ---------------------
#
# METplus first loads all of the configuration files found in parm/metplus_config,
# then it loads any configuration files passed to METplus via the command line
# with the -c option, i.e. -c parm/use_cases/model_applications/tc_and_extra_tc/cyclone_plotter.conf
#
# .. highlight:: bash
# .. literalinclude:: ../../../../parm/use_cases/model_applications/tc_and_extra_tc/cyclone_plotter.conf

##############################################################################
# MET Configuration
# -----------------
#
# METplus sets environment variables based on the values in the METplus configuration file.
# These variables are referenced in the MET configuration file. **YOU SHOULD NOT SET ANY OF THESE ENVIRONMENT VARIABLES YOURSELF! THEY WILL BE OVERWRITTEN BY METPLUS WHEN IT CALLS THE MET TOOLS!** If there is a setting in the MET configuration file that is not controlled by an environment variable, you can add additional environment variables to be set only within the METplus environment using the [user_env_vars] section of the METplus configuration files. See the 'User Defined Config' section on the 'System Configuration' page of the METplus User's Guide for more information.
#
# .. highlight:: bash
# .. literalinclude:: ../../../../parm/use_cases/model_applications/tc_and_extra_tc/TCPairsETCConfig
#
#
# See the following files for more information about the environment variables set in these configuration files.
#   parm/use_cases/met_tool_wrapper/TCPairs.py
#
#

##############################################################################
# Running METplus
# ---------------
#
# This use case can be run two ways:
#
# 1) Passing in cyclone_plotter.conf then a user-specific system configuration file::
#
#        master_metplus.py -c /path/to/METplus/parm/use_cases/model_applications/tc_and_extra_tc/cyclone_plotter.conf -c /path/to/user_system.conf
#
# 2) Modifying the configurations in parm/metplus_config, then passing in cyclone_plotter.conf::
#
#        master_metplus.py -c /path/to/METplus/parm/use_cases/model_applications/tc_and_extra_tc/cyclone_plotter.conf
#
# The former method is recommended. Whether you add them to a user-specific configuration file or modify the metplus_config files, the following variables must be set correctly:
#
# * **INPUT_BASE** - Path to directory where sample data tarballs are unpacked (See Datasets section to obtain tarballs). This is not required to run METplus, but it is required to run the examples in parm/use_cases
# * **OUTPUT_BASE** - Path where METplus output will be written. This must be in a location where you have write permissions
# * **MET_INSTALL_DIR** - Path to location where MET is installed locally
#
# Example User Configuration File::
#
#   [dir]
#   INPUT_BASE = /path/to/sample/input/data
#   OUTPUT_BASE = /path/to/output/dir
#   MET_INSTALL_DIR = /path/to/met-X.Y
#
# **NOTE:** All of these items must be found under the [dir] section.
#

##############################################################################
# Expected Output
# ---------------
#
# A successful run will generate a popup window containing a plot of all the cyclone tracks that are in the output .tcst file created
# by the MET tc-pairs tool. Click on the plot to close it.  Now you will observe the following output to both the screen and to the logfile::
#
#    INFO: METplus has successfully finished running.
#
# Additionally, two output files are created.  Refer to the value set for **OUTPUT_BASE** to find where the output data was generated.
# TCPairs output for this use case will be found in tc_pairs/201503 (relative to **OUTPUT_BASE**)
# and will contain files with the following format:
#
# * mlq2015030100.gfso.<*nnnn*>.tcst
#
# where *nnnn* is a zero-padded 4-digit number
#
#
# A plot (in .png format) will be found in the cyclone directory (relative to **OUTPUT_BASE**) along with
# a text file containing data corresponding to the plotted storm tracks:
#
#   * 20150301.png
#
#   * 20150301.txt




##############################################################################
# Keywords
# --------
#
#
#
#
# .. note:: TcPairsUseCase, CyclonePlotterUseCase
