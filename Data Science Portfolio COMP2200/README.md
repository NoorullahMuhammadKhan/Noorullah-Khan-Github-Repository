# Portfolio
This repository comprises the necessary files for the Portfolio task assigned in COMP2200/6200 S1 2023. 

The dataset (Yelp_Portfolio1_Input.csv
) can be accessed via the link provided at https://github.com/COMP2200-S1-2023/portfolio-part-1-dataset/releases/download/portfolio-dataset-p1/Yelp_Portfolio1_Input.csv

# Overall Presentation and Reflective Report

### GITHUB HISTORY-

I submitted onto Github on a regular basis. Whenever, I would complete a few questions, or one big questions, or just before I am about to take a break, I would launch a commit on Github, and push my repository. I did this so that if any accident happens, with my device (power, internet etc) or a technical error with my python files, it will minimise and mitigate the damage done. This is because I will always have many almost uptodate branches that are working in the github. This will allow me to create a new github branch, and continue my work from my most recent viable commit. I believe that commiting reguarly on Github would also allow me to make it easier to potentially share work if I had to work in a group or team.
I had a very important experience with github early on, around the due date of Portfolio 1. An error occured with my file, which made it not become a Json file, and no matter how much I tried to fix it, it woulnd't revert to a normal Json/Python file. I then decided to make a new branch in my github repository from my recent-most error-free commit. Luckily, as I made regular commits, I didn't lose much work. I am still using the new branch I made, for all my next portfolios (P2, P3, P4).
The way I structured my Github, with logical and simple commit titles, and sometimes adding detailed descriptions made it possible for me and the MQ COMP2200 Team to identify whatever work I had done, or my progress with my work. This made it easy to know when a new portfolio was added/started and similarily for the weekly practicals. I labelled each portfolio's start and end origin, and was able to add questions I had done in the Portfolio when comitting. I would almost always push my repository when I commit so that I don't lose any work I had done incase of an unplanned error (as described above).

### REFLECTIVE REPORT:

During this unit of COMP2200, I have learnt alot. Even at the start, using notebooks was easy and simple, as it was almost all self explanatory. An issue I did have at the start was with the installation of Anaconda. I had a lot of troubles when working with Anaconda in Week 1, as even after Anaconda was installed, I would still be unable to open and run the app and it wouldn't appear in my windows. It turned out that I had another copy of Python on my system, so I removed that and did a clean reinstall of Anaconda a few times and eventually it began to work. Myutor, Subash Sagar was very helpful in this process. As I did this unit, and did my fair share of problem solving and troubleshooting I've become more confident in being able to fix installation issues and file, Json issues. I had an issue with a file not being accepted as a Json, and to resolve this, I created a new branch in my portfolio from a recent commit. This again reinforced into me the idea about how important it is to commit regularly. In the future, I am intrested in using these skills I learnt, and the knowledge and experienced gained (about both Coding Python, Data Sciece, and Github) to perform better in my following units and in the workplace. 

#### Portfolio 4

Portfolio 4 was a far more complicated and difficult assignment compared to the others. This is because we had to start from strach, with no questions given and no answers provided. We were not even given a file to work in, so I decided to copy one from a previous portfolio but delete all the cells.
I decided in my portfolio to look at Californian House prices. This was to look at how the longitute, latitute, number of rooms, medium housing age and proximity to water affected the house prices (median and average.) The dataset is could widely be used in the field of machine learning because it provides real-world housing data, making it suitable for analyzing and predicting housing prices. Additionally, as mentioned above the dataset offers interesting insights into factors that affect housing prices in California, such as location, demographics, and economic indicators.
To idenfiy the problem I was targeting to solve in my portfolio, I cleaned my dataset, then made a heatmap. This heatmap, showed correlations between variables in the dataset. I wanted to choose correlations what had atleast a significant correlation, so above 0.5, or below -0.5, so that my machine learning models could actually function, operate and learn the way I intend.
I choose 4 different models, so that I could compare them. I chose polynomial regression and logical regression, because they are traditional and seemed to make sense for the dataset. I choose KNN and Naive Bayers so that I could compare the performance of the tradional regression models to others.

##### Naive Bayers:
It turned out, my datset was not optimised for use with Naive Bayers. This could be because the negative R-squared (R2) value suggests that the model did not fit the data well and performs worse than a simple horizontal line. Naive Bayes Classifier is primarily designed for classification problems and may not be suitable for regression tasks like predicting house prices. 

