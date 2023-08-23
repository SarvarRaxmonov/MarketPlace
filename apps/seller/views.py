from rest_framework import generics, viewsets
from .models import Profile, SendInquiry
from .serializers import ProfileSerializer, SendInquirySerializer


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class SendInquiryViewSet(viewsets.ModelViewSet):
    queryset = SendInquiry.objects.all()
    serializer_class = SendInquirySerializer
