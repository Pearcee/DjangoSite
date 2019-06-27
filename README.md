# DjangoSite

DjangoSite
setup
git clone https://github.com/Pearcee/DjangoSite.git

git checkout master
git fetch -p origin
git merge origin/master
git merge master
git push origin

git status
git add --all .
git commit -m "Brunch"
git push

pip freeze > requirments.txt

django-admin.exe startproject mysite .
python manage.py startapp blog
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
