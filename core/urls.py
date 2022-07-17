from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [

    # ! Company Info
    path("company/", CompanyListCreateAPIView.as_view()),
    path("company/<int:pk>/", CompanyRetrieveUpdateDestroyAPIView.as_view()),

    # ! Ledger
    path("ledger/<int:user>", LedgerListCreateAPIView.as_view()),
    path("ledger/<int:user>/<int:pk>", LedgerRetrieveUpdateDestroyAPIView.as_view()),

    # ! Journal
    path("journal/", JournalListCreateAPIView.as_view()),
    path("journal/<int:pk>", JournalRetrieveUpdateDestroyAPIView.as_view()),

    # ! Group
    path("group", GroupListAPIView.as_view()),
    
]