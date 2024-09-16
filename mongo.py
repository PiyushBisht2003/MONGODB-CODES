from pymongo  import MongoClient
client =MongoClient ("mongodb://localhost:27017")
#TO SEE  ALL THE DATABASES WE MADE 
#chin=client.list_database_names()
#print(chin)    

db = client["mydatabase"]
collection = db["users info"]

#TO SEE WHAT IS IN OUR DATABASE
Database = client.list_database_names()
print(Database)
 
#INSERT DATA ONE  
dictionary = {"Name":"piyush" ,"age":20,"city":"delhi"}
collection.insert_one(dictionary)

dictionary2 = {"Name":"negi" ,"age":24,"city":"uk"}
collection.insert_one(dictionary2)
 
#MULTIPLE DATA SET AT ONCE 
dataset = [
   {"Name" : "piyush" ,"age":20 ,"class" : "silver" },
   {"Name" : "negi" ,"age": 25 ,"class" : "gold" },
   {"Name" : "parcha" ,"age": 23 ,"class" : "bronze" },
   {"Name" : "mishra" ,"age": 22 ,"class" : "diammond" },
   {"Name" : "pal" ,"age": 21 ,"class" : "no rank" }
         ]
           
collection.insert_many(dataset)


# YOU CAN MAKE YOUR OWN ID IN YOUR GIVEN DATA 

dictionary34 = { "_id":1,"Name":"negi" ,"age":24,"city":"uk"}
collection.insert_one(dictionary34)

#FIND THE DATA IN YOUR DATABASE 

ohh  = collection.find({"Name":"piyush"})
print(ohh)

#FIND MULTIPLE DATA FROM DATBASE 
gg = collection.find({"Name":"piyush"})
for oh in gg:
  print(oh)

 #TO GET SPECIFIC  DATA FROM DATABASE 
gg = collection.find({"Name":"piyush"},{"Name":1,"age":1,  "_id":0})
for oh in gg:
 print(oh)

my =  client["mydatabase"]
print(my.list_collection_names())    
 
# UPDATE DATA IN YOUR DATABSE 

prev= {"Name":"parcha"}
upd={"$set":{"class":"gold"}}
collection.update_one(prev,upd) 

#UPDATE  MULTIPLE DATA IN YOUR DATABASE 
prev= {"Name":"parcha"}
upd={"$set":{"class":"gold"}}
up=collection.update_many(prev,upd) 
print(up.modified_count)

#delete  data from database 
prev= {"Name":"parcha"}
collection.delete_one(prev)
# delete multiple data from database
prev= {"Name":"parcha"}
collection.delete_many(prev)

#REPLACE THE DATA FROM DATABSE 
prev= {"Name":"pal"}
rep={"age":"68"}
collection.replace_one(prev,rep)
#REPLACE MULTPLE DATA FROM DATABSE
prev= {"Name":"pal"}
rep={"age":"68"}
collection.replace_one(prev,rep) 

