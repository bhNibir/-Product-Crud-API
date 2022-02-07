
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import CategoryViewSet, ProductViewSet,  CategoryList, ProductList, ProductRetrieveAPIView, ProductsListByCategory

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
    path('crud/', include(router.urls)),
    path('categories/', CategoryList.as_view()),
    path('products/', ProductList.as_view()),

    path('category/<int:category_id>/', ProductsListByCategory.as_view()),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view()),
    path('search/', ProductList.as_view()),

]