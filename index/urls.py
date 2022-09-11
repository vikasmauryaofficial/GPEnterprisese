from django.urls import path
from.import views


urlpatterns = [
path("",views.index,name="hm"),
path("about",views.about,name="ab"),
path("blog_sidebar",views.blog_sidebar,name="blar"),
path("blog_single",views.blog_single,name="blle"),
path("blog",views.blog,name="bl"),
path("contact",views.contact,name="co"),
path("course",views.course,name="course"),
path("course_single",views.course_single,name="cole"),
path("pricing",views.pricing,name="pr"),
path("register",views.register,name="re"),
path("service",views.services,name="se"),
path("trainer",views.trainer,name="tr"),
]