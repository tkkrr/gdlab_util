from django.urls import path

from . import views
from django_pdfkit import PDFView
from .models import Journal

app_name = 'journal'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('form/', views.CreateView.as_view(), name='create'),
    path('update/', views.UpdateView.as_view(), name='update'),
    path('<int:journal_id>/pdfcreate/', views.pdfview, name='pdfview'),
    # path('<int:journal_id>/pdfcreate/', PDFView.as_view(template_name='journal/pdfview.html', inline), name="temp_pdfview")
]
