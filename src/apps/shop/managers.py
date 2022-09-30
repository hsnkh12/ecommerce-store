from django.db import models

class ProductManager(models.Manager):

    def getBySlug(self, productSlug):
        return self.select_related('category').get(slug= productSlug,show_in_public=True)

    def getByID(self, productID):
        return self.select_related('category').get(id= productID,show_in_public=True)

    def getAll(self):
        return self.select_related('category').all()



class ProductAttributeManager(models.Manager):

    def getByID(self, productAttributeID):
        return self.select_related('product').get(id= productAttributeID,available=True)

    def filterBy(self, filter={}, limit=None):

        queryset = self.select_related('product').filter(**filter,available=True).filter(product__show_in_public=True)
        if limit:
            return queryset[:limit]
        
        return queryset
