from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import PartnerSerilizer
from .models import Partner
class PartnerViewSet(viewsets.ModelViewSet):
    queryset= Partner.objects.all()
    serializer_class = PartnerSerilizer
    def destroy(self, request, pk=None):
        queryset= Partner.objects.all()
        partner =get_object_or_404(queryset, pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)