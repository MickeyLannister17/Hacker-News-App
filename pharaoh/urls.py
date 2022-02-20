from django.contrib import admin
from django.urls import path, include
from apps.core.views import signup
from django.contrib.auth import views
from apps.stories.views import frontpage, submit, search, newest, vote, story

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('s<int:story_id>/vote/', vote, name='vote'),
    path('s<int:story_id>/', story, name='story'),
    path('u/', include('apps.userprofile.urls')),
    path('newest/', newest, name='newest'),
    path('search/', search, name='search'),
    path('submit/', submit, name='submit'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('signup/', signup, name="signup"),
    path('admin/', admin.site.urls),
]
