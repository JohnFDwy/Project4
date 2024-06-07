# Project 4

PROJECT URL: https://project4-0y0i.onrender.com

In this project we took the data stored in the vehicles_us.csv file and used it to look for trends information. 

First, we cleaned the data and filled in missing values. For columns "model_year" and "odometer", the missing data was filled using the median() method to fill in the missing values with the median value of the set. This is because the outliers we significant enough to impact the mean of our data and would not be representative of the dataset. 

After plotting some data on scatterplots to look for interesting patterns it became clear that price and mileage on a car were related, when odometer readings went up, price typically went down. 

Once the data had been cleaned, the graphs plotted and stored in our app.py file, the whole project was pushed back to GitHub and then connected to render in order to create out web application that shows the relationship between price of a car and the odometer mileage.
