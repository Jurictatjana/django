Postavljanje virtualne okoline (PyCharm)
    u terminalu pokrenuti: `python3 -m venv .venv`

Aktivirati virtualnu okolinu
    Terminal: `. .venv/Scripts/activate`

U aktiviranoj virtualnoj okolini instalirati Django

`pip install django`

Pokrenuti projekt

`django-admin startproject movies .`


pokretanje servera
`python manage.py runserver`

kreiranje usera za admin stranicu
    python manage.py createsuperuser
    username: admin
    email: admin@email.com
    password: admin


nakon kreiranja modela (objekt koji opisuje podatke aka tablica) potrebno je napraviti migraciju.
`python manage.py makemigrations movies`

python manage.py migrate movies

dodavanje tablice na admin stranicu