
from django.contrib import admin
from django.urls import path
from catalogue.views import home_page, catalogue_page, cap_page, ironman_page, spiderman_page, thor_page
from users.views import login_page, register_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_page),
    path('catalogue/', catalogue_page),
    path("cap/", cap_page),
    path("spiderman/", spiderman_page),
    path("ironman/", ironman_page),
    path("thor/", thor_page),
    path("login/", login_page),
    path("register/", register_page),
]


