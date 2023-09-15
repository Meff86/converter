# converter
Стандартный конверетер валют, работает с внешним api exchangeratesapi.io
Стек django+Drf 
Документация генерируется, swagger работает. 
Все токены спрятаны в переменных окружения
Пример запроса:
GET /api/rates?from=USD&to=RUB&value=1
