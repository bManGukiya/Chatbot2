from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import openai

def index(request):
    return render(request,'chat.html')

def chatAPI(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        if not prompt:
            return JsonResponse({'error': 'Prompt cannot be empty'})
        openai.api_key = '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'
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "how can i help you."},
                    {"role": "user", "content": prompt},
                ],
            )
            print(response)
            assistant_reply = response['choices'][0]['message']['content']
            return JsonResponse({'response': assistant_reply})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Invalid request method'})
