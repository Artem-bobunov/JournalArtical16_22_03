from django.contrib import admin
from .models import *
from import_export.admin import ExportActionMixin, ImportExportModelAdmin

class RegDataAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    from_encoding = 'utf-8'
    to_encoding = "utf-8"
    list_display = ["oks", "zu", "nameAson_oks", "nameAson_zu"]
    list_filter = ["oks", "zu", "nameAson_oks", "nameAson_zu"]

class ImportExportMixinBase:
    def get_model_info(self):
        app_label = self.model._meta.app_label
        return (app_label, self.model._meta.model_name)

admin.site.register(RegData, RegDataAdmin)
admin.site.register(OtrSquaria_oks)
admin.site.register(DrugoiReg_oks)
admin.site.register(Uslovnye_oks)
admin.site.register(BezKn_oks)
admin.site.register(Enk_oks)
admin.site.register(OtrSquaria_zu)
admin.site.register(DrugoiReg_zu)
admin.site.register(UserName)