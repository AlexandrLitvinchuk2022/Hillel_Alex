# https://developer.mozilla.org/ru/docs/Web/HTTP
# Протокол передачи гипертекста (Hypertext Transfer Protocol - HTTP) - это прикладной протокол для передачи гипертекстовых
# документов, таких как HTML. Он создан для связи между веб-браузерами и веб-серверами, хотя в принципе HTTP может использоваться
# и для других целей. Протокол следует классической клиент-серверной модели, когда клиент открывает соединение для создания запроса
# , а затем ждёт ответа. HTTP - это протокол без сохранения состояния, то есть сервер не сохраняет никаких данных (состояние) между
# двумя парами "запрос-ответ". Несмотря на то, что HTTP основан на TCP/IP, он также может использовать любой другой протокол
# транспортного уровня с гарантированной доставкой.
#
# Методы HTTP-запроса
# GET
# POST
# OPTIONS
# DELETE
# TRACE
# PATCH
# другие
#
# Коды ответа (HTTP response codes)
# Коды ответа HTTP указывают на результат выполнения определённого HTTP-запроса. Ответы сгруппированы в пять категорий:\
# информационные ответы, удачные ответы, перенаправления, ошибки клиента и ошибки сервера.
#
# Условные HTTP запросы
# В HTTP есть понятие условных запросов, в которых результат, и даже успех запрос, могут быть изменены с помощью сравнения затронутых
# ресурсов со значением валидатора. Такие запросы могут быть полезными для валидации контента в кеше, и избавления от бесполезного
# контроля, чтобы проверить целостность документа, например, пока длится загрузка, или пока предотвращается потеря обновлений, пока
# выгружаются или изменяются файлы на сервере.
#
# Принципы
# Условные запросы HTTP это запросы, которые выполняются по разному, в зависимости значения особых заголовков.
# Эти заголовки определяют предусловие, и результат запроса будет разным, если условие согласовано или нет.
#
# Отличие в поведении определяется используемым методом, и набором заголовков для предусловий:
#
# для безопасных методов, например как GET, который обычно используется, чтобы получить документ, условный запрос
# отправит документ только если это уместно. Следовательно, это расширит пропускную способность.
# для небезопасных методов, например PUT, который обычно используется для выгрузки документа на сервер, условный
# запрос загрузит документ, только если оригинал, на котором он основан, хранится на сервере.
#
# Коды ответа HTTP
# Информационные 100 - 199.
# Успешные 200 - 299.
# Перенаправления 300 - 399.
# Клиентские ошибки 400 - 499.
# Серверные ошибки 500 - 599.
#
# Для разграничения действий с ресурсами на уровне HTTP-методов и были придуманы следующие варианты:
# GET — получение ресурса
# POST — создание ресурса
# PUT — обновление ресурса
# DELETE — удаление ресурса

########################################################################################################

import requests
response = requests.get('https://rozetka.com.ua')
print(f"{response.status_code=}")

response = requests.request(url='https://rozetka.com.ua', method="GET")
print(f"{response.status_code=}")
print(f"{response.content=}")

######################
# url = "https://jsonplaceholder.typicode.com/comments"
# params = {"postId": 1}
#
# # option 1
# response = requests.get(url, params=params)
# print(f"{response.status_code=}")
# # print(f"{response.content=}")  #
# print(f"{response.json()=}")