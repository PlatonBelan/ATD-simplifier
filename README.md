# ATD-simplifier

ATD-simplifier is a tool for simplifying of administrative boundaries written as Shapefile or GeoJSON data formats.

Simplification is done by a weighted Visvalingam algorithm. Points located at the vertex of more acute angles are preferentially removed, for a smoother appearance.

## Dependencies
+ [Node.js](https://nodejs.org/en/)
+ [Mapshaper](https://github.com/mbloch/mapshaper#installation)
+ Python3

## Usage
```python
from ATDsimplifier.simplifier import Simplifier
from ATDsimplifier import choose_adaper

adapter = choose_adaper(percentage) #choose the most suitable adapter for a given percentage of remaining vertices
simplifier = Simplifier(input_file, adapter)
simplifier.simplify(percentage)
#output file (*.shp) will be written to ./results/
```




