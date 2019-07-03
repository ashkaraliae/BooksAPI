# mStakx-BooksAPI
To run the application follow the steps:-
    1. Create  a new folder and clone the repository, go inside mstakx folder
    2. DB Configurations:
        I am using postgres as local Database, so we need to update the db details
        in settings.py
    3. Run below commands:
        pip install -r requirements.txt
        python manage.py makemigrations
        python manage.py migrate
    4. Go inside mstakx folder and run below commands
        python manage.py runserver
    5. Now the server will be up and running

    
