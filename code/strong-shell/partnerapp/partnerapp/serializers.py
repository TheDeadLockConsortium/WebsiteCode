from rest_framework import serializers
from .models import Partner

class PartnerSerilizer(serializers.ModelSerializer):
    class Meta:
        model= Partner
        fields= ['id', 'name', 'CompanySize', 'image', 'url']