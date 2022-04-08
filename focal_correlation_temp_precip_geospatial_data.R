# Libraries
library(raster)
library(dplyr)
library(mapview)
library(mapedit)
library(sf)
library(readr)
library(ggplot2)

#set working directory i.e. output folder
setwd("F:/collab/pallavi/duststorm/new_data_apr2020/correlation")


TEMP<- raster("F:/collab/pallavi/duststorm/new_data_apr2020/local_spatial_correlation/resample_GIOVANNI-g4.timeAvgMap.M2SDNXSLV_5_12_4_T2MMEAN.20180514-20180514.68E_23N_88E_33N.tif")

PREC <- raster("F:/collab/pallavi/duststorm/new_data_apr2020/local_spatial_correlation/resample_GIOVANNI-g4.timeAvgMap.GPM_3IMERGDF_06_precipitationCal.20180514-20180514.68E_23N_88E_33N.tif")


# Correlation between layers
#cor(values(PREC)[,1],
#    values(TEMP)[,2],
#    use = "na.or.complete")

# Stack covariates
PREC_TEMP_stack <- stack(PREC, TEMP)

# define a new raster that records the positions of values from 1 to ncell
# DEFINITION: The focal correlation is a different way to see the relation between two covariates in space. The idea a simple. Around each cell of the rasters, we define a focal area (square, round, …). For the example, I chose a 3*3 square. We calculate the correlation between the 25 values of each raster in this square using function cor. This local correlation is recorded for the central cell. This operation is repeated over the entire raster thanks to focal function of library {raster}.
#However, we need to use a trick to use the function on two rasters at the same time.

PREC_TEMP_stack_corr <- raster(PREC_TEMP_stack, 1)
values(PREC_TEMP_stack_corr) <- 1:ncell(PREC_TEMP_stack)

matrix_PREC_TEMP_stack <- values(PREC_TEMP_stack) # stack as raster [MW]

focal_cor <- focal(
  x = PREC_TEMP_stack_corr,
  w = matrix(1, 3, 3),
  # fun = function(x, y = PREC_TEMP_stack){ # Original
    # cor(values(y)[x, 1], values(y)[x, 2], # Original
        # use = "na.or.complete")
  # },
  fun = function(x, y = matrix_PREC_TEMP_stack){ # [MW]
    cor(y[x, 1], y[x, 2], # [MW]
        use = "na.or.complete")
  },
  filename = file.path("F:/collab/pallavi/duststorm/duststorm/new_data_apr2020/correlation/", "focal_corr_prec_vs_temp14may.tif"),
  overwrite = TRUE
)