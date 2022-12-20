# Установка базового образа
FROM python:3.10-alpine

# Установка рабочего директория внутри контейнера
# Директорий будет создан, если его не было
# В дальнейшем будет использоваться как базовый
WORKDIR /app

# Копирование зависимостей
# Для того чтоб не пересобирать их каждый раз при сборке
COPY requirenments.txt .

# Выполнение необходимых команд
RUN pip install -U pip
RUN pip install -r requirenments.txt

# Копирование остальных файлов проекта
COPY . .

# Этот параметр требуется переопределить при СОЗДАНИИ контейнера, т.е. run команде
CMD ["pytest", "--browser", "firefox"]

# docker build -t tests .    -создаю докер образ
# docker run -it tests:latest sh    -запускаю докер образ и смотрю что в нем хранится. sh вместо bash используется по тому что юзаю alpine