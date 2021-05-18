from django.urls import path
from .views import api_detail_coruse_view

app_name = 'classroom'

urlpatterns = [
	path('<cid>/', api_detail_coruse_view, name="details"),
	# path('<slug>/update', api_update_blog_view, name="update"),
	# path('<slug>/delete', api_delete_blog_view, name="delete"),
	# path('create', api_create_blog_view, name="create"),
]