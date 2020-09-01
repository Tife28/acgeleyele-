from django.urls import path
#import from apps
from .views import BlogListView, HomePageView, sermon, ministries, about, bulletin, choir

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('sermon/', sermon, name='sermons'),
    path('ministries/', ministries, name='ministriess'),
    path('about/', about, name='abouts'),
    path('bulletin/', bulletin, name='bulletins'),
    path('choir/', choir, name='choirs'),
]