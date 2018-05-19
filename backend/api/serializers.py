from rest_framework import serializers
from leads.models import Lead
from users.models import CustomUser

class LeadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lead
    # fields = ('id', 'name', 'email', 'message')
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('email', 'username')