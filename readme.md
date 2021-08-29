# E-diaristas project

### Installing the project

#### Clone the project
``` git clone https://github.com/felipepanegalli/e-diaristas.git ```

#### Install the dependencies
``` pip install -r requirements.txt ```

#### Change de DB config in ` settings.py `
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "db_name",
        "HOST": "db_host",
        "PORT": "db_port",
        "USER": "db_password",
        "PASSWORD": "db_password",
    }
}
```

#### Migrate the database
``` python manage.py migrate ```

#### Start the server
``` python manage.py runserver ```