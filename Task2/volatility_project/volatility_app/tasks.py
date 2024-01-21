from celery import shared_task
from .utils import calculate_volatility

@shared_task
def calculate_volatility_from_csv(file):
    result = calculate_volatility(file)
    return result
