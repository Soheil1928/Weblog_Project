from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post-detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('like/<int:pk>', views.like_view, name='like'),
    path('add-post', views.AddPostView.as_view(), name='add_post'),
    path('edit-post/<int:pk>', views.EditPostView.as_view(), name='edit_post'),
    path('delete-post/<int:pk>', views.DeletePostView.as_view(), name='delete_post'),
    path('categories', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<str:cat>', views.category, name='category'),
    path('add-category/', views.AddCategoryView.as_view(), name='add_category'),
    path('post-detail/<int:pk>/comment', views.AddCommentView.as_view(), name='add_comment'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)