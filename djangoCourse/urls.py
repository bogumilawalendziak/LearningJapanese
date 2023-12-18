from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.wordview import WordViewSet
from api.historyview import HistoryViewSet

router = routers.DefaultRouter()
router.register(r'word', WordViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("admin/", admin.site.urls),
    path('api/getByWord?<str:word>/', WordViewSet.as_view({'get': "get_by_word"}), name='get-by-word'),
    path('api/getSingleWord/', WordViewSet.as_view({'get': "get_single_word"}), name='get-single-word'),
    path('api/word/', HistoryViewSet.as_view({'post': "create"}), name='create'),
    path('api/word/createList', HistoryViewSet.as_view({'post': "createList"}), name='create')

]
