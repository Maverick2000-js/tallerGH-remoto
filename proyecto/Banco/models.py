from django.db import models

class Cuenta(models.Model):
    id= models.AutoField(primary_key=True)
    tipocuenta= models.IntegerField()
    descripcion= models.CharField(max_length=200)
    saldo= models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True, default=0)

    class Meta:
        db_table = "cuenta"

    def __str__(self):
        return f"{self.descripcion} - saldo {self.saldo}"
    
