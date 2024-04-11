Create Virtualenv
pip install virtualenv
python<version> -m venv <virtual-environment-name>
1. Command to install Django
    pip install django
2. Command to check Django Version:
    python -m django --version
3. Command to check all the versions of installed modules:
    pip freeze
4. To create a project ---- django-admin startproject <projectname>
    projectname == mysite
5. Tp create an app    ---- python manage.py startapp <appname>
    appname == enggapp
6. cd mysite
7. To Run a project ---- pyhton manage.py runserver
8. python manage.py startapp <appname>
9. Add app name in INSTALLED_APPS inside the file mysite\mysite\settings.py 
10. Create Model
    Create a migration file inside the migration folder:
    i. python manage.py makemigrations
    ii. python manage.py migrate
    iii. python manage.py sqlmigration app_name miration_name
    python manage.py sqlmigrate app_name 0001
    python manage.py showmigrations
    python manage.py showmigrations app_name

11. admin.site.register(model_name)
12. First you need to run migrate to change the admin username and password. Run

    python manage.py migrate
    Then edit the username and password using

    python manage.py createsuperuser
    Then give an username and password and a email.
    Enter your desired username and press enter.
        Username: admin
    You will then be prompted for your desired email address:
        Email address: admin@example.com
    The final step is to enter your password twice, the second time as a confirmation of the first.
        Password: ********
        Password (again): ********
        Superuser create successfully.

Email: ashit.gajbhiye@citiustech.com
Username: ashitg
Password: superuser123

13. Change database sqllite to postgresql
    enggservicesite\enggservicesite\settings.py
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'enggservices',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}

14. Install postgres library
    pip install psycopg2