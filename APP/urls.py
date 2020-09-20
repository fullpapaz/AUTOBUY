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
    path("blogs", views.ArticleListView.as_view(), name="blog_list"),
    path("blog/<slug>", views.ArticleDetailView.as_view(), name="blog"),
    path("dealer/<slug>", views.DealerDetailView.as_view(), name="dealer"),
    path("submit-listing", views.submit_listing, name="submit_listing"),
    path("contact", views.contact, name="contact"),
    path("featured", views.featured, name="featured"),


]
