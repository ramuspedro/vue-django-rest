from django.db import models

"""Models for the chat app."""
from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

def deserialize_user(user):
  """Deserialize user instance to JSON"""
  
  return {
    'id': user.id,
    'username': user.username,
    'email': user.email
  }

class TrackableDateModel(models.Model):
  """Abstract model to track the creation/updated date for a model"""

  create_date = models.DateTimeField(auto_now_add = True)
  update_date = models.DateTimeField(auto_now_add = True)

  class Meta:
    abstract = True

def _generate_unique_uri():
  """Generates a unique uri for the chat session"""
  return str(uuid4()).replace('-', '')[:15]

class ChatSession(TrackableDateModel):
  """A chat session. The uri's are generated by tracking the first 15 characters from UUID"""

  owner = models.ForeignKey(User, on_delete = models.PROTECT)
  uri = models.CharField(max_length=200, default = _generate_unique_uri)

class ChatSessionMessage(TrackableDateModel):
  """"Store messages for a session"""

  user = models.ForeignKey(User, on_delete = models.PROTECT)
  chat_session = models.ForeignKey(
    ChatSession, related_name = 'messages', on_delete = models.PROTECT
  )
  message = models.TextField(max_length=2000)

  def to_json(self):
    """deserialize message to JSON."""
    return {
      'user': deserialize_user(self.user),
      'message': self.message
    }

class ChatSessionMember(TrackableDateModel):
  """store all users in a chat session"""
  chat_session = models.ForeignKey(
    ChatSession, related_name = 'members', on_delete = models.PROTECT
  )
  user = models.ForeignKey(User, on_delete = models.PROTECT)