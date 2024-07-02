from django.urls import path
from .views import (home, shop, CartView, BookDetailView, ProfileView, EditProfileView, LoginView, RegisterView,
                    User_registerView, Books_dashboardView, LogoutView, CreateView, Books_table, delete_book,
                    delete_cart, UsersView)


urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('detail/<int:book_id>/', BookDetailView.as_view(), name='detail'),
    path('login', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user-register/', User_registerView.as_view(), name='user_register'),
    path('book-dashboard/', Books_dashboardView.as_view(), name='book_dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create-book/', CreateView.as_view(), name='create_book'),
    path('books-table/', Books_table.as_view(), name='books_table'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
    path('delete-cart/<int:book_id>/', delete_cart, name='delete_cart'),
    path('users-table/', UsersView.as_view(), name='users_table'),

]

