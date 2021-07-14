from django.urls import path
from .views import (JobListView, JobSearchView, MainPageSearch, PrivacyPolicyView, TermsOfService,
                    read_file)

app_name = 'job_search'
urlpatterns = [
    # path('', JobListView.as_view(), name='job-list'),
    # path('', JobSearchView, name='search-list'),
    path('', MainPageSearch, name='main-page'),
    path('privacy/', PrivacyPolicyView, name='privacy-page'),
    path('terms/', TermsOfService, name='terms-page'),
    path('data.geojson/', read_file, name='json-file'),
    # path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-create'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]