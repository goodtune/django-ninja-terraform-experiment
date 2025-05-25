from django.contrib import admin

from manifest.models import Datacenter, Rack, Server, Switch


class RackInline(admin.TabularInline):
    model = Rack
    extra = 0


class SwitchInline(admin.TabularInline):
    model = Switch
    extra = 0


class ServerByRackInline(admin.TabularInline):
    model = Server
    fk_name = "rack"
    extra = 0


class ServerBySwitchInline(admin.TabularInline):
    model = Server
    fk_name = "connected_switch"
    extra = 0


class DatacenterAdmin(admin.ModelAdmin):
    inlines = [RackInline]
    list_display = ("name", "location")


class RackAdmin(admin.ModelAdmin):
    inlines = [SwitchInline, ServerByRackInline]


class SwitchAdmin(admin.ModelAdmin):
    inlines = [ServerBySwitchInline]


admin.site.register(Datacenter, DatacenterAdmin)
admin.site.register(Rack, RackAdmin)
admin.site.register(Switch, SwitchAdmin)
admin.site.register(Server)
