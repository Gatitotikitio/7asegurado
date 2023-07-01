from django.urls import path
from .views import home, contacto , repuesto , tuning , pago , inicio , registro , agregarProducto , listarProductos , modificarProdutos , eliminarProductos , not404


urlpatterns = [
    path('',home ,name="home"),
    path('app/contacto.html' , contacto , name="contacto"),
    path('app/repuesto.html', repuesto, name="repuesto"),
    path('app/tuning.html', tuning , name="tuning"),
    path('app/pago.html', pago , name="pago"),
    path('app/inicio.html', inicio , name="inicio"),
    path('app/registro.htmk' ,registro , name="registro"),
    path("app/404.html", not404, name="404"),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('listarProductos/', listarProductos, name="listarProductos"),
    path('modificarProductos/<id>/', modificarProdutos, name="modificarProductos"),
    path('eliminarProductos/<id>/', eliminarProductos, name="eliminarProductos"),
]
