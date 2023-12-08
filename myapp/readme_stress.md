### Aлгоритм для поставновки ударений

В основе алгоритма:

 - [авторская база данных](https://github.com/EugenefedorovPro/wiktionary_rus), созданная путем парсинга русского раздела en.wiktionary.org 
 - [авторская нейросеть](https://github.com/EugenefedorovPro/put_stress_rus)

Вначале алгоритм ищет слово в базе данных, которая включает 422 821 cловарных позиций. Если слово отсутствует, тогда подключается нейросеть. Точность нейросети - 79,5%. Данный показатель обусловлен спецификой ударения в русском языке, которое отчасти имеет стохастический характер.

Проект на [GitHub](https://github.com/EugenefedorovPro/put_stress_rus) с описанием на английском.