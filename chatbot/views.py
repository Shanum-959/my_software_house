from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session
from .models import ChatMessage
import json

@csrf_exempt
def chat_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message')
            if not message:
                return JsonResponse({'error': 'Message is required'}, status=400)

            # Get or create session
            session_id = request.session.session_key
            if not session_id:
                request.session.create()
                session_id = request.session.session_key

            # Save user message
            chat_message = ChatMessage.objects.create(
                user=request.user if request.user.is_authenticated else None,
                session_id=session_id,
                message=message,
            )

            # Mock bot response
            response = get_mock_response(message.lower())
            chat_message.response = response
            chat_message.save()

            return JsonResponse({'response': response})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_mock_response(message):
    # Mock responses tailored for a software house context
    message = message.lower()

    if 'help' in message or 'support' in message:
        return "How can we assist you today? Our support team is here to help with your project or service inquiries."

    elif 'service' in message or 'offer' in message or 'provide' in message:
        return "We offer custom software development, UI/UX design, digital marketing, and more. Visit our Services page for full details!"

    elif 'project' in message or 'build' in message or 'develop' in message:
        return "We’d love to hear about your project! Tell us your idea, and our team will guide you from planning to launch."

    elif 'price' in message or 'cost' in message or 'budget' in message:
        return "Our pricing depends on your project scope. Contact us for a free consultation and quote."

    elif 'time' in message or 'duration' in message:
        return "Project timelines vary based on complexity. Small websites may take 1–2 weeks, while full-scale apps take longer."

    elif 'portfolio' in message or 'example' in message:
        return "You can view our recent projects on the Portfolio page. Let us know if you'd like similar solutions."

    else:
        return "Thanks for reaching out! Please let us know how we can help you with your digital goals."
