from django.urls import path

from ads.views import AdCreateAPIView, AdListAPIView, AdUpdateAPIView, AdDestroyAPIView, AdRetrieveAPIView, \
    CommentListCreateAPIView, CommentUpdateAPIView, CommentDestroyAPIView

app_name = 'ads'


urlpatterns = [
    path('ads/create/', AdCreateAPIView.as_view(), name='create_ad'),
    path('ads/view/', AdListAPIView.as_view(), name='ads_list'),
    path('ads/view/<int:pk>', AdRetrieveAPIView.as_view(), name='ad_retrieve'),
    path('ads/update/<int:pk>/', AdUpdateAPIView.as_view(), name='ad_update'),
    path('ads/destroy/<int:pk>/', AdDestroyAPIView.as_view(), name='ad_destroy'),

    path('comment/<int:ad_pk>/', CommentListCreateAPIView.as_view(), name='create_ad'),
    path('comment/update/<int:pk>/', CommentUpdateAPIView.as_view(), name='ad_update'),
    path('comment/destroy/<int:pk>/', CommentDestroyAPIView.as_view(), name='ad_destroy'),

]
