# To Do Web App in using Django

* Install Django
```commandline
pip install django
```

* Create App using django-admin
```commandline
django-admin startproject todo .
```

* Run development server locally
```commandline
python manage.py runserver
```

![Django default landing page]()

* Quit development server```ctrl + c```

* Go to todo project folder and add 'templates' to 'DIRS' in ```settings.py```
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
```

* Create a 'templates' folder
```commandline
mkdir templates
```

* Go to templates folder
```commandline
cd templates
```

* Create a file index.html in ```templates``` directory
```commandline
touch index.html
```

* Go to [Bootstrap Getting Started](https://getbootstrap.com/docs/5.1/getting-started/introduction/) and copy starter template

* Paste starter template in ```index.html```

* Go to ```settings.py``` file and add ```'todo',```
```python
# Application definition

INSTALLED_APPS = [
    'todo',
    'django.contrib.admin',
    'django.contrib.auth',
```

* In todo directory create a file ```views.py```
```commandline
touch views.py
```

* Add the following code to ```views.py```
```python
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
```

* Go to ```urls.py``` file and add following code
```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
]
```

* Test your urls and template by running server again
```commandline
python manage.py runserver
```

![Django Hello World Template]()

* Prepare a form for ToDo input.

