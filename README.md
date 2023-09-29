# Заметочник на Flask
Простой заметочник для курса "Программирование на Python"

## Команды для запуска на ВМ
1. Получить requirements.txt
```
pip freeze
pip freeze > requirements.txt
```

3. После создания ВМ залогинимся на сервере и выполним
```
sudo apt update 
```
3. Проверим установлен ли pip
```
pip3 --version 
```
если не установлен 
```
sudo apt install python3-pip
```
4. Проверим git
```
git --version
```
если не установлен
```
sudo apt install git
```
5. Установим изолированную среду
```
sudo apt install python3-virtualenv
```
7. стянем наш репозиторий
```
git clone https://

cd todo_app
```

7. Создадим среду todoenv
```
virtualenv todoenv
```

8. Запустим среду
```
source todoenv/bin/activate

pip list
```
9. Установка всех необходимых пакетов 
```
pip install -r requirements.txt 
```
10. Установим gunicorn
```
pip install gunicorn
```
11. Отредактируем файл проекта
```
vim app.py
=======================================
if __name__ == "__main__":
    app.run(host='0.0.0.0')

:wq
=======================================

python app.py

http://<ip-adress>:5000
```
12. Точка входа wsgi (gunicorn)

```
vim wsgi.py

=======================================
from todo_app.app import app

if __name__ == "__main__":
    app.run()
=======================================
```
```
gunicorn --bind 0.0.0.0:5000 wsgi:app
```
13. Чиним ошибки
```
vim app.py
=======================================
@app.before__request
def create_tables():
    db.create_all()
=======================================

14. Автозапуск systemd
```
deactivate
```
```
sudo vim /etc/systemd/system/todo_app.service
```
=======================================
[Unit]
Description=Gunicorn instance to serve todo
After=network.target

[Service]
User=testadmin
Group=www-data
WorkingDirectory=/home/testadmin/
Environment="PATH=/home/testadmin/todo_app/todoenv/bin"
ExecStart=/home/testadmin/todo_app/todoenv/bin/gunicorn --workers 3 --bind unix:todo_app.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
=======================================
```
```
sudo systemctl start todo_app
sudo systemctl enable todo_app
```
```
sudo systemctl status todo_app
```
