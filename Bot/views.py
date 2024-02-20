from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import openai

def chat(request):
    return render(request,'index.html')

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
