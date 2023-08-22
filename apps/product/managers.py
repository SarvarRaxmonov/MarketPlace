from django.db import models


class ProductManager(models.Manager):
    def filter_average_rated_products(self, rate_value):
        return self.annotate(average_rate=models.Avg("review_product__rate")).filter(
            average_rate=rate_value
        )

