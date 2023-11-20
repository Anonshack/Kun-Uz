from django.urls import path
from temp.views import (
    HeadKunUzListView,
    InterMenuListView,
    TodayNewsView,
    UnderKunUzView,
    ThreeNewsKunUzView,

    HeadKunUzDeleteView,
    InternalMenusDelete,
    TodayDeleteView,
    UnderDeleteView,
    ThreeNewsDeleteView,
    ThreeInfoUnderUpdateView,
    UnderInfoUnderUpdateView
)

urlpatterns = [
    path('Head-uz/', HeadKunUzListView.as_view()),
    path('Internal-uz/', InterMenuListView.as_view()),
    path('Today-uz/', TodayNewsView.as_view()),
    path('Under-uz/', UnderKunUzView.as_view()),
    path('ThreeNewsKunUz-uz/', ThreeNewsKunUzView.as_view()),

    path('Delete/<int:pk>/', HeadKunUzDeleteView.as_view(), name='head-uz-delete'),
    path('Internal-delete/<int:pk>/', InternalMenusDelete.as_view(), name='internal-delete'),
    path('Today-delete/<int:pk>/', TodayDeleteView.as_view(), name='today-delete'),
    path('Under-delete/<int:pk>/', UnderDeleteView.as_view(), name='under-delete'),
    path('Three-News-update/<int:pk>/', ThreeInfoUnderUpdateView.as_view(), name='three-Update'),
    path('Three-News-delete/<int:pk>/', ThreeNewsDeleteView.as_view(), name='three-delete'),
    path('Under-update/<int:pk>/', UnderInfoUnderUpdateView.as_view(), name='under-update'),
]