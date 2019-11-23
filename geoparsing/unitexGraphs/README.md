# Transducers for FoR parsing

In this work, we enriched a custom version of the [Perdido Geoparser](http://erig.univ-pau.fr/PERDIDO/) adapted for English texts. Our objective is to transform the existing rules and to add new ones in order to retrieve and classify FoR in environmental narratives. 
FoR parsing rules are implemented using transducers in the [Unitex platform](https://unitexgramlab.org/fr) as described below.

FoR parsing rules:




* Betweenness FoR parsing rule

BF = {Target} + *between* + GO + *and* + GO

![Betweenness FoR parsing rule](FoR_BF.png?raw=true "Betweenness FoR parsing rule")


* Euclidean FoR parsing rule

EF CP = {Target + (*at*|*in*)} + modifier orientation + modifier inclusion + GO

EF CD = {Target + (*at*|*in*)} + modifier distance + modifier orientation + GO

EF G = {Target + (*at*|*in*)} + modifier gravity + GO

EF C = {Target + (*at*|*in*)} + modifier orientation + GO

![Euclidean FoR parsing rule](FoR_EF.png?raw=true "Euclidean FoR parsing rule")


* Linear construction FoR parsing rule

LCF S = {Target} + *along* + modifier orientation + modifier inclusion + GO

LCF M = {Target} + *from* + GO + *to* + GO

![Linear construction FoR parsing rule](FoR_LCF.png?raw=true "Linear construction FoR parsing rule")


* Topological FoR parsing rule

TF SP = {Target} + modifier topological + GO

TF I = {Target} + modifier intersect + GO + modifier topological + GO

TF T = {Target} + modifier touch + GO + *and* + GO

TF P = {Target} + modifier inclusion + GO

![Topological FoR parsing rule](FoR_TF.png?raw=true "Topological FoR parsing rule")


* Zonal FoR parsing rule

ZF Dn = {Target} + modifier distance + GO

ZF Do = {Target} + modifier location + GO + *and* + GO 

ZF C = {Target} + *in* + modifier central + GO 

![Zonal FoR parsing rule](FoR_ZF.png?raw=true "Zonal FoR parsing rule")


* Target and Ground object parsing rule

Target = spatial entity

GO = spatial entity + {separator + GO}




Authors:
* Simon Scheider ([home](http://geographicknowledge.de/))
* Ludovic Moncla ([home](https://lmoncla.ddns.net/))
* Gabriel Viehhauser ([home](https://www.ilw.uni-stuttgart.de/institut/team/Viehhauser-00002/))
