from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'libuser', views.LibuserViewSet)
router.register(r'rentbook', views.RentBookViewSet)
