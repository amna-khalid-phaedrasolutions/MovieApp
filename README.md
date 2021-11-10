# MovieApp

It was training task which is basically a movie portal. These are the features which are significant: 
 - Login
 - Signup
 - User can see movie
 - Add new movie
 - Add new user
 - Edit or delete movie
 - User profile.

## Setup

The first thing to do is to clone the repository:

```
git clone git@github.com:amna-khalid-phaedrasolutions/MovieApp.git
cd MovieApp
```

Make sure`Python3` & `pip` is installed

Create a virtual environment to install dependencies in and activate it:
```
python3 -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:
```
pip install -r requirements.txt
```

In order to create & apply migrations through:
```
python manage.py makemigrations
python manage.py migrate
```

Once `pip` has finished downloading the dependencies & `migrations` has been applied. Run server through:
```
python manage.py runserver
```

And navigate to 
`http://127.0.0.1:8000`
