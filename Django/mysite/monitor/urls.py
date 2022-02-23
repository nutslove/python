from django.urls import path
import sys
from pathlib import Path
sys.path.append(str(Path('__file__').resolve().parent.parent))
from . import views
import example.views as examview

urlpatterns = [
    path('', views.index, name="index"),
    path('next', views.next, name="next"),
    path('exam/', examview.index, name="examindex"),
]
