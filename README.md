# Code Institute

## About
A repo to demostrate the functionality of the Code Institute project "Boutique Ado"

## To recreate
1) Clone the Repo or if you are using GitPod, select the green "GitPod" button.
2) Install required libraries
  - pip3 install -r requirements.txt
3) Create "env.py" file and add the minimum requirements from the "example_env.py" file.
  - touch env.py
  - Copy line 1 to 10 of "example_env.py" into the newly created "env.py" file. 
4) Make migrations and migrate
  - python3 manage.py makemigrations
  - python3 manage.py migrate
5) Generate Product Data from products/fixtures
  - python3 manage.py loaddata collections
  - python3 manage.py loaddata products
6) Run the server
  - python3 manage.py runserver

Note - You may have to add a new host to your ALLOWED_HOSTS list in settings.py.  Django will tell you the name of the host to add and you can copy and paste.