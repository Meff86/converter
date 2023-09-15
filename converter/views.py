from rest_framework import views, response
from .serializers import CurrencyConversionSerializer
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_latest_exchange_rates():
    """Получение актуально рейтинга валют"""
    access_key = os.getenv('ACCESS_KEY')
    url = f'http://api.exchangeratesapi.io/v1/latest?access_key={access_key}'
    response = requests.get(url)
    data = response.json()
    return data['rates']


class CurrencyConversionView(views.APIView):
    """Обработка Api"""

    def get(self, request):
        from_currency = request.query_params.get('from')
        to_currency = request.query_params.get('to')
        value = request.query_params.get('value')

        serializer = CurrencyConversionSerializer(
            data={'from_currency': from_currency, 'to_currency': to_currency, 'value': value})
        serializer.is_valid(raise_exception=True)

        rates = get_latest_exchange_rates()

        if from_currency not in rates or to_currency not in rates:
            return response.Response({'error': 'Unsupported currency'})

        conversion_rate = rates[to_currency] / rates[from_currency]

        result = float(value) * conversion_rate

        return response.Response({'result': result})
