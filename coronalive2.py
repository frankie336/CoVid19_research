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

    • "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
      
    •    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"#new deaths data from csse
    • "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"#new recoveries data from csse
    • "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
    • https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
    •  "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"#new recoveries data from csse
"""

"""
General 
"""
from datetime import datetime
from datetime import date
import os
import time
start = time.time()# Times the ececution time of this function
import glob


"""♠
"""
from wwo_hist import retrieve_hist_data
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
from matplotlib.ticker import FuncFormatter
import matplotlib.gridspec as gridspec
import seaborn


import matplotlib.pyplot as plt
import matplotlib.ticker as ticker





log = []#General logging and error catching











class celcius(object):
 def __init__(self, country):
   
   self.now = now 
   

   self.World_CSSE_confirmed = World_CSSE_confirmed 
   self.world_CSSE_death = world_CSSE_death
   self.world_CSSE_recovered = world_CSSE_recovered



   self.World_CSSE_confirmed = usa_CSSE_confirmed 
   self.world_CSSE_death = usa_CSSE_death
   self.world_CSSE_recovered = world_CSSE_recovered
   

   self.country = country
   self.file_date = file_date
   self.file_date = datetime.now().strftime("%Y%m%d-%H%M%S")

   self.temp_hist0 = temp_hist0
   self.temp_hist1 = temp_hist1
   


  

 def CoronaLive2(self):


     """
     VARIABLES

     1. Uncomment and comment out the comnpeting alternative 
     for example #geography = 'USA' for USA data
 
     """
     #geography = 'USA'
     geography = 'World'
   
     
    
     if geography == 'USA':
      print('Selecting The US Coronavirus Numbers, stand by please.')
      confirmed = usa_CSSE_confirmed
      deaths = usa_CSSE_death
      recovered = usa_CSSE_recovered
      sub = 'Province_State'
      country = 'Country_Region'
      local = 'Admin2'
      UID = 'UID'
      iso2 = 'iso2'
      iso3 = 'iso3'
      code3 = 'code3'
      fips = 'FIPS'
      latitude = 'Lat'
      longitude = 'Long_'
      key = 'Combined_Key'
      population = 'Population'
      #geo_type = country
      geo_type = sub
      specific = 'Alabama'# When filtering for a specific Country or sub division chanage the entry here where you see 'United Kingdom

     else:
      if geography == 'World':
        print('Selecting the World Coronavirus Numbers, stand by please.')
        confirmed = World_CSSE_confirmed
        deaths = world_CSSE_death
        recovered = world_CSSE_recovered
        sub = 'Province/State'
        country = 'Country/Region'
        latitude = 'Lat'
        longitude = 'Long'
        geo_type = country
        specific = 'United Kingdom'# When filtering for a specific Country or sub division chanage the entry here where you see 'United Kingdom
      else:
        print("***********TBC**********")


      


      
     """ 
     1. Download the CSSE   feed for confirmed, death and recovered Pandemic cases
     2. For future reference, save a local copy of the data before we run any models or manipulate the
     3.  Sometimes the columns are set to an inappropriate data or not useful for immediate purposes so:
        • Preemptively change the informational columns to string data types and the metrics to integers 
        • Drop the fields for longitude / latitude 
     """

     
     df_confirmed = pd.read_csv(confirmed, error_bad_lines=False)  
     df_death = pd.read_csv(deaths, error_bad_lines=False) 
     df_recovered = pd.read_csv(recovered, error_bad_lines=False)
   

     df_confirmed.to_csv("scraped_data\\csse\\_"+file_date+"_CSSE_covid_new_time_series.csv", encoding='utf-8')#data for new cases
     df_death.to_csv("scraped_data\\csse\\"+file_date+"_CSSE_covid_death_time_series.csv", encoding='utf-8')#data for death rate
     df_confirmed.to_csv("scraped_data\\csse\\"+file_date+"_CSSE_covid_recovered_time_series.csv", encoding='utf-8')#data for recovered cases


  

     """
     The raw data revived is semi structured for the purposes of Python / Pandas .
      Thus we need to manipulate and eventually ‘Pivot’ it so we have the following structure:
     [datetime] [Province/State] [Country/Region] [CoVid19_new] [Covid19_death] [Covid19_recovery]
     """
     

     


     df_confirmed[geo_type]= df_confirmed[geo_type].astype(str)#Converts these fields to string type entities
     df_death[geo_type]= df_death[geo_type].astype(str)#Converts these fields to string type entities
     #df_recovered[geo_type]= df_recovered[geo_type].astype(str)#Converts these fields to string type entities
     
     geo_loc =  df_confirmed[geo_type].unique()

    
     
     remove = ['nan']   
     [geo_loc[i] for i in range(0, len(geo_loc)) if i not in remove]
     geo_loc  = [x for x in geo_loc if x != '']
     

     geo_loc=[x for x in geo_loc if specific in x]#Uncomment this line to filter for only a specific countru or sub division



     """
     Here we begin the manipulate the three separate .csv files ; which then became pandas frames.
     We are iterating several lists so keeep track. I will explain as we go down the  code.
     """



     for index, item in enumerate(geo_loc):#This loops items in our filtered country/region column
  
        
    
              if geography == 'USA':
                  dfx0 = df_confirmed[df_confirmed[geo_type]==(str(geo_loc[index]))]#dfx0 binds to x/New Cases
                  dfx1 = df_death[df_death[geo_type]==(str(geo_loc[index]))]
              else:
                if geography == 'World':
                  dfx0 = df_confirmed[df_confirmed[geo_type]==(str(geo_loc[index]))]#dfx0 binds to x/New Cases
                  dfx1 = df_death[df_death[geo_type]==(str(geo_loc[index]))]#dfx0 binds to x/New Cases
                  dfx2 = df_recovered[df_recovered[geo_type]==(str(geo_loc[index]))]#dfx0 binds to x/New Cases
            
        
              if geography == 'USA':
                 del dfx0[iso2]
                 del dfx0[iso3]
                 del dfx0[local]
                 del dfx0[sub]
                 del dfx0[country]
                 del dfx0[longitude]
                 del dfx0[latitude]
                 del dfx0[key]
                 del dfx0[UID]
                 del dfx0[code3]
                 del dfx0[fips]
                 #del dfx0['Population']
                 
                 del dfx1[iso2]
                 del dfx1[iso3]
                 del dfx1[local]
                 del dfx1[country]
                 del dfx1[longitude]
                 del dfx1[latitude]
                 del dfx1[key]
                 del dfx1[UID]
                 del dfx1[fips]
                 del dfx1[population]
                 
   
                 #del dfx2[iso2]
                 #del dfx2[iso3]
                 #del dfx2[local]
                 #del dfx2[sub]
                 #del dfx2[country]
                 #del dfx2[longitude]
                 #del dfx2[latitude]
                 #del dfx2[key]
                 #del dfx2[UID]
                 #del dfx2[code3]
                 #del dfx2[fips]
                 #del dfx2[population]
              else:
                if geography == 'World':
                   del dfx0[sub]
                   del dfx0[country]
                   del dfx0[longitude]
                   del dfx0[latitude]

                   del dfx1[sub]
                   del dfx1[country]
                   del dfx1[longitude]
                   del dfx1[latitude]

                   del dfx2[sub]
                   del dfx2[country]
                   del dfx2[longitude]
                   del dfx2[latitude]
                
              if geography == 'USA':
                   date_time0 = dfx0.columns#column headers to array
                   date_time1 = dfx1.columns
                   #date_time2 = dfx2.columns
    
    
                   valuesx0 = dfx0.values#values to array
                   valuesx1 = dfx1.values
                   #valuesx2 = dfx2.values
    
    
                   date_time0 =  (date_time0.tolist())#NP arrays are a little trickly to handle , so transform back to normal list
                   date_time1 =  (date_time1.tolist())
                   #date_time2 =  (date_time2.tolist())
    
                   dfn0 = pd.DataFrame({'datetime':date_time0})#We only need one datetime column in the finished product
                   #dfn1 = pd.DataFrame({'datetime':date_time1})
                   #dfn1 = pd.DataFrame({'datetime':date_time1})
                   #dfn2 = pd.DataFrame({'datetime':date_time2})
    
    
    
                   dfn0 = dfn0.iloc[1:]
                   #dfn1 = dfn1.iloc[4:]
                   #dfn2 = dfn2.iloc[4:]
                   [item for sublist in date_time0 for item in sublist]#merges the NP array incase it some how became multi dimensional
                   C = (geo_loc[index])
                   new = C+"_Covid19_new"
                   death = C+"_Covid19_deaths"
                   recover = C+"_Covid19_recovered"
    
    
                   valuesx1 =  (valuesx1.tolist())
                   #valuesx2 =  (valuesx2.tolist())
                   valuesx0 = [item for sublist in valuesx0 for item in sublist]#merges the NP array incase it some how became multi dimensional
                   valuesx1 = [item for sublist in valuesx1 for item in sublist]
                   #valuesx2 = [item for sublist in valuesx2 for item in sublist]
                   dfq0 = pd.DataFrame({new :valuesx0})
                   dfq1 = pd.DataFrame({death:valuesx1})
                   dfn0['datetime'] = pd.to_datetime(dfn0['datetime'])


                   """
                   we need to clean up the resultant data frame a little:
                    • Convert the relevant columns to string type entities
                    • Strip / extract only numeric values from them 
                    • Push down the starting position of each by one , to avoid the geo-location as a value
                   """ 

                   dfq0[new]= dfq0[new].astype(str)
                   dfq1[death]= dfq1[death].astype(str)
                   #dfq2[recover]= dfq2[recover].astype(str)
                   
         
                   dfq0[new] = dfq0[new].fillna('0')
                   dfq1[death] = dfq1[death].fillna('0')
                   #dfq2[recover] = dfq2[recover].fillna('0')
          
                   
                   
                   dfq0[new] = dfq0[new].str.extract('(\d+)', expand=False)
                   dfq1[death] = dfq1[death].str.extract('(\d+)', expand=False)
                   #dfq2[recover] = dfq2[recover].str.extract('(\d+)', expand=False)
                   dfq0[new] = dfq0[new].fillna('0')
                   dfq1[death] = dfq1[death].fillna('0')
                   #dfq2[recover] = dfq2[recover].fillna('0')
                   
                   dfq0[new]= dfq0[new].astype(int)
                   dfq1[death]= dfq1[death].astype(int)
                   #dfq2[recover]= dfq2[recover].astype(int)
                   
                   
          
                   
                   
                   final = pd.concat([dfn0,dfq0,dfq1], axis=1)#Concantenates each 
                   final['datetime'] = pd.to_datetime(final['datetime'])
                   
                   print(final)
                   print(final.dtypes)


                   w = (final[new].max())
                   e = (final[death].max())
                   #r = (final[recover].max())


                   diff0="Last_24_Hours_New_Cases_difference"
                   final[diff0] = final[new].diff()
                   print(final[diff0])

                   deq0 = deq0 = final[-1:]
                   #dfq0[diff0]= dfq0[diff0].astype(str)
                   deq0[diff0] = deq0[diff0].fillna('0')
                   #dfq0[diff0]= dfq0[diff0].astype(int)
                   s = (deq0[diff0].max()) 
                   
                   final.set_index(["datetime"], inplace = True)
                   
                   
                   final = final.rename(columns={new: new+'_:'+str(w), death: death+'_:'+str(e), diff0: diff0+'_:'+str(s)})
                   print(dfx0)
              else:


                 
                      if geography == 'World':
                         date_time0 = dfx0.columns#column headers to array
                         date_time1 = dfx1.columns
                         date_time2 = dfx2.columns
    
                         valuesx0 = dfx0.values#values to array
                         valuesx1 = dfx1.values
                         valuesx2 = dfx2.values
    
                         date_time0 =  (date_time0.tolist())#NP arrays are a little trickly to handle , so transform back to normal list
                         date_time1 =  (date_time1.tolist())
                         date_time2 =  (date_time2.tolist())
    
    
                         dfn0 = pd.DataFrame({'datetime':date_time0})#We only need one datetime column in the finished product
                         #dfn1 = pd.DataFrame({'datetime':date_time1})
                         #dfn1 = pd.DataFrame({'datetime':date_time1})
                         #dfn2 = pd.DataFrame({'datetime':date_time2})
    
    
                         dfn0 = dfn0.iloc[1:]
                         #dfn1 = dfn1.iloc[4:]
                         #dfn2 = dfn2.iloc[4:]
                         [item for sublist in date_time0 for item in sublist]#merges the NP array incase it some how became multi dimensional
                         C = (geo_loc[index])
                         new = C+"_Covid19_new"
                         death = C+"_Covid19_deaths"
                         recover = C+"_Covid19_recovered"
    
    

                         valuesx1 =  (valuesx1.tolist())
                         valuesx2 =  (valuesx2.tolist())
                         valuesx0 = [item for sublist in valuesx0 for item in sublist]#merges the NP array incase it some how became multi dimensional
                         valuesx1 = [item for sublist in valuesx1 for item in sublist]
                         valuesx2 = [item for sublist in valuesx2 for item in sublist]
                         dfq0 = pd.DataFrame({new :valuesx0})
                         dfq1 = pd.DataFrame({death:valuesx1})
                         dfq2 = pd.DataFrame({recover:valuesx2})
                         dfn0['datetime'] = pd.to_datetime(dfn0['datetime'])



                         """
                         we need to clean up the resultant data frame a little:
                          • Convert the relevant columns to string type entities
                          • Strip / extract only numeric values from them 
                          • Push down the starting position of each by one , to avoid the geo-location as a value
                         """ 


                 
                         dfq0[new]= dfq0[new].astype(str)
                         dfq1[death]= dfq1[death].astype(str)
                         dfq2[recover]= dfq2[recover].astype(str)
                         
         
                         dfq0[new] = dfq0[new].fillna('0')
                         dfq1[death] = dfq1[death].fillna('0')
                         dfq2[recover] = dfq2[recover].fillna('0')
          
                         
                         
                         dfq0[new] = dfq0[new].str.extract('(\d+)', expand=False)
                         dfq1[death] = dfq1[death].str.extract('(\d+)', expand=False)
                         dfq2[recover] = dfq2[recover].str.extract('(\d+)', expand=False)
                         dfq0[new] = dfq0[new].fillna('0')
                         dfq1[death] = dfq1[death].fillna('0')
                         dfq2[recover] = dfq2[recover].fillna('0')
                         
                         dfq0[new]= dfq0[new].astype(int)
                         dfq1[death]= dfq1[death].astype(int)
                         dfq2[recover]= dfq2[recover].astype(int)


                         final = pd.concat([dfn0,dfq0,dfq1,dfq2], axis=1)#Concantenates each 
                         final['datetime'] = pd.to_datetime(final['datetime'])
                         
                         print(final)
                         print(final.dtypes)
    
    
                         w = (final[new].max())
                         e = (final[death].max())
                         r = (final[recover].max())

                         diff0="Last_24_Hours_New_Cases_difference"
                         final[diff0] = final[new].diff()
                         print(final[diff0])
    
                         deq0 = deq0 = final[-1:]
                         #dfq0[diff0]= dfq0[diff0].astype(str)
                         deq0[diff0] = deq0[diff0].fillna('0')
                         #dfq0[diff0]= dfq0[diff0].astype(int)
                         s = (deq0[diff0].max()) 


                         final.set_index(["datetime"], inplace = True)
                         final = final.rename(columns={new: new+'_:'+str(w), death: death+'_:'+str(e),recover: recover+'_:'+str(r), diff0: diff0+'_:'+str(s)})

              if geography == 'USA':
                            stylex = "ggplot"  
                            plt.style.use(stylex)
                        
                            plt.figure(figsize=(15,8))
                            #plt.text(0.95, 0.05, '@author: Prime_Thanos, Francis Neequaye, prime.thanos336@gmail.com',fontsize=50, color='gray',ha='right', va='top', alpha=0.5)
                            
                            sns.lineplot(data=final)
            
                            directory_A="charts\\weather_catcher\\usa\\"+(geo_loc[index])
                            if not os.path.exists(directory_A):
                               os.makedirs(directory_A)
                            plt.savefig(directory_A+"\\_"+(str(geo_loc[index]))+"_daily_corona_chart2.png") 

                            print("DONE!, Find your Charts in"+directory_A+"\\_"+(str(geo_loc[index]))+"_daily_corona_chart2.png")
              else:
                  if geography == 'World':
                            stylex = "ggplot"  
                            plt.style.use(stylex)
                        
                            plt.figure(figsize=(15,8))
                            #plt.text(0.95, 0.05, '@author: Prime_Thanos, Francis Neequaye, prime.thanos336@gmail.com',fontsize=50, color='gray',ha='right', va='top', alpha=0.5)
                            
                            sns.lineplot(data=final)
            
                            directory_A="charts\\weather_catcher\\basic\\"+(geo_loc[index])
                            if not os.path.exists(directory_A):
                               os.makedirs(directory_A)
                            plt.savefig(directory_A+"\\_"+(str(geo_loc[index]))+"_daily_corona_chart2.png") 

                            print("DONE!, Find your Charts in"+directory_A+"\\_"+(str(geo_loc[index]))+"_daily_corona_chart2.png")
                
                             
                         
          
                 
         
                         
              
                         
              
                           
                         
            

   
    
if __name__ == '__main__':

    temp_hist0 = (glob.glob("temperatures\\nations\\*.csv"))
    temp_hist1 = (glob.glob("temperatures\\regions\\*.csv"))
    temp_hist2 = (glob.glob("temperatures\\usa\\*.csv"))    
    file_date = datetime.now().strftime("%Y%m%d-%H%M%S")
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    country = "country"

    """
    Johns Hopkins Raw Data

    """
    World_CSSE_confirmed ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"#new cases data from csse
    world_CSSE_death = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"#new deaths data from csse
    world_CSSE_recovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"#new recoveries data from csse
    
    usa_CSSE_confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
    usa_CSSE_death = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"
    usa_CSSE_recovered = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv"#new recoveries data from csse



    

    
    b = celcius(country) 
    b.CoronaLive2()

    
    

end = time.time() 
print(end - start)