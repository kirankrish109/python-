import pandas as pd #importing pandas library

user = pd.read_csv("user_id.csv") #Reading user_id dataset to user variable.
w_event=pd.read_csv("win_events.csv") #Reading windows event data set to w_event variable.
ws = pd.read_json('workstation_in_final.json') #Reading worksation data set to ws variable.

#merging user_id dataset and windows_event data set as mergeOne with common column "user_id".
mergeOne = pd.merge(user,w_event ,on = "user_id")

# Merging the workstation dataset along with the already merged data sets with common column "workstaion_id".
output = pd.merge(mergeOne,ws,on="workstation_id")

#merged output file is order as per the requrement and saved to the ord_out variable
ord_out = output[["Event_id","user_id","workstation_id","year","month","timetamp(epoch)","user_name","department","permission","os","vendor"]]
ord_out.to_csv('output.csv',index=False)


