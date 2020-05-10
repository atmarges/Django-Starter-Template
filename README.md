# Django-Stater-Template
A simple django starter template with [MDBootstrap](https://mdbootstrap.com/) design and ready-made authentication system usign [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/overview.html).

### Sign Up Page

![signup](https://user-images.githubusercontent.com/24236098/81509610-6762b900-933e-11ea-85c3-9affdbc2a8e4.jpg)

### Login Page

![signin](https://user-images.githubusercontent.com/24236098/81509612-69c51300-933e-11ea-8a24-3f865752b51a.jpg)

### After Login

![welcome](https://user-images.githubusercontent.com/24236098/81509611-692c7c80-933e-11ea-9e99-66f72325abf3.jpg)

# Quickstart
Create a python environment and install the required modules using pip.

```bash
C:\> cd django-starter-template

C:\django-starter-template\> virtualenv env
C:\django-starter-template\> env\Scritps\activate.bat

(env) C:\django-starter-template\> pip install -r requirements.txt 

```

Go to the `src` folder and rename the project using the `renameproject` command from manage.py. The example below renames the project to `myblog`.

```bash
$:\> python manage.py renameproject myblog
```

Generate a new django secret key using the `generatekey` command.

```bash
$:\> python manage.py generatekey
```

Run the `makemigration` command to generate migration files. The run `migrate` to apply the migrations to the database. Note: If you're planning to use another database, modify the `settings.py` first before executing `migrate`.

```bash
$:\> python manage.py makemigrations
$:\> python manage.py migrate
```

Finally, you can now use the `runserver` command to start the web server and visualize the output.

```bash
$:\> python manage.py runserver
```

## Features
- Authentication system using Django AllAuth
- Material design layout using MDBootstrap
- Easily extendable `User` model
- User avatar (image)
