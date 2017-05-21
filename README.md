# DOCKERIZE TELEGRAM SERVIS

## Dependieces:
* NGINX
* MongoDB
* Telegram
* Flask


``` sh
$ cd dockerize-telegram
$ docker-compose build #it build all dependieces.
$ docker-compose up # wake up all system.
``` 
# HINTS :

  We need some trick for up the telegram_db_service case : 
  3 containers are in the same network.So hosts names are changed.
  You need to change the host name of your db client,
  For example :
  ``` python
    client = MongoClient("localhost",4967)

    ###to client = MongoClient(HOST_NAME_ON_DOCKER,PORT_NUMBER_OF_MONGODB_ON_DOCKER)

    client = MongoClient("db",27017)

  ``` 
  Next trick is for the NGINX :
  
  ```
   ## The [PORT] is not use with another service on your host machine.
          if it is using by another service change [PORT] from sites-enabled/flask_config and 
  
  server {
          listen [PORT] 
     } 
  //docker-compose.yml
     nginx {
      expose:
         - "[PORT]:[PORT]"
     }
    ....
   ``` 
   If you wanna run telegram service on your 
   80 port you must check which service using your 80 port.
   ``` sh
      $ sudo netstat -plnt | grep ':80'
   ``` 
   
  
