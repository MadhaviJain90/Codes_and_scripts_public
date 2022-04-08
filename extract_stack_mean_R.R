library(raster) #load raster package

#set working directory i.e. output folder
setwd("U:/madhavi/same_resolution/AOD_0_05DEG_cliprural")

#create list of raster file paths
rasterlist <- list.files(path="U:/madhavi/same_resolution/AOD_0_05DEG_cliprural", pattern="*.tif", full.names=T, recursive=FALSE)

outlist <- list() #create empty list to store outputs from loop

for (i in 1:length(rasterlist)) { #for each raster in rasterlist
   r <- raster(rasterlist[[i]]) #read eoulement i of rasterlist into R
   val <- getValues(r) #get raster values
   m <- mean(val,na.rm=T) #remove NAs and compute mean
   outlist[[i]] <- c(rasterlist[[i]],m) #store raster path with mean
   #return("complete")
}

df <- data.frame(do.call(rbind,outlist)) #convert list to data frame
colnames(df) <- c("raster_path","mean")
row.names(df) <- df$raster_path

write.csv(df,file = "AOD_MEAN_RURAL.csv")