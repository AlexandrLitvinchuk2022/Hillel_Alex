#######
# - Создал проект my_shany_env. Перезапустил терминал. Получил следующит ответ от PyCharm:
# Невозможно загрузить файл C:\CODE\envs\my_shiny_env\Scripts\activate.ps1, так как выполнение сценариев отключено в этой системе. Для получения дополнительных
# сведений см. about_Execution_Policies по адресу https:/go.microsoft.com/fwlink/?LinkID=135170.
#     + CategoryInfo          : Ошибка безопасности: (:) [], ParentContainsErrorRecordException
# Дальше решил работать с существующим окружением:
# С помощью pip install проверил всё что уже установлено. Достаточно много всего.

# Заупустил pip install requests.  Установил новый релиз:
# [notice] A new release of pip available: 22.2.2 -> 22.3.1
# [notice] To update, run: python.exe -m pip install --upgrade pip

# Запустил pip uninstall requests Получил ответ:

# Found existing installation: requests 2.28.1
# Uninstalling requests-2.28.1:
#   Would remove:
#     c:\users\alex\appdata\local\programs\python\python310\lib\site-packages\requests-2.28.1.dist-info\*
#     c:\users\alex\appdata\local\programs\python\python310\lib\site-packages\requests\*
# Proceed (Y/n)? Запустил

# Повторно установил pip install requests
# Получил ответ
# Your response ('запустил pip install requests') was not one of the expected responses: y, n,
# Proceed (Y/n)?
# Указал Y
# Успешно Successfully uninstalled requests-2.28.1


###################
# pip install numpy
# обновил существующюю версию

###################
# pip install locust
# обновил существующюю версию. Время заняло чуть больше обічного.
