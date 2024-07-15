#tts/urls.py
from django.urls import path
from .views import ChangeSoundView, GetAudioResultView

urlpatterns = [
    path('change_sound/', ChangeSoundView.as_view(), name=''),
    path('get_tts_task/<str:task_id>/', GetAudioResultView.as_view(), name='get_audio_result'),
    ]
