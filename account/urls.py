from django.urls import path, re_path
from account import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.Customerlogin, name='login'),
    path('logout/', views.Customerlogout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    re_path(r'^reset/$',auth_views.PasswordResetView.as_view(
        template_name='account/password_reset.html',
        email_template_name='account/password_reset_email.html',
        subject_template_name='account/password_reset_subject.txt',
        success_url = reverse_lazy('account:password_reset_done')
    ), name='password_reset'),
    re_path(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html',
                                                    success_url = reverse_lazy('account:password_reset_complete')
                                                    ),
        name='password_reset_confirm'),
    re_path(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
        name='password_reset_complete'),
]
