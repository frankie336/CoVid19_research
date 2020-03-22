# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:21:34 2020

@author: Prime_Thanos, 'Francis Neequaye'

@author: Prime_Thanos, '+44 (0)7427 348 836'
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:21:34 2020

@author: francis.neequaye@gmail.com
@author  https://github.com/frankie336/CoVid19_research
@author: https://github.com/frankie336

"""

"""

Live data of the  ongoing CoVid-19 ,‘Corona virus’ transmission and clinical outcomes is collected by numerous national and international health organizations. 
The Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE) collects and aggregates the data, presenting it in their Git hub repository. 
This data has been the main source of authority throughout the crisis . Below, are a list of the data sources. 

    • World Health Organization (WHO): https://www.who.int
      http://3g.dxy.cn/newh5/view/pneumonia.
    • BNO News: https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/
    • National Health Commission of the People’s Republic of China (NHC):
      http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml
    • China CDC (CCDC): http://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm
    • Hong Kong Department of Health: https://www.chp.gov.hk/en/features/102465.html
    • Macau Government: https://www.ssm.gov.mo/portal/
    • Taiwan CDC: https://sites.google.com/cdc.gov.tw/2019ncov/taiwan?authuser=0
    • US CDC: https://www.cdc.gov/coronavirus/2019-ncov/index.html
    • Government of Canada: https://www.canada.ca/en/public-health/services/diseases/coronavirus.html
    • Australia Government Department of Health: https://www.health.gov.au/news/coronavirus-update-at-a-glance
    • European Centre for Disease Prevention and Control (ECDC): https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases
    • Ministry of Health Singapore (MOH): https://www.moh.gov.sg/covid-19
    • Italy Ministry of Health: http://www.salute.gov.it/nuovocoronavirus




CSSE Keep their data at their GitHub repository the main page:
    • https://github.com/CSSEGISandData/COVID-19 
The raw data feeds:
    • https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv
    • https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv
    • https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv



"""
import time
start = time.time()# Times the ececution time of this function
from datetime import datetime
from datetime import date

"""
Data Science
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
import numpy as np
import re
import csv
import json
import requests
import urllib3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

