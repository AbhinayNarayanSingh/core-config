from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext, gettext_lazy as _

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import *
from .serializers import *

from user.models import User
from user.serializers import UserSerializer

app_name = 'core'


# ! Company Info

class CompanyListCreateAPIView(ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


# ! Group

class GroupListAPIView(ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


# ! Ledger

class LedgerListCreateAPIView(ListCreateAPIView):
    serializer_class = LedgerSerializer
    def get_queryset(self):
        user = self.kwargs['user']
        return Ledger.objects.filter(user=user) 
    

class LedgerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LedgerSerializer
    def get_queryset(self):
        user = self.kwargs['user']
        pk = self.kwargs['pk']
        return Ledger.objects.filter(user=user, pk=pk) 


# ! Journal Entry

class JournalListCreateAPIView(ListCreateAPIView):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()

class JournalRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()
