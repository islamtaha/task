# task
simple django application task

## Intsallation:
1- Install python-pip

2- Install python requirements

$ sudo pip install -r requirements.txt

3- install mysql

$ sudo apt-get update

$ sudo apt-get install mysql-server

4-Allow remote access for mySql

$ sudo ufw allow mysql

5-Start the MySQL service

$ systemctl start mysql

$ systemctl enable mysql

6- add database testDatabase to mysql and change the root password into 'password'

$ /usr/bin/mysql -u root -p
> UPDATE mysql.user SET Password = PASSWORD('password') WHERE User = 'root';

> FLUSH PRIVILEGES;

> CREATE DATABASE testDatabase;

7-open another terminal for reset password sending mail debuging and type the following command

$ python -m smtpd -n -c DebuggingServer localhost:1025

8- make migrations and run the server

$ python manage.py makemigrations

$ python manage.py migrate

$ python manage.py runserver


## API

url for api:

http://127.0.0.1:8000/account/api/v1/profiles/
