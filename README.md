# P5 OpenFoodFacts

This Python project is a substitute research (console) application for a given food.
The application hosts in database (MySQL) about 3000 food products from openfoodfacts.

## For ease of use, here are some prerequisites: 

**Python 3.5+** compatible (typing module)

This application is standalone, to use it you must follow these indications:
- by clicking on the green button "Code", get the link and
-  `git clone link`
-  create a virtual environment in which you must install the modules from the requirements.txt file

To run the app, you must create the `.env` file at the same level as the `main.py` file :
```ini
DB_USER=your_login (e.g. root)
DB_PASSWD=your_passord
DB_HOST=your_host (e.g. localhost)

# And this data are used for the creation pre-filled in the 
# code of a new non-root user, his password and the name of the db.
# Leave them like that in the file.
OFF_PASSWD=spoff
OFF_USER=offp5
OFF_DB=offdb
```



## The patterns

The app works on the model of MVC design and strategy patterns.

In addition to the segregation of duties implied by the MVC model, the strategy model aims to give controllers the same behavior.
It is often used in various frameworks to provide users with the ability to modify the behavior of a class without extending it. The structure and navigation are really simplified. 
