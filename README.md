# Awwards-App
This is a Django application that allows users to post their projects for others to rate and review

## Author  
  
LinkedIn - [KIPKEMOI ELVIS RONO](https://www.linkedin.com/in/elvis-rono-aa3548209/)


GITHUB - [ELVIS](https://github.com/DynastyElvis)

  
 
##  Live Link  
 Click [View Site](test)  to visit the site


[Go Back to the top](#Awwards-App)



### User Story

1. User registers
2. User Logins
3. User Edit their profile
5. User can submit their site
6. User can view other users site and review
7. user Can logout


[Go Back to the top](#Awwards-App)


## Technology used  

1. [Python](https://www.python.org/): programming language.
2. [Django](https://www.djangoproject.com/): web framework.
3. [Bootstrap](https://getbootstrap.com/): front-end framework.
4. [Javascript](https://www.javascript.com/) -programming language

[Go Back to the top](#Awwards-App)


### Installation
1. Clone this Github repository:
```
    git clone https://github.com/juliamwangi123/clone_awwards.git
     
    cd awwards

```

2. Install the pre-requisites:

```
      pip install -r requirements.txt
```


3. Copy the settings template to create your local settings:

```
    cp awwards/settings_local.template awwards/settings_local.py
```


4. Edit the local settings file with your settings:
```
     vi awwards/settings_local.py
```


5. Create the database and admin user:
```
    python manage.py syncdb
```



6. Collect static files:

```
   python manage.py collectstatic
```


7. Configure your web server to serve static files from the directory specified in the local settings file. 



8. Launch the application using the built-in runserver, or deploy using gunicorn, which is the application server of choice:

```
web: gunicorn awwards.wsgi --log-file -
```


[Go Back to the top](#Awwards-App)



## License

[MIT LICENCE](https://github.com/DynastyElvis/Awwards-App/blob/main/LICENSE)


Copyright (c) 2022 K. E. Rono



[Go Back to the top](#Awwards-App)

## Known Bugs

No Known Bugs.


[Go Back to the top](#Awwards-App)



## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at 
Email Address - [Kipkemoilvs@gmail.com](Kipkemoilvs@gmail.com)


[Go Back to the top](#Awwards-App)
