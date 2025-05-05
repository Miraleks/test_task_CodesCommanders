# User & Order API

[Перейти к инструкции на русском 🇷🇺](#инструкция-на-русском-языке)

---

## English Instructions

### Clone the repository:
```
git clone https://github.com/your-username/user-order-project.git
cd user-order-project
```

### Create `.env` file:
Create a `.env` file in the project root and add the following (example):
```
DB_NAME=mydb
DB_USER=user
DB_PASSWORD=password
DB_HOST=db
SECRET_KEY=your-django-secret-key
```

### Generate a Django SECRET_KEY:
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Build and run with Docker:
```
docker-compose up --build -d
```

### Apply migrations:
```
docker-compose exec web python user_order_project/manage.py migrate
```

### Create a superuser (optional):
```
docker-compose exec web python user_order_project/manage.py createsuperuser
```

### Open in browser:
- API: [http://localhost:8000/api/](http://localhost:8000/api/)
- Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Инструкция на русском языке

### Клонируйте репозиторий:
```
git clone https://github.com/your-username/user-order-project.git
cd user-order-project
```

### Создайте Django SECRET_KEY:
```
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Создайте файл `.env` в корне проекта:
Пример содержимого:
```
DB_NAME=mydb
DB_USER=user
DB_PASSWORD=password
DB_HOST=db
SECRET_KEY=your-django-secret-key
```

### Соберите и запустите контейнеры:
```
docker-compose up --build -d
```

### Примените миграции:
```
docker-compose exec web python user_order_project/manage.py migrate
```

### Создайте суперпользователя (по желанию):
```
docker-compose exec web python user_order_project/manage.py createsuperuser
```

### Откройте в браузере:
- API: [http://localhost:8000/api/](http://localhost:8000/api/)
- Админка: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Примечание

- После изменений в моделях выполните:
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

- Убедитесь, что `.env` загружается через `python-dotenv`.

