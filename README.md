# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The goal of this project is to create a model that correctly predicts whether an applicant will be approved for a loan and to deploy this model to AWS.

## Hypothesis

After some quick research these are the factors I think will have an impact. 
Hypothesis 1:  
H1 Credit Score will impact loan approval significantly  
  
Hypothesis 2:  
H1 Income will have a signifcant impact on loan approval  
  
Hypothesis 3:  
H1 Income to loan ratio will have a signifcant impact on loan approval  

For hypothesis 3, while we don't have a comprehensive list of all the liabilities an applicant has, we can use a ratio of the loan amount to their income to get an idea of their income-to-debt ratio.
  

## EDA 

I learnt that income and education are highly correlated, and income and loan amount are highly correlated.
In the case of loan amounts, the minimums are not looking very different, but the maximums and averages are very different so maybe this indicates a difference in the ability to borrow high ammounts.
It also looks like credit history is very important.




## Process
(fill in what you did during EDA, cleaning, feature engineering, modeling, deployment, testing)
1) Reserch and hypothesis building

Usually, I think this is a hugely important part of any project - I always start here. If there is no hypothesis then there is no project. I did some very quick research about what finincial institutions look for in a loan applicant and came up with the hypothses described above.

2) EDA

I ran a lot of quick comparisons and found the observations above. I noticed that the distributions were not normal, and we fixed this in the next step.

3) Feature engineering

I filled in missing features. A detailed explanation of why I chose different strategies for each feture can be found in the Data_Cleaning_3 notebook.
I converted loan amount to a log.
I created a new feature called 'total_income' which was a sum of applicant and coapplicant income and took the log of that
After running an initial random forest, I remembered my hypothesis about the loan ratio and came back and added a very simple ratio of LoanAmount/total_income. This actually improved my results by 2-5% across all 3 of the models I ran.

4) Modelling

I ran 3 models - all classifiers. I ran random forest, xgboost, and svclinear. All 3 did well, but I chose svclinear to deploy because the recall was really good. As a bank I would rather be risk averse.

5) Deployment

 In general, the idea is that I build an api in a flask file, pushed this to docker as an image, pulled the image into my AWS instance, and theoretically it would run and allow me to send a query.

## Results/Demo

SVC Linear results:

Accuracy
0.8319327731092437

Precision
0.8058252427184466

Recall
1.0

Confusion Matrix
[[16 20]
 [ 0 83]]


## Challanges 

I had the most issues with deployment - I still havent resolved this. The issue I run into is that flask tries to import and it can't. "ImportError: cannot import name 'escape' from 'jinja2'". I've tried to update to a version of flask that doesn't do that with no success so my app is uploaded but won't run.

## Future Goals

Right now I want to focus on the deployment - once I can work with a mentor to do this.
I think more features could always be fun - things like total liability, and property type (house/apartment ect), and property use (primary residence/investment/leisure etc) could be useful
I was inspired by Marc's presentation - he spent some time focusing on the biases possibl;e in the dataset eg. would this deprioritize certain communities, and while a bank wouldn't neccessariliy care in terms of their risk investment if it marginalizes groups, it's a good question to ask.