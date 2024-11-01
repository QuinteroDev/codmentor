from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .utils import generate_openai_feedback

@method_decorator(csrf_exempt, name='dispatch')
class FeedbackView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            user_code = data.get('code')
            exercise_description = data.get('exercise_description')
            result = data.get('result')

            if not user_code or not exercise_description:
                return JsonResponse({'error': 'Code or exercise description missing'}, status=400)

            # Generar feedback usando OpenAI
            feedback = generate_openai_feedback(
                user_code=user_code, 
                expected_output=result, 
                exercise_description=exercise_description)

            return JsonResponse({'feedback': feedback})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)