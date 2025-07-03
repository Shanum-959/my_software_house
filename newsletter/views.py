# newsletter/views.py
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.core.mail import send_mail
# from .serializers import NewsletterSubscriptionSerializer
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# from .models import Subscriber
# from django.shortcuts import render
# 
# def newsletter_form_view(request):
#     return render(request, 'newsletter/subscribe.html')
# 
# 
# @api_view(['POST'])
# def subscribe_newsletter(request):
#     serializer = NewsletterSubscriptionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         
#         # Send confirmation email
#         email = serializer.validated_data['email']
#         confirmation_link = f"http://127.0.0.1:8000/newsletter/confirm/{email}/"  # or use a token system later
# 
#         send_mail(
#             subject='Confirm your newsletter subscription',
#             message=f'Thank you for subscribing! Please confirm here: {confirmation_link}',
#             from_email='no-reply@yourdomain.com',
#             recipient_list=[email],
#             fail_silently=False,
#         )
# 
#         return Response({'message': 'Subscribed successfully! Confirmation email sent.'}, status=status.HTTP_201_CREATED)
#     
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
# def confirm_subscription(request, email):
#     subscriber = get_object_or_404(Subscriber, email=email)
#     if not subscriber.confirmed:
#         subscriber.confirmed = True
#         subscriber.save()
#         return HttpResponse("✅ Your subscription has been confirmed. Thank you!")
#     return HttpResponse("ℹ️ Your subscription was already confirmed.")


from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Subscriber
from .serializers import NewsletterSubscriptionSerializer
from rest_framework.permissions import AllowAny


class NewsletterSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = NewsletterSubscriptionSerializer
    permission_classes = [AllowAny]


    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({'email': ['This field is required.']}, status=400)

        if Subscriber.objects.filter(email=email).exists():
            return Response({'email': ['You are already subscribed.']}, status=400)

        subscription = Subscriber.objects.create(email=email)
        serializer = self.get_serializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
