"""
URL configuration for salvo_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from website.views import home, login, member_dashboard, account_dashboard, register_member, register_account, \
    create_post, verify_post, join_request, view_applications, upvote_application, update_application_status, like_post


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),
    path('member_home/', member_dashboard, name='member_dashboard'),
    path('account_home/', account_dashboard, name='account_dashboard'),
    path('login/', login),
    path('member_signup/', register_member),
    path('account_signup/', register_account),
    path('create_post/', create_post, name='create_post'),
    path('verify_post/<int:post_id>/', verify_post, name='verify_post'),
    path('join_request/<int:reg_no>/', join_request, name='join_request'),
    path('applications/', view_applications, name='view_applications'),
    path('applications/upvote/<int:app_id>/', upvote_application, name='upvote_application'),
    path('applications/<int:app_id>/<str:action>/', update_application_status, name='update_application_status'),
    path('like_post/<int:post_id>/', like_post, name='like_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)