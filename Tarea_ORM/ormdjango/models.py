from django.db import models
class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.FloatField(default=0)
    iva = models.BooleanField(default=True)

class Cliente(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True, null=True)
    producto = models.ManyToManyField(Producto)


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField()
    total = models.FloatField(default=0)

class DetalleFactura(models.Model):
    factura=models.ForeignKey(Factura, on_delete= models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)


#                    Ingresar "Producto - Cliente - Factura - Detalle Factura"
#P = Producto(descripcion='Aceite Girazol',precio=1.50,stock=2000)
#P.save()
#Producto.objects.create(descripcion='Coca Cola',precio=0.90,stock=10000)
#icli = Cliente(ruc='0987654536001',nombre='Lucetty',direccion='las piñas')
#icli.save()
#Cliente.objects.create(ruc='1227678375001',nombre='Rosa Martinez',direccion='Vicente Rocafuerte')
#icli.producto.add(1)
#icli2 = Cliente.objects.get(id=2)
#icli2.producto.add(2)
#ifactura = Factura(cliente=icli,fecha='2020-05-28',total=16.78)
#ifactura.save()
#Factura.objects.create(cliente=icli2,fecha='2020-05-30',total=7.88)
#idetfact = DetalleFactura(factura=ifactura,producto=P,cantidad=2,precio=8.39,subtotal=16.78)
#idetfact.save()
#DetalleFactura.objects.create(factura=ifactura,producto=P,cantidad=1,precio=7.88,subtotal=7.88)

#                  Modificar     "Producto - Cliente - Factura - Detalle Factura"
#p = Producto.objects.get(id=1)
#p.precio=1.13
#p.save()
#Producto.objects.filter(id=1).update(precio=1.7)

#modificacliente = Cliente.objects.get(id=1)
#modificacliente.nombre='Lucetty Cruz'
#modificacliente.save()
#Cliente.objects.filter(id=2).update(ruc='13090987654001')

#modififactura= Factura.objects.get(id=1)
#modififactura.total = 33.75
#modififactura.save()
#Factura.objects.filter(id=2).update(fecha='2020-07-22')

#modifidetafa = DetalleFactura.objects.get(id=1)
#modifidetafa.cantidad=3
#modifidetafa.save()
#DetalleFactura.objects.filter(id=2).update(subtotal=9.75)

#Eliminar "Producto - Cliente - Factura - Detalle Factura"
#elimidetafa = DetalleFactura.objects.get(id=1)
#elimidetafa.delete()

#DetalleFactura.objects.filter(id=2).delete()

#elimifactu = Factura.objects.filter(id=1)
#elimifactu.delete()

#Factura.objects.filter(id=2).delete()

#elimicli = Cliente.objects.get(id=1)
#elimicli.delete()

#Cliente.objects.filter(id=2).delete()

#elimipro=Producto.objects.get(id=1)
#elimipro.delete()

#Producto.objects.filter(id=2).delete()



#Query de un Modelo
#p=Producto.objects.all()
#p=Producto.objects.get(id=3)
#Producto.objects.filter(id__lte=3)
#Producto.objects.exclude(descripcion__icontains='Cola')
#Producto.objects.filter(id__gte=4)
#Producto.objects.filter(id__gt=3).values('id','descripcion')
#Producto.objects.filter(id__lt=4).values('id','descripcion')
#Producto.objects.filter(descripcion=‘Coca Cola').values('id','descripcion')





#Query de varios modelos relacionados
#Factura.objects.filter(cliente__nombre='Lucetty')
#c = Cliente.objects.get(nombre='Lucetty')
#c.factura_set.all()
#c.factura_set.filter(id=3)
#Factura.objects.select_related('cliente').filter(cliente__nombre='Lucetty')