# Bank Marketing Campaign Machine Learning Model Prediction


## **1. Project Overview**

### **Business Understanding**
A banking company conducted a marketing campaign to offer various financial products, including deposit products.
To increase product sales, the bank carried out direct marketing campaigns by contacting customers via phone to acquire new deposit customers.

However, these efforts must also be evaluated in terms of cost and benefits. To ensure efficiency and better targeting, a Machine Learning model is needed to predict potential customers who are likely to subscribe to deposit products.

### **Analytical Approach**
Using the available data, a predictive model was developed to identify potential customers who are likely to subscribe to deposit products by building a classification model. The objectives are:
- To create a more efficient and targeted campaign program
- To improve campaign effectiveness by targeting customers with a high probability of subscribing to deposit products
- To optimize the campaign budget
- To minimize operational costs by reducing irrelevant or ineffective calls


## **2. Data**
The dataset used in this project was obtained from the UCI Machine Learning Repository :
- data_bank_marketing_campaign.csv


## **3. Tools Used**
- Microsoft Visual Studio Code, Jupyter Notebook, Google Colab
- Programming Language : Python (Pandas, Numpy, Scikit-learn)
- Visualization        : Seaborn, Matplotlib
- App Builder          : Streamlit [(Bank Deposit Predictor)](https://bankdepositpredictorapp-yanfa121.streamlit.app/)
- Presentation Report  : Canva


## **4. Prerequisites**
This project was developed using the following library versions :
- Python 3.13.5
- NumPy 2.2.0
- Pandas 2.2.3
- Seaborn 0.13.2
- Matplotlib 3.10.0
- Scikit-learn 1.7.0
- Streamlit 1.49.1


## **5. Project Structure**
```
├── README.md                                 <- Guideline and overview of the entire project
├── Models
│   ├── Bank_Marketing_Campaign_ML.ipynb      <- Notebook for building this model
│   ├── bestmodel.mdl                         <- Saved model pipeline
│   ├── data_bank_marketing_campaign.csv      <- Raw data
│   |__ lgbm_grid_tune_9.hyp                  <- Saved best tuning for model
│
├── Reports
│   ├── Link_Video_Explanation.txt            <- Link video explanation
│   |__ Bank_Marketing_Campaign_PPT.pdf       <- Slide explanation
│
|__ Streamlit
│   ├── bank_deposit_predictor.py             <- Model app main file
│   ├── bestmodel.mdl                         <- Saved model pipeline
│   ├── Link_Streamlit.txt                    <- Streamlit app link
│   |__ requirements.txt                      <- Requierements version of library
```


## **6. Link**
App Deployment Repository : [github.com/yanfa121/Bank_Deposit_Predictor](https://github.com/yanfa121/Bank_Deposit_Predictor_Streamlit_App)

App Link : [Bank Deposit Predictor (Streamlit)](https://bankdepositpredictorapp-yanfa121.streamlit.app/)

Explanation Video : [Video Explanation](https://drive.google.com/file/d/1wgLVkhoHFC-g_27j9-Nu9fI5AH149ZkQ/view?usp=drive_link)

GDrive : [Link GDrive](https://drive.google.com/drive/folders/1Xe9N1hDM9JYdt5rcJP7zOZuyccdfJz7P?usp=sharing)


## **7. Conclusion & Recommendation**
### **Conclusion**
The final model used in this project is LGBM (Light Gradient Boosting Machine) with hyperparameter tuning. Based on the final evaluation and comparison with pre tuning models and threshold optimization, the model was optimized to maximize recall for the positive class (class 1).

This means the model prioritizes not missing potential customers, even at the risk of producing false positives (contacting customers who ultimately do not subscribe to deposits). This approach is chosen because the cost of losing potential customers is considered higher than the cost of contacting uninterested customers.

By implementing this model, the bank can improve employee productivity, save time, reduce operational costs, and increase profit. Although the performance improvement is only slightly better than a naive approach of predicting all customers as positive (calling everyone), the model significantly helps in optimizing time, effort, and operational efficiency.

### **Recommendation**
1. Business Recommendations
- Focus outreach efforts on customers with high predicted probabilities
- Apply customer treatment segmentation, for example:
    - High probability: direct phone calls
    - Medium probability: contact via email or WhatsApp (lower cost)
    - Low probability: consider not contacting
- Conduct regular cost evaluations to ensure the model continues to deliver optimal value, adjusting the decision threshold according to changing cost structures

2. Model Performance Improvement
- Enhance model performance by adding more features, such as income and existing deposit amounts
- Provide a more detailed explanation of unknown values to make them more interpretable and actionable
- Continuously update the model with the latest campaign data, as data distribution changes can affect model performance. Regular monitoring helps the model adapt to evolving data patterns


### Expected Impact
With the implementation of this model, the bank is expected to optimize marketing campaigns more effectively, efficiently, and strategically:
- Improve campaign targeting by focusing on high-probability customers, reducing ineffective contacts
- Minimize time and effort spent by marketing and telemarketing teams by prioritizing high-potential customers
- Reduce operational costs (e.g., call costs and resource allocation), enabling more efficient budget utilization
- Increase short-term and long-term profitability, not only by reducing false positives (contacting uninterested customers) but also by minimizing false negatives (losing potential customers)


## **8. Contact**
- Yanfa Anandika
- Email : yanfaanandika21@gmail.com
- LinkedIn : [Yanfa Anandika](https://www.linkedin.com/in/yanfa-anandika-a663bb170/)
- GitHub : [yanfa121](https://github.com/yanfa121)
