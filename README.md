
# Barcelona-Bikes

Scraped live geolocation data from 1300+ bikes and electric motorbikes. Cleaned, resampled and analyzed data from over 7 milion records.

If notebook does not render on github, use this [NBviewer link](https://nbviewer.jupyter.org/github/marcpgg/barcelona-bikes/blob/master/analytics/analytics-muv.ipynb).



### Data Acquisition

Set up scrapers on cloud service provider, to scrape data  every 5 minutes from a couple bike providers, and compile it in a single csv file / database.  See scraping scripts in **scrp** directory.

Previously acquired data was cleaned and merged in a single file. 

#### Geolocation analysis and Clustering

Clustering as a potential way to optimize driving routes for employees in charge of charging the bikes overnight. Number of clusters could be assigned to the number of charging employees. All bikes will be classified into a number of clusters minimizing the time it takes to charge all bikes.


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





These are some of the results:

#### Heatmap of bikes movement.


![Heatmap](/CARTO_imgs/muv-heatmap.gif)
