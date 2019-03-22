
Scraped live geolocation data from 1300+ bikes and electric motorbikes. Cleaned, resampled and analyzed data from over 7 milion records.





# Barcelona-Bikes
This project consists of a Jupyter Notebook analyzing data from  over 1300 bikes and electric motorbikes in the city of Barcelona.

Check one of the  Jupyter Notebooks [here](https://nbviewer.jupyter.org/github/pggmrt/barcelona-bikes/blob/master/analytics/analytics-muv.ipynb)

These are some of the results:

#### Heatmap of bikes movement.


![Heatmap](/CARTO_imgs/muv-heatmap.gif)


#### Geolocation analysis and Clustering

As a potential charging route optimization, by setting the number of charging employees as the number of clusters in our clustering algorithms. All bikes will be classified into a number of clusters minimizing charging time.


#### Predictions

Predicted usage and revenue with features impacting urban mobility such as historical weather data, geolocation and sports events, etc. Tested models based on Support Vector Regression, Ridge and Lasso Regressions and ensemble methods (Random Forests, Gradient Boost Regressors). 



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


### Data Acquisition

Set up scrapers on cloud service provider, to scrape data  every 5 minutes from a couple bike providers, and compile it in a single csv file / database.  See scraping scripts in **scrp** directory.

Previously acquired data was cleaned and merged in a single file. 