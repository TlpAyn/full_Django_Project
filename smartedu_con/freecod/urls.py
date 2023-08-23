from django.urls import path
from freecod.views import FreecodeListView


urlpatterns = [
    
    path('', FreecodeListView.as_view(), name="freecode"),


]
