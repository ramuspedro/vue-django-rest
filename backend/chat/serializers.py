from rest_framework import serializers
from chat.models import ChatSession
from chat.models import ChatSessionMessage

class ChatSessionSerializer(serializers.ModelSerializer):
  class Meta:
    model = ChatSession
    # fields = ('id', 'name', 'email', 'message')
    fields = '__all__'

class ChatSessionMessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = ChatSessionMessage
    # fields = ('id', 'name', 'email', 'message')
    fields = '__all__'