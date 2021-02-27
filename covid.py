import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
covid=pd.read_csv('covid.csv')

#Getting the cases in India
india_case=covid[covid["location"]=="India"]

india_case.head()
india_case.tail()

#Total Case Per Day
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x="date",y="total_cases",data=india_case)
plt.show()

#Making a dataframe for last 5 days
india_last_5_days=india_case.tail()

#Total cases in last 5 days
sns.set(rc={'figure.figsize':(3,3)})
sns.lineplot(x="date",y="total_cases",data=india_last_5_days)
plt.show()

#Total tests per day
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x="date",y="total_tests",data=india_case)
plt.show()

#Total tests in last 5 days
sns.set(rc={'figure.figsize':(15,10)})
sns.lineplot(x="date",y="total_tests",data=india_last_5_days)
plt.show()


#Understanding cases of India, China and Japan
india_japan_china=covid[(covid["location"] =="India") | (covid["location"] =="China") | (covid["location"]=="Japan")]


#Plotting growth of cases across China, India and Japan
sns.set(rc={'figure.figsize':(15,10)})
sns.barplot(x="location",y="total_cases",data=india_japan_china,hue="date")
plt.show()

#Getting latest data
last_day_cases=covid[covid["date"]=="2020-05-24"]
last_day_cases

#Sorting data w.r.t total_cases
max_cases_country=last_day_cases.sort_values(by="total_cases",ascending=False)
max_cases_country


#Top 5 countries with maximum cases
max_cases_country[1:6]

#Making bar-plot for countries with top cases
sns.barplot(x="location",y="total_cases",data=max_cases_country[1:6],hue="location")
plt.show()

