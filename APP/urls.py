from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "APP"

urlpatterns = [
    path("", views.IndexListView.as_view(), name="index"),
    path("index.html", views.IndexListView.as_view(), name="index"),
    path("car/<slug>", views.CarDetailView.as_view(), name="details"),
    path("search", views.SearchListView.as_view(), name="search"),
    path("cars", views.CategoryListView.as_view(), name="cars"),
    path("submit-listing", views.submit_listing, name="submit_listing"),

]
