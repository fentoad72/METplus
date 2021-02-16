METplus Release Notes
---------------------

When applicable, release notes are followed by the GitHub issue number which
describes the bugfix, enhancement, or new feature:
https://github.com/dtcenter/METplus/issues
<<<<<<< HEAD

**New in v3.1.1 (20201222)**


Bugfixes:

* Missing dependencies for CyclonePlotter wrapper no longer prevent others wrappers from being used (`#586 <https://github.com/dtcenter/METplus/issues/586>`_)
* Fixed corrupted time information error when running using custom loop list (`#740 <https://github.com/dtcenter/METplus/issues/740>`_)
* Fixed logic preventing StatAnalysis to run with MakePlots (`#743 <https://github.com/dtcenter/METplus/issues/743>`_)


**New in v3.1 (20200810)**
=======
>>>>>>> feature_803_cycloneplotter_line

**New in v4.0**

Bugfixes:

<<<<<<< HEAD
* Running EnsembleStat then GridStat fails when PCPCombine is also run (`#509 <https://github.com/dtcenter/METplus/issues/509>`_)
* All changes included in `3.0.1 <https://github.com/dtcenter/METplus/milestone/11?closed=1>`_ and `3.0.2 <https://github.com/dtcenter/METplus/milestone/13?closed=1>`_ bugfix releases
=======
* Fix bug causing GridStat fatal error (`#740 <https://github.com/dtcenter/METplus/issues/740>`_)
* Add support for comparing inputs using a mix of python embedding and non-embedding (`#684 <https://github.com/dtcenter/METplus/issues/684>`_)
* Fix quick search links (`#687 <https://github.com/dtcenter/METplus/issues/687>`_)
* Align the user guide with get_relativedelta() in time_util.py (`#579 <https://github.com/dtcenter/METplus/issues/579>`_)

Enhancements:
>>>>>>> feature_803_cycloneplotter_line

* Enhance Python embedding logic to allow multiple level values (`#719 <https://github.com/dtcenter/METplus/issues/719>`_)
* Enhance Python embedding logic to allow multiple fcst and obs variable levels (`#708 <https://github.com/dtcenter/METplus/issues/708>`_)
* Add support for a UserScript wrapper (`#723 <https://github.com/dtcenter/METplus/issues/723>`_)
* Add support for a group of files covering multiple run times for a single analysis in GridDiag (`#733 <https://github.com/dtcenter/METplus/issues/733>`_)
* Enhance ascii2nc python embedding script for TC dropsonde data (`#734 <https://github.com/dtcenter/METplus/issues/734>`_, `#731 <https://github.com/dtcenter/METplus/issues/731>`_)
* Support additional configuration variables in EnsembleStat (`#748 <https://github.com/dtcenter/METplus/issues/748>`_)
* Create use case subdirectories (`#751 <https://github.com/dtcenter/METplus/issues/751>`_)
* Handle model, obtype, desc, and regrid dictionary the same in all wrappers (`#755 <https://github.com/dtcenter/METplus/issues/755>`_)
* Ensure backwards compatibility for MET config environment variables (`#760 <https://github.com/dtcenter/METplus/issues/760>`_)
* Combine configuration file sections into single config section (`#777 <https://github.com/dtcenter/METplus/issues/777>`_)
* Add support for skipping existing output files for all wrappers  (`#711 <https://github.com/dtcenter/METplus/issues/711>`_)
* Add support for multiple instance of the same tool in the process list  (`#670 <https://github.com/dtcenter/METplus/issues/670>`_)
* Add GFDL build support in build_components (`#614 <https://github.com/dtcenter/METplus/issues/614>`_)
* Add support for vld_thresh in EnsembleStat (`#621 <https://github.com/dtcenter/METplus/issues/621>`_)
* Decouple PCPCombine, RegridDataPlane, and GridStat wrappers behavior (`#602 <https://github.com/dtcenter/METplus/issues/602>`_)
* Add support for GridStat neighborhood cov thresh (`#620 <https://github.com/dtcenter/METplus/issues/620>`_)
* StatAnalysis run without filtering or config file (`#625 <https://github.com/dtcenter/METplus/issues/625>`_)
* Enhance User Diagnostic Feature Relative use case to Run Multiple Diagnostics (`#536 <https://github.com/dtcenter/METplus/issues/536>`_)
* Enhance PyEmbedIngest to run RegridDataPlane over Multiple Fields in One Call (`#549 <https://github.com/dtcenter/METplus/issues/549>`_)
* Filename templates that have other arguments besides a filename for python embedding fails (`#581 <https://github.com/dtcenter/METplus/issues/581>`_)
* Implement [INIT/VALID]EXCLUDE for time looping (`#307 <https://github.com/dtcenter/METplus/issues/307>`_)
* Add more logging to tc_gen_wrapper (`#576 <https://github.com/dtcenter/METplus/issues/576>`_)
  
New Wrappers:

<<<<<<< HEAD
* TCRMW (`#437 <https://github.com/dtcenter/METplus/issues/437>`_)
* Point2Grid (`#405 <https://github.com/dtcenter/METplus/issues/405>`_)
* GenVxMask (`#387 <https://github.com/dtcenter/METplus/issues/387>`_)
* Grid-Diag (`#490 <https://github.com/dtcenter/METplus/issues/490>`_)

