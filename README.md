# drf_listings_example - пример DRF доски объявлений

- db - sqlite
- jwt-auth
- эндпойнты на создание пользователя, авторизацию, создание/обновление/удаление объявления
- вывод всех объявлений
- permissions

Для запуска:
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

#TODO:
- докеризация
- расширение моделей Accounts и Listings
- etc