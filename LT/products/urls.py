from django.urls import path, re_path


from django.conf.urls.static import static

from LT import settings
from .views import *

urlpatterns = [
    path('', main_page.as_view(), name='main'),
    path('catalog/', CatalogHome.as_view(), name='home'),
    path('item/<slug:item_slug>/', ShowItem.as_view(), name='item'),
    path('catalog/<slug:cat_slug>/', ShowCatalog.as_view(), name='category'),
    path('about/', about.as_view(), name='about'),
    path('addpage/', AddItem.as_view(), name='add_page'),
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)