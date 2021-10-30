# Arkham-Rainfall-Predictor
**About 96 percent Accurate prediction of rainfall in the regions of Arkham county. 
Deployed using flask.**

**Arkham county is in bad shape already. So, least we can do is to forecast the rain in the regions of Arkham county to 
give them a heads up. So, we are going to build the Rainfall predictor to forcast the rain possiblity with 96 percent accuracy.
The model had been trained by the Xgboost Classifier, which out performed other models like 'Logistic Regression','Decision Tree','Neural Network','Random Forest',
'LightGBM','CatBoost', and finally Ensemble.
We all want the best for the Arkham.
**

## Here's how to run it:
You can run through Visual Studio or through Command Prompt

1. run "pip install -r requirements.txt" in your shell"

2. Then simply run the app.py. 


## Deployed site will look like this.

![Screenshot (94)](https://user-images.githubusercontent.com/72303641/136688139-250512b0-13fa-41b8-9ea6-95b1dfd07979.png)


## Data Preparation
![image](https://user-images.githubusercontent.com/72303641/138696813-fc2519c8-db5e-453a-b3d6-b661f746f931.png)
 
## Handling the imbalance data:
![image](https://user-images.githubusercontent.com/72303641/138696854-83cdf604-21e0-4e37-a8fc-248d14266bd5.png)
![image](https://user-images.githubusercontent.com/72303641/138696906-942989f3-0855-4399-adc6-91caf7307bf6.png)

## Handling the Missing data:
![image](https://user-images.githubusercontent.com/72303641/138696977-3ced5126-0216-4839-bfde-acb000430511.png)
 
## Imputation and Transformation
![image](https://user-images.githubusercontent.com/72303641/138697116-bbfb5c5d-db3d-483d-81dc-e43e7f88cf79.png)
![image](https://user-images.githubusercontent.com/72303641/138697161-4e07b781-e43e-44b8-a815-740ab7524859.png)



## Eliminating the outliers:
![image](https://user-images.githubusercontent.com/72303641/138697200-28faf806-19d2-4bfa-92f1-4ad1a048aa18.png)
![image](https://user-images.githubusercontent.com/72303641/138697291-eea4c06d-ad5a-462b-b167-081350da4226.png)

 
## Heat map of the Data:
![image](https://user-images.githubusercontent.com/72303641/138697243-42759c81-5b95-4d7f-b3eb-f4e12f2ab2db.png)
![image](https://user-images.githubusercontent.com/72303641/138697314-8a44b386-7b6e-4ed5-8071-f532ab5d5f55.png)

## Training Rainfall Prediction Model with Different Models And Plotting Decision Region for all Models

![image](https://user-images.githubusercontent.com/72303641/138697456-67ced65e-05eb-486c-ab61-628508ccfb65.png)


## Rainfall Prediction Model Comparison And Selection 
![image](https://user-images.githubusercontent.com/72303641/138697497-1a3837aa-9c5a-4b73-ab79-3993495707f1.png)
![image](https://user-images.githubusercontent.com/72303641/138697352-276e6250-2322-48d3-8058-23ae8b72f47f.png)

**If we are considering the speed and accuracy than XGBoost is the best option. **

