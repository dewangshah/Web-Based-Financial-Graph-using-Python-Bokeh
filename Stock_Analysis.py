#!/usr/bin/env python
# coding: utf-8

# In[175]:


from pandas_datareader import data
import datetime
from bokeh.plotting import figure,show, output_file

start=datetime.datetime(2019,10,8)
end=datetime.datetime(2019,12,8)

df=data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end)#AAPL - Stock Symbol for Apple
#Output of DataReader method is a Data frame

#date_increase=df.index[df.Close < df.Open]
#date_decrease=df.index[df.Close > df.Open]
def inc_dec(c,o):
    if c>o:
        value="Increase"
    elif c<o:
        value="Decrease"
    else:
        value="Equal"
    return value

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Close-df.Open)
df

p=figure(x_axis_type='datetime',width=1000, height=300, sizing_mode='scale_width')
p.title.text="Candlestick Chart"
p.grid.grid_line_alpha=0.3

hours_12=12*60*60*1000

p.segment(df.index, df.High, df.index, df.Low, color="Black") #Params=xhigh,yhigh,xlow,ylow,color
#Segments have to be added first if we want them to hide behind the rectangles

p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"], hours_12, df.Height[df.Status=="Increase"],fill_color="#50C878",line_color="black")
#Param1=x_axis Values, Param2=y_axis Values, Param3=Rectangle_width(in ms),Param 4=Rect_height, Param5=Rect_color, Param6=line_color

p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"], hours_12, df.Height[df.Status=="Decrease"],fill_color="#c41e3a",line_color="black")


output_file("CandleStick.html")
show(p)


# In[ ]:




