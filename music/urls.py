from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),

    # path('song/<int:song_id>/', show_song, name='song'),

    path('category/<int:category_id>/', show_category, name='category'),
    path('detailed/<int:pk>', detailed, name='detailed'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),

]

# делаю проект на основе сайта SEFON.SU
