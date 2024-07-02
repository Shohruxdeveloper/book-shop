from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Books, Category, Cart, User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, User_registerForm, EditProfileForm, CreateBookForm
from .permissions import AdminRequiredMixin, UserRequiredMixin, SellerRequiredMixin


def home(request):
    context = {
        'books': Books.objects.filter(stock=True),
        'categories': Category.objects.all(),
        'count': Cart.objects.count()
    }
    return render(request, 'shop/index.html', context)


def shop(request):
    context = {
        'books': Books.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'shop/shop.html', context)


class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        cart = Cart.objects.count()
        count = Cart.objects.count()
        return render(request, 'shop/detail.html', context={"book": book, "cart": cart, 'count':count})

    def post(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        quantity = int(request.POST['cart'])
        if Cart.objects.filter(books=book).exists():
            cart = Cart.objects.filter(books=book).first()
            cart.quantity += quantity
            cart.save()
        else:
            cart = Cart()
            cart.books = book
            cart.quantity = quantity
            cart.save()
        return redirect('shop')


class CartView(View):
    def get(self, request):
        books = Cart.objects.all()
        count = Cart.objects.count()
        return render(request, 'shop/cart.html', {'books': books, 'count':count})


class ProfileView(View):
    def get(self, request):
        return render(request, 'shop/profile.html')


class Books_dashboardView(View):
    def get(self, request):
        return render(request, 'shop/dashboard.html')


# class Create_bookView(View):
#     def get(self, request):
#         return render(request, 'shop/create_book.html')


#-----------------------------------------------------------------------------------------------


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'shop/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        form = LoginForm()
        return render(request, 'shop/login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'shop/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return redirect('/')

        form = RegisterForm()
        return render(request, 'shop/register.html', {'form': form})


class EditProfileView(View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)
        return render(request, 'shop/edit_profile.html', {'form': form})

    def post(self, request):
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'shop/edit_profile.html', {'form': form})


class User_registerView(View):

    def get(self, request):
        form = User_registerForm()
        return render(request, 'shop/user_register.html', {'form': form})

    def post(self, request):

        form = User_registerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return redirect('/')

        form = RegisterForm()
        return render(request, 'shop/user_register.html', {'form': form})



class CreateView(View):
    def get(self,request):
        form = CreateBookForm()
        return render(request,'shop/create_book.html',{"form":form})

    def post(self, request):
        form = CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            category_id = form.cleaned_data['category'].id
            category = get_object_or_404(Category, id=category_id)
            book = form.save(commit=False)
            book.category = category
            book.save()
            return redirect('shop')
        form = CreateBookForm()
        return render(request, 'shop/create_book.html', {"form": form})


def delete_cart(request, book_id):
    book = get_object_or_404(Cart, id=book_id)
    book.delete()
    return redirect('shop')


def delete_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    book.delete()
    return redirect('shop')



class Books_table(View):
    def get(self, request):
        books = Books.objects.all()
        return render(request, 'shop/books_table.html', {'books': books})

class UsersView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'shop/admin_table.html', {'users': users})




