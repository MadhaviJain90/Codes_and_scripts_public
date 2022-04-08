#load libraries
library(raster)
library(rgdal)

#set working directory i.e. output folder
setwd("U:/madhavi/same_resolution/SRFCE_LYR_HGT_0_05DEG")

#x1 is the raster you need to set the resol size similar to
#provide folder detail of input tifs
#resampling will be performed on x2 based on x1 and output is x3

X1 <- readOGR("U:/madhavi/delhi_shp/15km_urban_wgs.shp")
files <- list.files(path="U:/madhavi/same_resolution/SRFCE_LYR_HGT_0_05DEG", pattern="*.tif", full.names=T, recursive=FALSE)
for (i in 1:length(files)) {
X2 <- raster(files[i])
X3<- mask(X2, X1)

newfilename = paste0("clipurban_", basename(files[i]))
outputfolder="U:/madhavi/same_resolution/SRFCE_LYR_HGT_0_05DEG_clipurban/"
newfilepathname = paste0(outputfolder,newfilename)

writeRaster(X3,newfilepathname ,overwrite=TRUE)
}