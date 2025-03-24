from django.db import models

class Car(models.Model):
    car_id = models.IntegerField(primary_key=True)
    serial_number = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    for_sale_yn = models.BooleanField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Salesperson(models.Model):
    salesperson_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SalesInvoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    invoice_number = models.IntegerField()
    invoice_date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='sales_invoices')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sales_invoices')
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE, related_name='sales_invoices')

    def __str__(self):
        return f"Invoice #{self.invoice_number}"

class ServiceTicket(models.Model):
    service_ticket_id = models.IntegerField(primary_key=True)
    service_ticket_number = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='service_tickets')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='service_tickets')
    date_received = models.DateField()
    comments = models.TextField()
    date_returned = models.DateField()

    def __str__(self):
        return f"Service Ticket #{self.service_ticket_number}"

class Mechanic(models.Model):
    mechanic_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Service(models.Model):
    service_id = models.IntegerField(primary_key=True)
    service_name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.service_name

class ServiceMechanic(models.Model):
    service_mechanic_id = models.IntegerField(primary_key=True)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE, related_name='service_mechanics')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_mechanics')
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE, related_name='service_mechanics')
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"ServiceMech #{self.service_mechanic_id}"

class Part(models.Model):
    part_id = models.IntegerField(primary_key=True)
    part_number = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.part_number

class PartsUsed(models.Model):
    parts_used_id = models.IntegerField(primary_key=True)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE, related_name='parts_used')
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name='parts_used')
    number_used = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"PartsUsed #{self.parts_used_id}"