New Use Cases:

* StatAnalysis use case to demonstrate using Python Embedding (`#492 <https://github.com/dtcenter/METplus/issues/492>`_)
* Develop new SWPC use case using_gen_vx_mask (`#427 <https://github.com/dtcenter/METplus/issues/427>`_)
* Create a Feature Relative Use Case with User Diagnostics (`#522 <https://github.com/dtcenter/METplus/issues/522>`_)
* Develop Surrogate Severe Calculation use-case (`#413 <https://github.com/dtcenter/METplus/issues/413>`_)

Enhancements:

* GenVxMask wrapper doesn't handle commas within command line arguments properly (`#454 <https://github.com/dtcenter/METplus/issues/454>`_)
* Enhance PointStat to process one field at a time (`#451 <https://github.com/dtcenter/METplus/issues/451>`_)
* GridStat and other wrappers set input dir to OUTPUT_BASE if not set (`#446 <https://github.com/dtcenter/METplus/issues/446>`_)
* Add curl possibility to build_components build MET script (`#513 <https://github.com/dtcenter/METplus/issues/513>`_)
* Change the shebang lines from "#!/usr/bin/env python" to "#!/usr/bin/env python3" (`#503 <https://github.com/dtcenter/METplus/issues/503>`_)
* Add variable MET_BIN_DIR to replace {MET_INSTALL_DIR}/bin in the code (`#502 <https://github.com/dtcenter/METplus/issues/502>`_)
* File window functionality gives useful message if not enough information provided in filename template (`#517 <https://github.com/dtcenter/METplus/issues/517>`_)
* Enable METplus to only process certain months of a year (`#512 <https://github.com/dtcenter/METplus/issues/512>`_)
* Enhance StatAnalysis/MakePlots to support use defined templates in plotting scripts (`#500 <https://github.com/dtcenter/METplus/issues/500>`_)
* Create Docker image for METplus release (`#498 <https://github.com/dtcenter/METplus/issues/498>`_)
* StatAnalysis wrapper no longer silently fails when no field information is provided (`#422 <https://github.com/dtcenter/METplus/issues/422>`_)
* Allow regrid_data_plane wrapper to input multiple fields (`#421 <https://github.com/dtcenter/METplus/issues/421>`_)
* Expand support for begin_end_incr syntax (`#404 <https://github.com/dtcenter/METplus/issues/404>`_)
* Clean up StringSub/StringExtract calls (`#343 <https://github.com/dtcenter/METplus/issues/343>`_)
* Rearrange ush with subdirs (`#311 <https://github.com/dtcenter/METplus/issues/311>`_)

Internal:

* Change mouse over text for use cases to include config file name (`#400 <https://github.com/dtcenter/METplus/issues/400>`_)
* Setup Initial Integration Test Framework - Travis CI (`#185 <https://github.com/dtcenter/METplus/issues/185>`_)
* Setup new location to house INPUT DATA for testing (`#461 <https://github.com/dtcenter/METplus/issues/461>`_)
* Split up use case tests so it can be run on Travis (`#460 <https://github.com/dtcenter/METplus/issues/460>`_)
* Update Tutorial Chapter 4 for MET 9.0, METplus 3.0 (`#428 <https://github.com/dtcenter/METplus/issues/428>`_)
* Reorganize sphinx documentation files (`#418 <https://github.com/dtcenter/METplus/issues/418>`_)

**New in v3.0 (20200316)**


