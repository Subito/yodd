from django.contrib import admin
from django.conf import settings

from mydns.models import RessourceRecord, StartOfAuthority

class MultiDBModelAdmin(admin.ModelAdmin):
    using = settings.DNS_DATABASE
    
    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)
        
    def delete_model(self, request, obj):
        obj.delete(using=self.using)
            
    def queryset(self, request):
        return super(MultiDBModelAdmin, self).queryset(request).using(self.using)
                
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        return super(MultiDBModelAdmin, self).formfield_for_foreignkey(db_field, request=request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        return super(MultiDBModelAdmin, self).formfield_for_manytomany(db_field, request=request, using=self.using, **kwargs)

class RessourceRecordAdmin(MultiDBModelAdmin):
    pass

class StartOfAuthorityAdmin(MultiDBAdmin):
    pass

admin.site.register(RessourceRecord, RessourceRecordAdmin)
admin.site.register(StartOfAuthority, StartOfAuthorityAdmin)
