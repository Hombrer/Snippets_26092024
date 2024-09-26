# Snippets_26092024

## Инструкция по развертыванию проекта

1. Создать виртуальное окружение:  
```
python3 -m venv django_venv
```

2. Aктивировать виртуальное окружение:  
```
source django_venv/bin/activate
```

3. Установить нужные пакеты:  
```
python -m pip install -r requirements.txt
```

4. Применить все миграция для создания таблиц в БД 
```
python manage.py migrate
```

5. Запустить сервер:  
```
python manage.py runserver
```

## Запуск `ipython` в контексте приложений проекта `django`
```
python manage.py shell_plus --ipython
```

## Выгрузка и загрузка данных
### Выгрузить данные из БД (Linux)
```
python manage.py dumpdata MainApp --indent 4 > MainApp/fixtures/save_all.json
```
### Выгрузить данные из БД (Windows)
```
python -Xutf8 manage.py dumpdata MainApp --indent 4 -o MainApp/fixtures/save_all.json
```

###  Загрузить данные в БД
```
python manage.py loaddata MainApp/fixtures/save_all.json
```