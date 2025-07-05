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