* Moved to using Python 3.6.3
* User environment variables ([user_env_vars]) and [FCST/OBS]_VAR<n>_[NAME/LEVEL/OPTIONS] now support filename template syntax, i.e. {valid?fmt=%Y%m%d%H}
* Added support for python embedding to supply gridded input data to MET tools (PCPCombine, GridStat, PointStat (gridded data only), RegridDataPlane...
* PCPCombine now supports custom user-defined commands to build atypical use case calls
* Improved logging to help debugging by listing expected file path
* PyEmbedIngester wrapper added to allow python embedding for multiple data sources
* Added support for month and year intervals for [INIT/VALID]_INCREMENT and LEAD_SEQ
* Addition of contributor/developer guide as part of documentation
* Documentation moved online using GitHub Pages and completely renamed, PDF option TBD.
* Bugfix: PCPCombine subtract mode will call add method with 1 file if processing accumulation data and the lead time is equal to the desired accumulation
* Bugfix: PCPCombine add mode forecast GRIB input
* Bugfix: PCPCombine sum mode no longer fails when input level is not explicitly specified

=======
* Met Tool Wrapper: PlotDataPlane/PlotDataPlane_grib1
* Met Tool Wrapper: PlotDataPlane/PlotDataPlane_netcdf
* Met Tool Wrapper: PlotDataPlane/PlotDataPlane_python_embedding
* Met Tool Wrapper: GridStat/GridStat_python_embedding
* Met Tool Wrapper: PyEmbedIngest_multi_field_one_file

New Use Cases:

* Air Quality and Comp: EnsembleStat_fcstICAP_obsMODIS_aod
* Medium Range: UserScript_fcstGEFS_Difficulty_Index
* Convection Allowing Models: MODE_fcstFV3_obsGOES_BrightnessTemp
* Data Assimilation: StatAnalysis_fcstHAFS_obsPrepBufr_JEDI_IODA_interface
* Medium Range: SeriesAnalysis_fcstGFS_obsGFS_FeatureRelative_SeriesByLead_PyEmbed_Multiple_Diagnostics
* Precipitation: EnsembleStat_fcstWOFS_obsWOFS

Internal:

* Append semi-colon to end of _OPTIONS variables if not found (`#707 <https://github.com/dtcenter/METplus/issues/707>`_)
* Ensure all wrappers follow the same conventions (`#76 <https://github.com/dtcenter/METplus/issues/76>`_)
* Refactor SeriesBy and ExtractTiles wrappers (`#310 <https://github.com/dtcenter/METplus/issues/310>`_)
* Refactor SeriesByLead wrapper (`#671 <https://github.com/dtcenter/METplus/issues/671>`_, `#76 <https://github.com/dtcenter/METplus/issues/76>`_)
* Add the pull request approval process steps to the Contributor's Guide (`#429 <https://github.com/dtcenter/METplus/issues/429>`_)
* Remove jlogger and postmsg (`#470 <https://github.com/dtcenter/METplus/issues/470>`_)
* Add unit tests for set_met_config_X functions in CommandBuilder (`#682 <https://github.com/dtcenter/METplus/issues/682>`_)
* Define a common set of GitHub labels that apply to all of the METplus component repos (`#690 <https://github.com/dtcenter/METplus/issues/690>`_)
* Transition from using Travis CI to GitHub Actions (`#721 <https://github.com/dtcenter/METplus/issues/721>`_)
* Improve workflow formatting in Contributers Guide (`#688 <https://github.com/dtcenter/METplus/issues/688>`_)
* Change INPUT_BASE to optional (`#679 <https://github.com/dtcenter/METplus/issues/679>`_)
* Refactor TCStat and ExtractTiles wrappers to conform to current standards
* Automate release date (`#665 <https://github.com/dtcenter/METplus/issues/665>`_)
* Add documentation for input verification datasets (`#662 <https://github.com/dtcenter/METplus/issues/662>`_)
* Add timing tests for Travis/Docker (`#649 <https://github.com/dtcenter/METplus/issues/649>`_)
* Set up encrypted credentials in Travis to push to DockerHub (`#634 <https://github.com/dtcenter/METplus/issues/634>`_)
* Add to User's Guide: using environment variables in METplus configuration files (`#594 <https://github.com/dtcenter/METplus/issues/594>`_)
* Cleanup version info (`#651 <https://github.com/dtcenter/METplus/issues/651>`_)
* Fix Travis tests for pull requests from forks (`#659 <https://github.com/dtcenter/METplus/issues/659>`_)
* Enhance the build_docker_images.sh script to support TravisCI updates (`#636 <https://github.com/dtcenter/METplus/issues/636>`_)
* Reorganize use case tests so users can add new cases easily (`#648 <https://github.com/dtcenter/METplus/issues/648>`_)
* Investigate how to add version selector to documentation (`#653 <https://github.com/dtcenter/METplus/issues/653>`_)
* Docker push pull image repository (`#639 <https://github.com/dtcenter/METplus/issues/639>`_)
* Tutorial Proofreading (`#534 <https://github.com/dtcenter/METplus/issues/534>`_)
* Update METplus data container logic to pull tarballs from dtcenter.org instead of GitHub release assets (`#613 <https://github.com/dtcenter/METplus/issues/613>`_)
* Convert Travis Docker files (automated builds) to use Dockerhub data volumes instead of tarballs (`#597 <https://github.com/dtcenter/METplus/issues/597>`_)
* Migrate from travis-ci.org to travis-ci.com (`#618 <https://github.com/dtcenter/METplus/issues/618>`_)
* Migrate Docker run commands to the METplus ci/jobs scripts/files (`#607 <https://github.com/dtcenter/METplus/issues/607>`_)
* Add stage to Travis to update or create data volumes when new sample data is available (`#633 <https://github.com/dtcenter/METplus/issues/633>`_)
* Docker data caching (`#623 <https://github.com/dtcenter/METplus/issues/623>`_)
* Tutorial testing on supported platforms (`#468 <https://github.com/dtcenter/METplus/issues/468>`_)
* Add additional Branch support to the Travis CI pipeline (`#478 <https://github.com/dtcenter/METplus/issues/478>`_)
* Change $DOCKER_WORK_DIR from /metplus to /root to be consistent with METplus tutorial (`#595 <https://github.com/dtcenter/METplus/issues/595>`_)
* Add all use_cases to automated tests (eg Travis) (`#571 <https://github.com/dtcenter/METplus/issues/571>`_)
* Add support to run METplus tests against multiple version of Python (`#483 <https://github.com/dtcenter/METplus/issues/483>`_)
>>>>>>> feature_803_cycloneplotter_line
