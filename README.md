### WEB сервис-агрегатор курса валют выдающий текущий курс валют и историю изменения курса валют с доступом только для авторизованных пользователей.
* Текущие и исторические данные об обменных курсах предоставлены Альфабанком, Белагропромбанком, Беларусбанком

---

#### 1. Необходимые зависимости:
* django
* postgresql (psycopg2)
* rest-framework
* redis
* celery
---

#### 2. Начало
* Этот проект является самостоятельной бесплатной демоверсией, созданной на базовых знаниях Python и Django, и как любой проект может иметь некоторые проблемы. 
---

#### 3. Внутренняя работа
* Используется БД Postgresql (для работы с БД устанавливаем модуль psycopg2)
* Для запуска redis используем настройки описанные в docker-compose командой: docker-compose up
* Для запуска celery(запись в БД актуальных курсов валют за текущий день) используем команду: celery -A devtest worker -l INFO
* Запуск сервера командой: python manage.py runserver 8080
---

#### 4. Процесс для клиента
* Запуск программы комаандой: python manage.py runserver
* Для регистрации: добавляем register/ и проходим регистрацию в соответствии с требованиями полей.
* Для входа в систему: добавляем login/ и заполняем данные, исходя из регистрации
* Далее, для просмотра курсов валют, необходимо в зависимости от банка изменить url 
> > Альфабанк: http://127.0.0.1:8000/company/rates/Название банка/

> > Названия банков: alfabank, belagro, belbank
* Данные ссылки доступны только для авторизованных пользователей!!!
* Для неавторизованных пользователей предусмотрены ссылки, дающие возможность только для просмотра курсов валют:
> > Альфабанк: http://127.0.0.1:8000/company/sellrates/Название банка/

> > Названия банков: alfabank, belagro, belbank
* По умолчанию, валюты указаны по международным стандартам с учетом покупки банком (buy) и продажи банком (sell)
* Для просмотра текущего и за определенные даты курсов валют:
> > За определенный день курс валют: http://0.0.0.0:8000/company/date/?company="Название"&date=2021-09-03
> 
> > За определенный интервал дат курс валют: http://0.0.0.0:8000/company/dateinterval/?company="Название"&date_start=2021-09-03&date_end=2021-09-05
>
> > За текущий день курс валют почасовой: http://0.0.0.0:8000/company/datetoday/"Название банка"
> 
---
#### 5. Использование
* В проекте используются API банков с принимаемыми данными в формате JSON и XML.
* Валюты используемые в проекте: EUR, USD, RUR
---

#### 6. Terminal
* docker-compose up
