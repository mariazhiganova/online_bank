# Проект "Приложение для анализа банковских операций"

## Описание
Приложение для анализа транзакций, которые находятся в Excel-файле. 
Приложение генерирует JSON-данные для веб-страниц, формирует отчеты, а также предоставляет другие сервисы.
Разработано в учебных целях. 

### Описание модулей
Excel-файл с транзакциями хранится в модуле __data__.

В пакете __src__ находятся модули с функциями:

Основные функции для генерации JSON-ответов реализованы в отдельном модуле __views__.
Данные для анализа и вывода на веб-страницах — это данные с начала месяца, на который выпадает входящая дата, по входящую дату.
Валюты и акции для отображения на веб-страницах заданы в отдельном файле пользовательских настроек __user_settings.json__.

Сервис для определения выгодных категорий повышенного кэшбека реализован в модуле __services__. В дальнейшем, возможно, будут добавлены и другие сервисы.
Сервис позволяет проанализировать, какие категории были наиболее выгодными для выбора в качестве категорий повышенного кешбэка.

Функция для формирования отчета трат по категориям реализована в модуле __reports__. В дальнейшем, возможно, будут добавлены и другие отчеты.
Функция возвращает траты по заданной категории за последние три месяца (от переданной даты).

Для функций отчетов также написан декоратор. Он находится в модуле __decorators__. Декоратор записывает сформированный в формате DataFrame отчет в файл.

В модуле __utils__ расположены вспомогательные функции для чтения файлов.

В модуле __external_api__ находятся функции для получения данных о валютах и акциях через Open API *api.apilayer.com* и *api.polygon.io*

В пакете __tests__ находятся тесты на функции основного функционала.

В файле __logging_config__ реализован логгер, который используется в функциях, выполняющих основной функционал.

Финальным модулем проекта выступает **main**,

## Разработка

### Установка
1. Клонируйте репозиторий
```commandline
git clone git@github.com:mariazhiganova/online_bank.git

```
2. Установите зависимости
```commandline
poetry install
```

### Конфигурационные файлы

В проекте есть файлы конфигурации, в которых находятся переменные для записи в них путей к файлам и других параметров.
В файле **.env.example** хранится API-ключ. Создайте файл .env из копии этого файла и замените значения переменных реальными данными.
В файле **settings** находятся универсальные пути к файлам логирования, а также к файлам с информацией о банковских транзакциях.

### Тестирование 
Проект покрыт юнит-тестами Pytest.

Чтобы запустить тесты с оценкой покрытия выполните команду:
```commandline
poetry run pytest --cov
```
Чтобы сгенерировать отчет о покрытии в HTML-формате, где src — пакет c модулями, которые тестируем. 
Отчет будет сгенерирован в папке htmlcov и храниться в файле с названием index.html.
```commandline
pytest --cov=src --cov-report=html
```
### Логирование
Логирование корректной работы функции и возникающих ошибок реализовано в модулях **masks** и **utils**. Лог-файлы создаются в директории **logs**.

### Команда проекта

- **Мария Жиганова** - Junior Backend Developer (Python)

#### P.S.:
Проект разрабатывался в учебных целях и в сжатые сроки:) За недоработки понять и простить.
