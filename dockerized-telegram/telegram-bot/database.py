from pymongo import MongoClient
import datetime

class MongoDB():

    def __init__(self):
        self.client = MongoClient("db",27017)
        self.db = self.client["telegram"]
        self.collection = self.db["telegramcollection"]

    def Insert(self,url,user):
        urll={
            "url":url,
            "user":user,
            "date":datetime.datetime.now()

        }
        try:
            if(self.UrlCheck(str(url))==False):
                self.collection.insert(urll)
                return True
            else:
                return False
        except:
            print("Excepet")
            return False

    def UrlList(self):
        myresults = list(self.collection.find())
        return myresults

    def UrlCheck(self,url):

        if(self.collection.find_one({"url":url})):
            print("Var")
            return True
        else:
            print(url+"Yok")
            return False
