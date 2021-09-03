
# OC-QL-P10 / SoftDesk 


***

## 1.Presentation
***
Créer une API sécurisée RESTful en utilisant Django REST
1) Description de l'application:<br>
Ce projet consiste à développer une API sécurisée, pour le compte de la société SoftDesk, permettant d’accéder à une application de suivi de développement logiciel.
2) Frameworks utilisés:
   * Django : pour le développement de sites web en Python
   * Django REST Framework : pour concevoir des API REST avec Django
3) Packages supplémentaires:
   * Django REST Framework simple JWT  : package pour gérer l'authentification via des JSON Web Token (JWT)


## 2-Installation  :
***
Se diriger sur le repertoire où l'on souhaite installer l'application.

Pour installer le programme via un terminal :  

Sous Windows :  
```sh
$ git clone https://github.com/quentin8469/OC-QL-P10   
$ python3 -m venv env  
$ env/scripts/activate  
$ pip3 install -r requirements.txt   
```
Sous linux/Mac :      
```sh
$ git clone https://github.com/quentin8469/OC-QL-P10 
$ python3 -m venv env    
$ source env/bin/activate    
$ pip3 install -r requirements.txt    
```

**Lancement du serveur Django** :

* Se rendre dans le repertoire contenant le fichier python ' manage.py ' ( API_SoftDesk )
* Puis exécuter python manage.py runserver
* La page sera accessible à l'URL suivante:  http://127.0.0.1:8000/

## 3-Fonctionnement:

* Se referer à la documentation POSTMAN pour efectuer les tests.
* lien: https://documenter.getpostman.com/view/16984358/U16evntT


***
Créer un rapport flake8 :  

`flake8 --exclude=env,venv --format=html --htmldir=flake8_report --max-line-lengt=119`

