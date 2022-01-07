# Серверная часть
:shipit: для установки [прочитать](./install.md)

## О проекте
в проекте используется mysql в качестве субд и требуется ее наличие перед использованием самого серверного программного обеспечение
<br>

### Создание базы
Для простоты развертывания системы написан скрипт по созданию базы и заполнению ее данными
<br>
В папке ***crete_base*** находяится настройки базы и файлы для автоматизации процессов создания и удаления базы
- [settings.py](./create_base/settings.py) хранит в себе базовые настройки базы 
- [show_datebases.py](./create_base/show_datebases.py) выводит на экран все существующие базы согласно [настройкам](./create_base/settings.py)
- [drop_db.py](./create_base/drop_db.py) удаляет базу согласно [настройкам](./create_base/settings.py)
- [create_db.py](./create_base/create_db.py) создает базу согласно [настройкам](./create_base/settings.py) и заполняет ее данными (из-за того, что данные заполняются очень быстро, время на сабсервисах будет отображаться одно и то же со стороны клиента)
### Ссновные файлы проекта
Для запуска сервера нужно запустить файл [run.py](./run.py), в нем запускается сервер по прописанному в данном файле url (http://localhost:8000/) и вызывается хендлер из [server_handler.py](./server_handler.py)
### Структура базы
База состоит из 2х таблиц:
- servises
- subservises

***servises*** состоит из 2х полей:
- id (инкремент)
- name (текстовое поле)

***subservises*** имеет такие поля:
- id (инкремент)
- servis_id (поле для связи с таблицей сервисов, хранит ид родительского сервиса)
- name (текстовое поле)
- price (поле типа DECIMAL с 2 символами после запятой)
- date (поле типа TIMESTAMP с автоматическим заполнением)

Существует связь один ко многим между таблицами 