class celcius(object):
 def __init__(self, country):
   
   self.now = now 
   self.CSSE_confirmed = CSSE_confirmed 
   self.CSSE_death = CSSE_death
   self.CSSE_recovered = CSSE_recovered
   self.country = country
   self.file_date = file_date
   self.file_date = datetime.now().strftime("%Y%m%d-%H%M%S")

 def corona_live(self):
      
     """ 
     1. Download the CSSE   feed for confirmed, death and recovered Pandemic cases
     2. For future reference, save a local copy of the data before we run any models or manipulate the
     3.  Sometimes the columns are set to an inappropriate data or not useful for immediate purposes so:
        • Preemptively change the informational columns to string data types and the metrics to integers 
        • Drop the fields for longitude / latitude 
     """


     df_confirmed = pd.read_csv(CSSE_confirmed) 
     df_death = pd.read_csv(CSSE_death) 
     df_recovered = pd.read_csv(CSSE_recovered)
     """
     -Firstly, save  un adulterated copies of each .csv locally for later reference or lack of internet
     -These are stored in the scaraped_data directory change this line of code to preference or need 
     """
     
     df_confirmed.to_csv("scraped_data\\_"+file_date+"_CSSE_covid_new_time_series.csv", encoding='utf-8')#data for new cases
     df_confirmed.to_csv("scraped_data\\"+file_date+"_CSSE_covid_death_time_series.csv", encoding='utf-8')#data for death rate
     df_confirmed.to_csv("scraped_data\\"+file_date+"_CSSE_covid_recovered_time_series.csv", encoding='utf-8')#data for recovered cases

     
     remove =['Lat','Long']##Looping over these lists provides some code efficiency 
     frame = [df_confirmed,df_death,df_recovered,df_recovered]
     fielsds = ['Lat','Long','']
     for f,r,s in zip(frame, remove,fielsds):
        f['Province/State']= df_confirmed['Province/State'].astype(str)#Converts these fields to string type entities
        f['Country/Region']= df_confirmed['Country/Region'].astype(str)
        del df_confirmed[s]#Removes some fields we do not need right now 
    
     """
     The raw data revived is semi structured for the purposes of Python / Pandas .
      Thus we need to manipulate and eventually ‘Pivot’ it so we have the following structure:
     [datetime] [Province/State] [Country/Region] [CoVid19_new] [Covid19_death] [Covid19_recovery]
     """
     
     places =[df_confirmed,df_death,df_recovered]#A list of the individual frames we will be iterating 
     cats = [df_confirmed,df_death,df_recovered]
     """
     We need to do the same manipulation on 3 sets of .csv files and integrate them at the
     end of the process . These lists will be called upon to that end.
     """
     cats0 = [df_confirmed]
     cats1 = [df_death]
     cats2 = [df_recovered]
     
     names =['CoVid19_confirmed','Covid19_Mortality','Covid19_Confirmed_Recovered']#Used for auto file naming an graph anotation , once we hae the data 




   
     """
      With this , we can begin to gain further insight inclusive of a few like: relative burden, worst case outcomes and other possible correlations.  
      Cases are Keyed against Geo locations. In some instances. This is at a more localized level of Government; depending on the organizational 
      structure of each Sovereign Nation: 
      [‘Province/State’]  [‘Country/Region’]
      For example. New York is Keyed in the [‘Province/State’] and so goes the other administrative areas of The USA. All of Kuwait is keyed against the  [‘Country/Region’] . 
      So that we do not have to run the script twice, guess, or look which column is relevant for our target country, the following technique is employed:
      1.  Initiate a ‘surveillance’ instance of filtering  the most error prone column [‘Province/State’] against our target country .
      2. Transom the result of the output to a  normal list, ‘go_list’.
      3. If the location is not keyed in the [‘Province/State’]  column, the list will be empty and the length ‘0’  
      4. If the length  of the go_list is not ‘0’, then it must be keyed against the [‘Country/Region’] column . 
     """
      
     for p,x,y,z in zip(places, cats,cats1,cats2): 
      
     
      geo_type ="Province/State"
      geo_loc = "United Kingdom" #Type your target location here 

      dfx0 = x[x[geo_type]==(geo_loc)]#dfx0 binds to x/New Cases
      go_list = dfx0["Province/State"].tolist() 
      
      
      print (go_list) 
      a = (len(go_list))
      print (go_list) 
    

      
      if a in ['0']:
        geo_type ="Country/Region"
      else:
        geo_type ="Province/State"


     """
     Here we begin the manipulate the three separate .csv files ; which then became pandas frames.
     We are iterating several lists so keeep track. I will explain as we go down the  code.

     """
       
     for p,x,y,z in zip(places, cats,cats1,cats2): 
     
       places = x["Country/Region"].unique()
       print(places)
       for p, in zip(places):

      
        
       
          dfx0 = x[x[geo_type]==(geo_loc)]#dfx0 binds to x/New Cases
          dfx1 = y[y[geo_type]==(geo_loc)]#dfx1 binds to y/deaths
          dfx2 = z[z[geo_type]==(geo_loc)]#dfx2 binds to z/recoveries
      
          """

          CSSE provide a summarized time series or fall relevant events , updated once daily. It has the following structure:
          ….['Country/Region']  ['Lat']  ['Long'] ['1/22/20'] ['1/23/20']…
          
          This is a little tricky to work with filtering graphing , etc, etc . Here we will do the following:
              • Transform the dates of events which are held in column headers to a  list 
              • Extract cell values to a list – these are the daily numbers in each category 
              • Transform  the dates and values list to a separate  new pandas frames 
              • Make a mew pandas data frame that merges all three sheets 
              • Save the new sheet for prosperity 
          """
          
          date_time0 = dfx0.columns#column headers to array
          date_time1 = dfx1.columns
          date_time2 = dfx2.columns
          print(date_time0,date_time1,date_time2)
          
          
          valuesx0 = dfx0.values#values to array
          valuesx1 = dfx1.values
          valuesx2 = dfx2.values
          print(valuesx0,valuesx1,valuesx2)
          
          
          
          
          date_time0 =  (date_time0.tolist())#NP arrays are a little trickly to handle , so transform back to normal list
          date_time1 =  (date_time1.tolist())
          date_time2 =  (date_time2.tolist())
          print(date_time0,date_time1,date_time2)
          dfn0 = pd.DataFrame({'datetime':date_time0})#We only need one datetime column in the finished product
          #dfn1 = pd.DataFrame({'datetime':date_time1})
          #dfn2 = pd.DataFrame({'datetime':date_time2})
          dfn0 = dfn0.iloc[4:]
          #dfn1 = dfn1.iloc[4:]
          #dfn2 = dfn2.iloc[4:]
          [item for sublist in date_time0 for item in sublist]#merges the NP array incase it some how became multi dimensional


          valuesx0 =  (valuesx0.tolist())
          valuesx1 =  (valuesx1.tolist())
          valuesx2 =  (valuesx2.tolist())
          valuesx0 = [item for sublist in valuesx0 for item in sublist]#merges the NP array incase it some how became multi dimensional
          valuesx1 = [item for sublist in valuesx1 for item in sublist]
          valuesx2 = [item for sublist in valuesx2 for item in sublist]
          dfq0 = pd.DataFrame({'CoVid19_new':valuesx0})
          dfq1 = pd.DataFrame({'Covid19_death':valuesx1})
          dfq2 = pd.DataFrame({'Covid19_recovery':valuesx2})
          #dfq0['CoVid19_new'].fillna(0, inplace=True)
          #dfq0['CoVid19_new'] = dfq0['CoVid19_new'].astype(int)
          #final[["CoVid19_new", "Covid19_death"]] = final[["CoVid19_ne

          dfq0 = dfq0.iloc[4:]
          dfq1 = dfq1.iloc[4:]
          dfq2 = dfq2.iloc[4:]


          print(valuesx0,valuesx1,valuesx2)
          print(dfq0,dfq1,dfq2)
          

         
          final = pd.concat([dfn0,dfq0,dfq1,dfq2], axis=1)#Concantenates each 
          final['datetime'] = pd.to_datetime(final['datetime'])
          #final.set_index(["datetime"], inplace = True,)
          final.fillna(0)
         
         
      
          final.reset_index()
         

          print(final[final.index.duplicated()])
          print(final.columns)
          
          print(final['CoVid19_new'].max())
          print(final['Covid19_death'].max())
          print(final['Covid19_recovery'].max())



       """
       In this section, we import a list of all recognized nations in the world in a pandas frame, taken from:
       • https://www.worldometers.info/geography/alphabetical-list-of-countries/countries-that-start-with-a/ 
       This frame has the following structure :
       [‘Country’] [‘Population’] [‘Population_2020’] [‘Area_Km’] [‘Density_Pkm’]

       With this , we can begin to gain further insight inclusive of a few like: relative burden, 
       worst case outcomes and other possible correlations. 
       
       """

       df_genpop = pd.read_csv('scraped_data\\countrypop.csv',encoding='utf-8')
       print(df_genpop)



       g = sns.PairGrid(final)
       g.map_diag(plt.hist)
       g.map_offdiag(plt.scatter);
    
       plt.savefig(geo_loc+"_daily_corona_chart.png")
       
       
       
       
       
   
      
      
      

if __name__ == '__main__':
    
    file_date = datetime.now().strftime("%Y%m%d-%H%M%S")
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    country = "country"
    CSSE_confirmed ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
    CSSE_death = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
    CSSE_recovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
    j = celcius(country)
    j.corona_live()
    
    

end = time.time() 
print(end - start)