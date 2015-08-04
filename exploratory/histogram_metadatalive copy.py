import matplotlib.pyplot as plt
import numpy as np
import pymongo
from function import count_occurences_field

client = pymongo.MongoClient("localhost", 27017) 
db = client.phoenix

##collections
genre = db.genre
event = db.event
total_number_of_events = event.count()

##make the histogram
field_list = [ "topic.metadata.release_date", "topic.source_id", "topic.type"]

##work in progress now
for fieldname in field_list:
    data = count_occurences_field(event,fieldname)
    x = data.keys()
    y = data.values()


    pos = np.arange(len(x))+0.5

    plt.figure(figsize=(6,8))
    plt.barh(x, y)
    plt.axvline(total_number_of_events,linestyle="dashed",color="black")
    plt.xlabel("Counts")
    plt.ylabel(fieldname)
    plt.yticks(pos,x)
    plt.savefig("figures/histogram_"+fieldname+".pdf")

