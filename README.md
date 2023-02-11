# Тестовое задание Django+StripeAPI.
## Запуск проекта
Предварительно, необходимо:
1. зарегистрироваться и авторизоваться на https://stripe.com <br><br>
2. скопировать `Publishable key` и `Secret Key`(*'developers' > 'API Keys'*) <br><br>
3. `git clone https://github.com/Gimmyhat/django_stripe_checkout.git` <br><br>
4. в корневой папке проекта создать файл .env и заполнить его следующими данными:<br><br>
   - SECRET_KEY=`'django secret key'`
   - STRIPE_PUBLISHABLE_KEY=`'Publishable key'`
   - STRIPE_SECRET_KEY=`'Secret key'` <br><br>
5. Запустить docker-compose:
```sh
docker-compose up --build
```

Логин/пароль от админки `admin/admin` 

Для тестирования можете использовать следующие номера карт:

4242 4242 4242 4242\
4000 0000 0000 3220\
4000 0000 0000 9995
