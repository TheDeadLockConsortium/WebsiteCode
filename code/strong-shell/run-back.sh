python ./partnerapp/manage.py createsuperuser
python ./partnerapp/manage.py makemigrations partnerapp
python ./partnerapp/manage.py makemigrations
python ./partnerapp/manage.py migrate
python ./partnerapp/manage.py runserver