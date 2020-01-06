"""hwangsyjung URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from web.views import index
from web.views import pop
from web.views import pop2
from web.views import about
from web.views import goods
from web.views import portfolio
from web.views import portfolio1
from web.views import portfolio2
from web.views import portfolio3
from web.views import portfolio6
from web.views import supports
from web.views import team
from web.views import contact
from web.views import notice
from accounts.views import loginpage, user_login, user_registration
from accounts.views import register


urlpatterns = [
    url(r'^admin/r', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^pop$', pop, name="pop"),
    url(r'^pop2$', pop2, name="pop2"),
    url(r'^about$', about, name="about"),
    url(r'^goods$', goods, name="goods"),
    url(r'^portfolio$', portfolio, name="portfolio"),
    url(r'^portfolio1$', portfolio1, name="portfolio1"),
    url(r'^portfolio2$', portfolio2, name="portfolio2"),
    url(r'^portfolio3$', portfolio3, name="portfolio3"),
    url(r'^portfolio6$', portfolio6, name="portfolio6"),
    url(r'^supports$', supports, name="supports"),
    url(r'^team$', team, name="team"),
    url(r'^contact$', contact, name="contact"),
    url(r'^notice$', notice, name="notice"),
    url(r'^loginpage$', loginpage, name="loginpage"),
    url(r'^user_login$', user_login, name="user_login"),
    url(r'^register$', register, name="register"),
    url(r'^user_registration$', user_registration, name="user_registration"),
]
