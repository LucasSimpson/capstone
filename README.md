# Capstone #

### This repo contains all code for 2016/2017 ECE Capstone ###

##### James Emmens, Lucas Simpson, Orest Nowasad, Ziyad Mekhemer #####



## Rasterizer ##
Python code that takes high-level commands and spits out a file describing all the LED timings and colors

## Simulator ##
Processing code that takes in the output of the rasterizer and simulates our project visually

## Arduino Code ##
All code that lives on the Arduino. Takes in the output of the rasterizer over USB, processes, streams to blades

## Blade Code ##
Takes stream of data from arduino, saves in memory, plays back sequentially in time

## Routing Slaves ##
Takes stream of data from blade controllers, forwards to correct LED
