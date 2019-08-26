#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def player_split(vals):
    return vals.split('\\')[0]
for X in range(1994,2019):
    #iterate the filename with variables
    df=pd.read_csv("rawdata%d.csv"%X)
    #clean the redundant part of players' name 
    df.Player=df.Player.apply(player_split)
    #add new column-year
    df['year']=X
    #select and drop the rows that one player has several teams
    droplist=df[df.duplicated(subset=['Player'],keep='first')]
    df=df.drop(droplist.index, axis=0)
    #select and drop the rows that column position has invalid value except for those 5 positions 
    droplist2=df[df['Pos'].str.contains('-')]
    df=df.drop(droplist2.index, axis=0)
    #extract the columns we need
    df_final = df[['Player','Pos','Tm','G','MP','WS','BPM','VORP','year']]
    #generate the final csv file for each year
    df_final.to_csv("finaldata%d.csv"%X,index=False)
    
dfHW=pd.read_csv('player_data.csv')
#fliter out the players who retired before 1994
dfHW=dfHW.drop(dfHW[dfHW.year_end<1995].index,axis=0).reset_index(drop=True)
dfHW.rename(columns={'name':'Player'},inplace=True)  
#get the list of player using overlapping name
c=dfHW.Player.duplicated(keep=False)
dfHW[c].head()

