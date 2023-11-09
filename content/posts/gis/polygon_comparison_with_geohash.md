---
title: Polygon Comparison with Geohash
date: '2022-10-22'
tags: ['gis']
draft: false
description: Polygon Comparison with Geohash
---

## Introduction

Recently, I need to compare two sets of polygons. The polygons between these two sets may have significant differences or very minimal differences. We want to compare the polygons with their centroids, areas, and perimeter with limits.

### Brutce Force algorithm

The most simple algorithm is to compare them one by one. However, for each polygon, it is required to compuare it with all the polygons in another set. The time complexity of the algorithm is O(N^2). This algorithm is too slow if the data set is too large. 

### Geohash based algorithm
#### Build Geohash based dictionary

The first step is to build a dictionary with their centroid's geohash value. The key will be geohash value and the value is the list which contains polygons whose centroids are located inside this geohash.

#### Search 

For each polygon in another set, we firstly calculate the geohash. Then, we search the dictionary with this geohash and its neighboring geohashes according to the differences of area, perimeter, and centroid. Basically, we use geohash and its neighboring geohashes to narrow down our search area. The complexity is reduced to O(N).
