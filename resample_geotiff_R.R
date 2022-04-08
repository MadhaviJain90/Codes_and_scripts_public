#load libraries
library(raster)
library(rgdal)

#set working directory i.e. output folder
setwd("U:/madhavi/SURFACE_LYR_HGT")

#x1 is the raster you need to set the resol size similar to
#provide folder detail of input tifs
#resampling will be performed on x2 based on x1 and output is x3

X1 <- raster("U:/madhavi/MODIS_LST_DAY/GIOVANNI-g4.timinstalleAvgMap.MYD11C3_006_LST_Day_CMG.2002JJAS.70E_25N_85E_35N.tif")
files <- list.files(path="U:/madhavi/SURFACE_LYR_HGT", pattern="*.tif", full.names=T, recursive=FALSE)
for (i in 1:length(files)) {
X2 <- raster(files[i])
X3<-resample(X2, X1, method="bilinear")
writeRaster(X3, file = paste0("new_", basename(files[i])))
}