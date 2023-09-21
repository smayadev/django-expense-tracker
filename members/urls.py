from django.urls import path
from .views import (
    SignUpView, 
    DashboardView, 
    LoginView, 
    ExpenseCategoryView, 
    LogoutView, 
    SupportView,
    TicketView,
    AccountView,
    HomeView
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    #path("privacy", PrivacyPolicyView.as_view(), name="privacy"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("support/", SupportView.as_view(), name="support"),
    path("account/", AccountView.as_view(), name="account"),
    path("ticket/<int:pk>", TicketView.as_view(), name="ticket"),
    path("<slug:slug>/", ExpenseCategoryView.as_view(), name="expense_category"),
]