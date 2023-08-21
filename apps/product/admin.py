from django.contrib import admin
from apps.product.models import (
    Product,
    Category,
    MainCategory,
    Tag,
    Brand,
    Feature,
    WholeSale,
    Image,
    SavedForLater,
    Review,
)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(MainCategory)
admin.site.register(Tag)
admin.site.register(Brand)
admin.site.register(Feature)
admin.site.register(WholeSale)
admin.site.register(Image)
admin.site.register(SavedForLater)
admin.site.register(Review)
