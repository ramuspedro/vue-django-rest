from django.shortcuts import render

"""Views for the chat app"""

from django.contrib.auth import get_user_model

from .models import (
  ChatSession, ChatSessionMember, ChatSessionMessage, deserialize_user
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework import generics

from chat.serializers import ChatSessionSerializer
from chat.serializers import ChatSessionMessageSerializer

class ChatSessionView(generics.ListCreateAPIView):
  queryset = ChatSession.objects.all()
  serializer_class = ChatSessionSerializer
  permission_classes = (permissions.IsAuthenticated,)

  def perform_create(self, serializer): # new
    serializer.save(owner=self.request.user)

class ChatSessionMessageView(generics.ListCreateAPIView):
  queryset = ChatSessionMessage.objects.all()
  serializer_class = ChatSessionMessageSerializer

class ChatSessionViewTest(APIView):
  """"Menage Chat sessions."""

  permission_classes = (permissions.IsAuthenticated,)

  def post(self, request, *args, **kwargs):
    """Create a new chat session"""
    
    user = resquest.user

    chat_session = ChatSession.objects.create(owner = user)

    return Response({
      'status': 'SUCCESS',
      'uri': chat_session.uri,
      'message': 'New chat session created'
    })

  def patch(self, resquest, *args, **kwargs):
    """Add user to a chat session"""

    User = get_user_model()

    uri = kwargs['uri']
    username = resquest.data['username']
    user = User.objects.get(username = username)

    chat_session = ChatSession.objects.get(uri = uri)

    owner = chat_session.owner

    if owner != user: # Only allow non owners join the room
      chat_session.members.get_or_create(
        user = user,
        chat_session = chat_session
      )
    
    owner = deserialize_user(owner)

    members = [
      deserialize_user(chat_session.user)
      for chat_session in chat_session.members.all()
    ]

    members.insert(0, owner) # Make the owner the first member

    return Response({
      'status': 'SUCESS',
      'members': members,
      'message': '%s joined that chat' % user.username,
      'user': deserialize_user(user)
    })

class ChatSessionMessageViewTest(APIView):
  """"Create/Get Chat session messages."""

  permission_classes = (permissions.IsAuthenticated)

  def get(self, request, *args, **kwargs):
    """return all the messages in a chat session"""

    uri = kwargs['uri']

    chat_session = ChatSession.objects.get(uri = uri)

    messages = [
      chat_session_message.to_json()
      for chat_session_message in chat_session.messages.all()
    ]

    return Response({
      'id': chat_session.id,
      'uri': chat_session.uri,
      'messages': messages
    })

  def post(self, request, *args, **kwargs):
    """create a new message in a chat session"""
    
    uri = kwargs['uri']

    message = resquest.data['message']

    user = request.user
    chat_session = ChatSession.objects.get(uri = uri)

    ChatSessionMessage.objects.create(
      user = user,
      chat_session = chat_session,
      message = message
    )

    return Response({
      'status': 'SUCCESS',
      'uri': chat_session.uri,
      'message': message,
      'user': deserialize_user(user)
    })