# Проект Juneberries

## Описание
<p>
  Juneberries — это

  Основные возможности:
</p>

### Технологии
Python 3.11, FastAPI, PostgreSQL, MongoDB, Redis, Kafka, Celery
## Техническое описание
---
### Инструкция запуска проекта на локальном компьютере
#### 1. Установите Docker, если его нет:
**для Windows**

- *Сначала установите Windows Subsystem for Linux по [инструкции с официального сайта Microsoft](https://learn.microsoft.com/ru-ru/windows/wsl/install).*
- *Зайдите на [официальный сайт](https://www.docker.com/products/docker-desktop/), скачайте и установите Docker Desktop.*

**для Linux**

- *Скачайте и установите curl — консольную утилиту, которая умеет скачивать файлы по команде пользователя:*
```
sudo apt update
sudo apt install curl
```
- *С помощью утилиты curl скачайте скрипт для установки докера с официального сайта:*
```
curl -fSL https://get.docker.com -o get-docker.sh
```
- *Запустите сохранённый скрипт с правами суперпользователя:*
```
sudo sh ./get-docker.sh
```
- *Дополнительно к Docker установите утилиту Docker Compose:*
```
sudo apt install docker-compose-plugin
```
- *Проверьте, что Docker работает:*
```
sudo systemctl status docker
```

**для macOS**

- *Зайдите на [официальный сайт](https://www.docker.com/products/docker-desktop/) и скачайте установочный файл Docker Desktop для вашей платформы — Apple Chip для процессоров M1/M2 и Intel Chip для процессоров Intel.*
- *Откройте скачанный DMG-файл и перетащите Docker в Applications, а потом — запустите программу Docker.*

#### 2. Склонируйте проект себе на компьютер:
- *В терминале выполните команду из той директории, в которой хотите разместить проект:*
```
git@github.com:VanZep/Juneberries.git
```
- *Перейдите в корневую директорию проекта:*
```
cd Juneberries
```
#### 3. В корневой директории проекта создайте файл .env:
```
touch .env
```
#### 4. Наполните его данными по аналогии с файлом .env.example:
```
nano .env
```
#### 5. Разверните проект на локальном компьютере:
- *В терминале, из директории /Juneberries, выполните команду:*
```
docker compose up
```
---
### Инструкция запуска проекта на удалённом сервере


### Автор:
***VanZep***
