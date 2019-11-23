# Repository of resources for discovering spatial Frames of Reference (FoR) in narratives

In order to transform locative expressions contained in narrative texts to coordinate systems in a GIS, it is necessary to identify the different types of cognitive frames of reference (FoR) used within parts of speech (PoS).

This repository contains computational resources as well as annotation and validation files used to automatically geoparse FoRs in texts. Source texts include:
* Murray's 'Undiscovered Scotland' 
* McFarlane's 'The Wild places' 
* Stevenson's 'Kidnapped'

Folders include:
1. Annotation: Manual annotation files (.tsv)
2. Geoparsing: Geoparser resources, outputs and their quality (.tsv and geoparsing rules)
3. GISmodels: Python models for approximating FoR georeferences. Tests can be run with [pytest](https://docs.pytest.org/en/latest/) by executing `pytest` in the repository's root folder.
