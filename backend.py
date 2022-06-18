# import pymongo
import time
import datetime

from pymongo import MongoClient
timetable={"Monday":{"ptrp":[570,630],"dldm":[630,690],"os":[690,750],"seminar":[780,840],"bhr":[840,900],"coa":[900,960]},
           "Tuesday":{"coa":[570,630],"bhr":[630,690],"os":[690,750],"dldm":[780,840],"seminar":[840,900],"ptrp":[900,960]},
           "Wednesday":{"coa":[570,630],"bhr":[630,690],"os":[690,750],"dldm":[780,840],"seminar":[840,900],"ptrp":[900,960]},
           "Thursday":{"coa":[570,630],"bhr":[630,690],"os":[690,750],"dldm":[780,840],"seminar":[840,900],"ptrp":[1140,1460]},
           "Friday":{"bhr":[400,630],"ptrp":[630,690],"os":[690,750],"dldm":[780,840],"seminar":[840,900],"coa":[900,960]},
           "Saturday":{},
           "Sunday":{}}


lec = {"dldm":0,"seminar":1,"ptrp":2,"bhr":3,"coa":4,"os":5}
flags = {"Aniket":0,"Sangamesh":0};
reset_time = [300,630,690,750,780,840,900,960]
def get_database(name,datestring,date):

    t = time.localtime(time.time())
    h = t.tm_hour
    m =  t.tm_min
    curr_time = (h*60)+m
    # print(type(curr_time))

    x = datetime.datetime.now()
    today = x.strftime("%A")


    client = MongoClient('mongodb+srv://Aniketwagh123:Aniket9277@cluster0.ofr9k.mongodb.net/?retryWrites=true&w=majority')
    db = client.get_database('test-database')
    collection = db.collections
    doc= collection.find_one({"name":name.title()})
    pre = doc["sub"]
    print(pre)
    lec = get_lecture(curr_time, today)
    if lec==None:
        return
    temp = pre[lec]
    templ = temp.split(",")
    temp1 =str((int(templ[0])+1))+","+str((int(templ[1])+1))
    pre[lec]=temp1
    print(pre)
    if flags[name.title()]==0 :
        collection.update_one({"name":name.title()},{"$set": {"sub":pre}})
        flags[name.title()]=1
        return
    else:
        if curr_time in reset_time:
            flags[name.title()]=0
            return
# get_database("Name","Aniket")

def get_lecture(curr_time,today):
    for i in timetable[today]:
        # print(type(timetable[today][i][0]))
        # print(timetable[today][i][0])
        if curr_time>=timetable[today][i][0] and curr_time<timetable[today][i][1]:
            return lec[i]

t = time.localtime(time.time())
print(t)
