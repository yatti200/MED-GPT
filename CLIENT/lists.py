from .models import Conversation
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

class ConversationDelete(DeleteView):
    
    model = Conversation
    success_url = reverse_lazy('client-chatbot')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)