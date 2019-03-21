

# Barcelona-Bikes
This project consists of a Jupyter Notebook analyzing data from  over 1300 bikes and electric motorbikes in the city of Barcelona.

Check one of the  Jupyter Notebooks [here](https://nbviewer.jupyter.org/github/pggmrt/barcelona-bikes/blob/master/notebooks/analytics-muv.ipynb)

These are some of the results:

#### Heatmap of bikes movement.


![Heatmap](/CARTO_imgs/muv-heatmap.gif)


#### K-means clustering
As a potential charging route optimization, set number of charging employees as number of clusters. All bikes will be classified into a number of clusters maximizing proximity to each other. Here 5 clusters were used.


![Clustering](/CARTO_imgs/5clusters.png)

#### Predictions

Aemet weather data.




### Requirements:
* Python 3
* Pandas
* Numpy
* scipy
* geopy
* scikit-learn
* mpleaflet
* mtplotlib
* CARTOframes

### Acquire Data
Set up scrapers on any cloud service provider, to scrape data  every 5 minutes from a couple bike providers, and compile it in a single csv file.  See scraping scripts in **scrp** directory.

Previously acquired data was cleaned and merged in a single file. 
