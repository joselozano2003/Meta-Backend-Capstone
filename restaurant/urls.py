from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('', views.home, name="home"),

    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menus/', views.menu, name="menu"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings', views.bookings, name='bookings'),

    # API
    path('menus/', views.MenuItemsView.as_view()),
    path('menus/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]