##### Linear Regression:
This model performs the best among the four models based on the provided metrics. It has the lowest Mean Squared Error (MSE) and Mean Absolute Error (MAE) values, indicating smaller prediction errors. The R-squared (R2) value of 0.6488 suggests that the model can explain around 64.88% of the variance in the target variable. Linear Regression is a traditional and widely used machine learning algorithm. In this case, it demonstrates better predictive power for house prices compared to the other models.

##### Polynomial Regression:
The Polynomial Regression model has higher MSE and MAE values compared to Linear Regression, indicating larger prediction errors. The R-squared (R2) value of -0.5532 indicates that the model does not fit the data well and performs worse than a simple horizontal line. Polynomial Regression is a more complex approach that can capture non-linear relationships between features and the target variable. However, in this case, it does not provide a good fit for the data.

##### KNN Regression:
The KNN Regression model performs better than the Naive Bayes Classifier and Polynomial Regression models but is still outperformed by Linear Regression. It has higher MSE and MAE values compared to Linear Regression, indicating larger prediction errors. The R-squared (R2) value of 0.1091 suggests limited ability to explain the variance in the target variable. KNN Regression is a non-parametric algorithm that uses nearest neighbor information for predictions. While it shows some predictive capability, it falls short compared to Linear Regression.


##### Conclusion
In this assignment, I explored the task of predicting house prices using various machine learning techniques. I started by loading the "California Housing Prices" dataset and performing data cleaning and exploration. I then applied linear regression, polynomial regression, KNN regression, and Naive Bayes classifier to build predictive models and evaluated their performance using different evaluation metrics.

I studied the trends in the data to make findings. My findings were aided by the correlation heatmap which was very helpful. There was was a relationship bewteen house value and number of houses (at that value), house value and total rooms and median income and house values. The other relationships between variables can in a photo("headmap") added to my repository.

Based on the results obtained, here are the key findings:

It can be seen that between median income and median house value, that there seems to be a positive correlation trend. Properties with a higher median income have a higher median house price. This could mean that wealthier people buy wealthier houses.

It can be seen that between median house value and total rooms, that there seems to be a slight bell curve trend. Properties with the average number of total rooms, have a slighly lower, or normal house value. However, there is a solid line at the top of the graph of houses with the highest value but low total rooms. This could potentially be the elite high end mansions for wealthy families.

It can be seen that between median house value and count ((number of houses (at that value)), that there seems to be a bell curve distribution slighly negatively skewed. However, there is a large outlier and the end with there being a not-normal number of properties with the highest value. These could perhaps be the elite luxurious mansions for wealth families.

Linear Regression: The linear regression model achieved a moderate level of accuracy in predicting house prices. It had a reasonable mean squared error (MSE) and mean absolute error (MAE), indicating that it captured a significant portion of the variance in the data. The R-squared value showed that the model explained around 62.5% of the variance in the target variable.

Polynomial Regression: The polynomial regression model showed improved performance compared to linear regression. It captured more complex relationships between the input features and the target variable. However, it also had a higher MSE and MAE compared to linear regression, indicating some level of error in the predictions. The R-squared value indicated that the model explained around 62.5% of the variance, similar to linear regression.

KNN Regression: The KNN regression model had a higher MSE and MAE compared to both linear and polynomial regression models. It showed a weaker performance in predicting house prices, with a lower R-squared value. This suggests that the KNN model might not be the best choice for this particular dataset, as it struggled to capture the underlying patterns in the data.

Naive Bayes Classifier: The Naive Bayes classifier, despite being a classification algorithm, was applied to predict house prices. However, it showed poor performance in terms of regression metrics. The high MSE and MAE values indicate that the Naive Bayes model was not able to accurately predict house prices based on the given features. This could be due to the assumption of feature independence in Naive Bayes, which might not hold true in this dataset.

Overall, linear regression and polynomial regression showed the most promising results among the models tested. However, it's important to note that further refinement of the models, feature engineering, or trying other advanced algorithms could potentially lead to better predictive performance.

In conclusion, accurately predicting house prices is a complex task that requires careful data preparation, feature selection, and model selection. While linear regression and polynomial regression models showed reasonably good performance, there is still room for improvement. Exploring more advanced techniques, incorporating additional features, and fine-tuning the models could potentially enhance the accuracy of the predictions.

In future, I could repeat this, but including more cross verification, to try increase the accuracy of my KNN Regression. Also, I could implement a Neural Network. However, my data would need alot more preparations to iron out any flaws, before the flaw gets magnified 10 or 100 times through the Neural Network's Machine Learning Algorthm. Similarily, I could include a decision tree model.
