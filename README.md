# Tecplot2Vtk

## Intro to VTK

Visualization Toolkit is a software system for computer visualization.

There are two kinds of VTK formats. One is VTK legacy format, which can be edited as easily as txt file, the other is based on XML, which need us to know more about XML format.

More detials can be found in *The VTK User’s Guide 11th Edition*  

## Intro to Tecplot

Tecplot is a post-process software. One of the data file format is modularized .dat file.

## Object

Convert the .dat file to vtk file.

## Methodology

Python, and the package *pyevtk*.

## Outlook

In future, a module in C++ will be developed to generate the vtk file directly from output of model, rather than .tec file.
