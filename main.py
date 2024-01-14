# Импортируем библиотеку

from googletrans import Translator # Создаем переводчик
translator = Translator()  # Задаем исходные язык и целевой язык
text = input('Enter text to translate it: ')  # Переводим текст
src = 'auto'
dest = input('Entre a short language name. e.g. en - english, es-spanish: ') # Задаем исходный текст

translated_text = translator.translate(text, src=src, dest=dest).text  # Выводим переведенное предложение
print(translated_text)