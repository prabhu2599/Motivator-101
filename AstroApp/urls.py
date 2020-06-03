from django.urls import path
from .views import AstroView,AstroAll

urlpatterns = [
    path('all/', AstroView.as_view()),
    path('show/', AstroAll.as_view())
]