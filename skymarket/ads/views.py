from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Comment
from ads.paginators import AdPagination, CommentPaginator
from ads.permissions import IsOwnerOrAdmin
from ads.serializers import AdSerializer, CommentSerializer


# AD

class AdCreateAPIView(generics.CreateAPIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_ad = serializer.save()
        new_ad.user = self.request.user
        new_ad.save()


class AdListAPIView(generics.ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ('price', 'user',)
    ordering_fields = ('title',)
    search_fields = ('title',)
    pagination_class = AdPagination


class AdRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]


class AdUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsOwnerOrAdmin, IsAuthenticated]


class AdDestroyAPIView(generics.DestroyAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


# COMMENT

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CommentPaginator
    ordering_fields = ('id', 'user',)

    def get_queryset(self):
        ad_id = self.kwargs['ad_pk']
        return Comment.objects.filter(ad_id=ad_id)

    def perform_create(self, serializer):
        ad_id = self.kwargs['ad_pk']
        ad = Ad.objects.get(pk=ad_id)
        new_comment = serializer.save(ad=ad)
        new_comment.user = self.request.user
        new_comment.save()


class CommentUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class CommentDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]