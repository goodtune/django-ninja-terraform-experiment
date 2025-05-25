from django.db import models


class Datacenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Rack(models.Model):
    datacenter = models.ForeignKey(Datacenter, related_name="racks", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name} ({self.datacenter.name})"


class Switch(models.Model):
    rack = models.ForeignKey(Rack, related_name="switches", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return self.name


class Server(models.Model):
    rack = models.ForeignKey(Rack, related_name="servers", on_delete=models.CASCADE)
    connected_switch = models.ForeignKey(
        Switch,
        related_name="connected_servers",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        default="active",
        choices=[
            ("active", "Active"),
            ("maintenance", "Maintenance"),
            ("offline", "Offline"),
        ],
    )

    def __str__(self):
        return self.name
