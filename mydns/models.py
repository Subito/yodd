from django.db import models
from django.conf import settings

class UsingManager(models.Manager):
    def get_query_set(self):
        return super(UsingManager, self).get_query_set().using(settings.DNS_DATABASE)

ACTIVE_CHOICES = (
    ('Y', 'Y'),
    ('N', 'N'),
)

class StartOfAuthority(models.Model):
    origin = models.CharField(max_length=255)
    ns = models.CharField(max_length=255)
    mbox = models.CharField(max_length=255)
    serial = models.PositiveIntegerField()
    refresh = models.PositiveIntegerField()
    retry = models.PositiveIntegerField()
    expire = models.PositiveIntegerField()
    minimum = models.PositiveIntegerField()
    ttl = models.PositiveIntegerField()    
    active = models.CharField(max_length=1, choices=ACTIVE_CHOICES)
    xfer = models.CharField(max_length=255, null=True, blank=True)

    objects = UsingManager()

    def __unicode__(self):
        return self.origin

    class Meta:
        db_table = 'dns_soa'

class RessourceRecord(models.Model):
    TYPE_CHOICES = (
        ('A', 'A'),
        ('AAAA', 'AAAA'),
        ('CNAME', 'CNAME'),
        ('TXT', 'TXT'),
        ('HINFO', 'HINFO'),
        ('MX', 'MX'),
        ('NAPTR', 'NAPTR'),
        ('NS', 'NS'),
        ('PTR', 'PTR'),
        ('RP', 'RP'),
        ('SRV', 'SRV'),
    )

    zone = models.ForeignKey(StartOfAuthority)
    name = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    aux = models.PositiveIntegerField(null=True)
    ttl = models.PositiveIntegerField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    active = models.CharField(max_length=1, choices=ACTIVE_CHOICES)

    objects = UsingManager()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'dns_rr'
