from django.db import models
from django.urls import reverse
""" from audit_log.models.fields import LastUserField
from audit_log.models.managers import AuditLog """

# Create your models here.

class Section(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Assettype(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Assetmodel(models.Model):
    assettype = models.ForeignKey(Assettype, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Dutystation(models.Model):
    name = models.CharField("Duty station", max_length=30)

    def __str__(self):
        return self.name

class Holder(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    dutystation = models.ForeignKey(Dutystation, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)

    # audit_log = AuditLog()

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('holder_detail', args=(self.id,))

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

class Purchaseorder(models.Model):
    number = models.PositiveIntegerField(unique=True)
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    date_delivered = models.DateField()

    def __str__(self):
        return str(self.number)

class Asset(models.Model):
    inventorytag = models.CharField("Inventory Tag", max_length=6, unique=True)
    amr = models.PositiveIntegerField("AMR", unique=True)
    assettype = models.ForeignKey(Assettype, on_delete=models.CASCADE)
    assetmodel = models.ForeignKey(Assetmodel, on_delete=models.CASCADE)
    serialnumber = models.CharField("Serial Number", max_length=50, unique=True)
    holder = models.ForeignKey(Holder, on_delete=models.CASCADE)
    po = models.ForeignKey(Purchaseorder, on_delete=models.CASCADE)
    price = models.DecimalField("Price", max_digits=10000, decimal_places=2)

    # audit_log = AuditLog()

    GOOD = 'GOOD'
    DAMAGED = 'DAMAGED'
    OBSOLETE = 'OBSOLETE'
    LOST = 'LOST'
    STATUS_CHOICES = ((GOOD, 'Good'), (DAMAGED, 'Damaged'), (OBSOLETE, 'Obsolete'), (LOST, 'Lost'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='GOOD')

    comment = models.TextField(blank=True)

    NONE = 'NONE'
    MARKED = 'MARKED'
    EXECUTED = 'EXECUTED'
    PSB_STATUS_CHOICES = ((NONE, 'None'), (MARKED, 'Marked'), (EXECUTED, 'Executed'))
    psbstatus = models.CharField(max_length=10, choices=PSB_STATUS_CHOICES, default='NONE')

    def __str__(self):
        return self.assetmodel.name
