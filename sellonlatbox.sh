#!/bin/bash
file="*nc"

for f in $file
    do
    cdo sellonlatbox,76.75,77.5,28.3,29 $f sellonlatbox_$f
    file1=sellonlatbox_$f
    cdo selvar,al $file1 al_$file1
    cdo selvar,skt $file1 skt_$file1
    cdo selvar,e $file1 e_$file1
    cdo selvar,slhf $file1 slhf_$file1
    cdo selvar,str $file1 str_$file1
    cdo selvar,ttr $file1 ttr_$file1
    cdo selvar,sshf $file1 sshf_$file1
    cdo div sshf_$file1 slhf_$file1 bw.nc

    done
