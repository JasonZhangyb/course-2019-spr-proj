
# Chicago Transit Zones
Nathaniel Smith | BU: smithnj | github: njsmithh </br>
CS504 - Data Mechanics - Project 2

## Intent
The City of Chicago currently has a flat rate of $2.50 for entry into the Elevated Rail ("L")  transit system. Other metropolitan transit systems such as Transport for London's Tube network have fare zones where, depending on your entry and exit into the system, a fare may be higher or lower. While the "L" infrastructure is currently incapable of tracking when passengers exit the system, is it still possible for Chicago to benefit from zone-based fares?

Using data on station popularity, community socioeconomic hardship, and taxi pick-up and drop-off, fare zones can be created for the "L" network that encourage transit in burdened areas of the network while offsetting this fare deficit by charging riders in more stressed parts of the network a higher fare.

### Would a zone based system for the 'L' benefit Chicago?
*Two smaller questions to answer:*
1. *What would the zones look like?* Using the k-means algorithm, zones will be created with a varying number of clusters, taking into account the station popularity, community hardship, and area taxi demand. Each cluster will represent a zone, with all stations in it now residing in that zone.

2. *Do these three metrics obtained show insight into Chicago Transit?* Statistical analysis will be done observing correlation between the three tracked metrics.

3. **Not answered in Project 2 but will be explored later on.** Whether lowering certain fares while increasing other zone fares will produce a similar amount of revenue.
---
Insights:
See generated images for k-means grouping and print statements for correlation coefficients.
---
## Scripts
| Name                     | Purpose                                                                    | Datasets Used                                                  |
|--------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------|
| create_taxiagg           | Calculate taxi ride totals for Community Areas.                            | get_taxitrips                                                  |
| create_stationpopularity | Calculate station popularity statistics.                                   | get_stationstats                                               |
| create_stationhardship   | Match Community Hardship Index with stations.                              | get_censushardship get_stations                                |
| create_metricarray       | Create final metric array of taxi rides, station popularity, and hardship. | create_taxiagg create_stationpopularity create_stationhardship |
| do_kmeans                | Perform k-means analysis on metric array to gather stations into clusters. | create_metricarray                                             |
| do_stats                 | Calculate metric coefficients.                                                               | create_metricarray                                                   |
---
## Data Sets
| Portal             | Name (Source Linked)                                                                                                                 | Filetype |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------|----------|
| Chicago Data Porta | [Census Tract Boundaries](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Census-Tracts-2010/5jrd-6zik)   | .geojson |
| Chicago Data Porta | ['L' Station Statistics](https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Monthly-Day-Type-A/t2rn-p8d7) | .csv     |
| Data.gov           | [Census Hardship Data](https://catalog.data.gov/dataset/census-data-selected-socioeconomic-indicators-in-chicago-2008-2012-36e55)    | .json    |
| Data.gov           | [Chicago Taxi Trip Data](https://catalog.data.gov/dataset/taxi-trips)                                                                | .json    |
| datamechanics.io   | [Chicago L-Stations](https://data.cityofchicago.org/Transportation/CTA-L-Rail-Stations-kml/4qtv-9w43)                                | .geojson |
---
#### Library Dependencies
* pandas, geopandas, numpy
* JSON
* Data Mechanics Library, Provenance, Protoql
* datetime
* sodapy import Socrata
* matplotlib.pyplot
* sklearn
* mpl_toolkits.mplot3d
* from scipy.stats.stats import pearsonr

