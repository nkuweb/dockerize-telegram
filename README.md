# DOCKERIZED TELEGRAM SERVICES

* MongoDB
* Telegram
* Flask


``` sh
$ cd dockerize-telegram
$ docker-compose build #it build all dependieces.
$ docker-compose up # wake up all system.
``` 
We need another trick in this case : 
3 containers are in the same network.So hosts names are changed.
You need to change the host name of your db client,
For example :
``` python
  client = MongoClient("localhost",4967)
  
  ###to client = MongoClient(HOST_NAME_ON_DOCKER,PORT_NUMBER_OF_MONGODB_ON_DOCKER)
  
  client = MongoClient("db",27017)
   
``` 
