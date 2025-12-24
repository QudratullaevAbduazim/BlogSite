from django.urls import path
from .views import (
    IndexView, PortfolioView, PostListView, PostDetailView,
    TagPostsView, CategoryTagPostsView, ContactView,
    LoginView, SignupView, Page404View, PortfolioDetailView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view(), name='portfolio_details'),  # <-- Loyiha ichi uchun

    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('tag/<int:tag_id>/', TagPostsView.as_view(), name='tag_posts'),
    path('category/<int:category_id>/', CategoryTagPostsView.as_view(), name='category_posts'),

    # Sahifalar
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('404/', Page404View.as_view(), name='page_404'),
]