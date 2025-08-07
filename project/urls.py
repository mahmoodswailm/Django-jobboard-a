"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),  # Accounts app URLs
    path('admin/', admin.site.urls),
    path('', include('home.urls',namespace='home.urls' )),  # Home page
    path('jobs/',include('job.urls',namespace="jobs")) # ==> (define url name , path to urls file )
]

# Adding static and media URl patterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Adding media URL patterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
]

# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']


# Note: The `urlpatterns` list should be defined only once.
# If you have multiple definitions, they will be overwritten.