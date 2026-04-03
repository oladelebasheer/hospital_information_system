from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect


def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


def logout_view(request):
    logout(request)
    return redirect('login')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),

    path('', root_redirect, name='root'),

    path('dashboard/', include('reports.urls')),
    path('patients/', include('patients.urls')),
    path('records/', include('records.urls')),
    path('billing/', include('billing.urls')),
]