# Copyright (c) 2011-2021 Berkeley Model United Nations. All rights reserved.
# Use of this source code is governed by a BSD License (see LICENSE).

from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from huxley.api.mixins import ListUpdateModelMixin
from huxley.api import permissions
from huxley.api.serializers import NoteSerializer
from huxley.core.models import Note


class NoteList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, )
    permission_classes = (permissions.NotePermission, )
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.all()
        query_params = self.request.GET
        sender = query_params.get('sender', None)
        recipient = query_params.get('recipient', None)

        committee_id = query_params.get('committee_id', None)
        if committee_id:
            queryset = queryset.filter(sender__committee_id=committee_id) | 
                        queryset.filter(recipient__committee_id=committee_id)


        if sender and recipient:
            queryset = queryset.filter(sender_id = sender).filter(recipient_id = recipient) | 
                        queryset.filter(sender_id = recipient).filter(recipient_id = sender)

                    
        return queryset


class NoteDetail(generics.CreateAPIView, generics.RetrieveAPIView):
    authentication_classes = (SessionAuthentication, )
    queryset = Note.objects.all()
    permission_classes = (permissions.NotePermission, )
    serializer_class = NoteSerializer
