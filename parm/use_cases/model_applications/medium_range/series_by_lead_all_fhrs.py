#
#  DIRECTORIES
#
[dir]
# Create another directory to differentiate from other series by lead output
SERIES_ANALYSIS_FILTERED_OUTPUT_DIR = {OUTPUT_BASE}/series_lead_filtered
SERIES_ANALYSIS_OUTPUT_DIR = {OUTPUT_BASE}/series_analysis_lead


#
#  CONFIGURATIONS
#
[config]
PROCESS_LIST = TcPairs, ExtractTiles, SeriesByLead

# Variables and levels of interest
BOTH_VAR1_NAME = TMP
BOTH_VAR1_LEVELS = P850
BOTH_VAR2_NAME = HGT
BOTH_VAR2_LEVELS = P500

# Statistics of interest (Must always have include TOTAL)
SERIES_ANALYSIS_STAT_LIST = TOTAL, FBAR, OBAR, ME

#TC-STAT filtering options used to extract tiles
EXTRACT_TILES_FILTER_OPTS = -basin ML

# The init time begin and end times, increment, and last init hour.
INIT_TIME_FMT = %Y%m%d
INIT_BEG = 20141214
INIT_END = 20141214
INIT_INCREMENT =  21600


SERIES_ANALYSIS_CONFIG_FILE = {PARM_BASE}/use_cases/feature_relative/met_config/SeriesAnalysisConfig_by_lead

SERIES_ANALYSIS_REGRID_TO_GRID = latlon 60 60 23 -115 0.5 0.5

# if true, run series_by_lead for groups of forecasts
#  must set LEAD_SEQ_[N] and LEAD_SEQ_[N]_LABELS for N > 0 groups
# if false, run series_by_lead for all forecast hours
#  must set LEAD_SEQ
SERIES_ANALYSIS_GROUP_FCSTS = False

# Used for performing series analysis based on lead time
LEAD_SEQ = begin_end_incr(0,96,6)

