"""
URL configuration for real_estate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings.views import *
from blog.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Listings,name='listing'),
    path("listing/<pk>/", SingleListing,name='single'),
    path("create_listing/", createListing,name='addlisting'),
    path("listing/<pk>/edit/", UpdateListing,name='update_listing'),
    path("listing/<pk>/delete/", listingDelete,name='deletelisting'),
    path("blog_listing/",blogList, name='blogList'),
    path("blogDetail/<pk>/",blogdetail, name='blogdetail'),
     path("create_blog_listing/", createBlogListing,name='addblog'),
    path("blogDetail/<pk>/edit/", UpdateBLogListing,name='updateblog'),
    path("blogDetail/<pk>/delete/", BlogDelete,name='deleteblog'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
