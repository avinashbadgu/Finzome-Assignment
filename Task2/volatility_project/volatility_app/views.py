# volatility_app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import calculate_volatility

@csrf_exempt
def calculate_volatility(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            result = calculate_volatility(file)
            return JsonResponse(result)
        else:
            return JsonResponse({'error': 'No file provided'}, status=400)
    else:
        return JsonResponse({'error': 'Unsupported method'}, status=405)
