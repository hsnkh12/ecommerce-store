from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView, View
import json
from django.http import JsonResponse
from .cart import Cart
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import gettext as _
from .models import ProductAttribute, Product

class IndexView(TemplateView):

    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['products'] = self.get_queryset({}, limit=8)
        return context

    def get_queryset(self, filter={}, limit=None):
        return ProductAttribute.objects.filterBy(filter=filter, limit=limit)


class ProductsListView(ListView):

    template_name = 'shop/products.html'
    paginate_by = 16 
    context_object_name = 'products'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = self.request.get_full_path()
        try:
            page_index = url.index('page')
            context['filterURL'] = url[:page_index] 
        except:
            context['filterURL'] = url + '&' if self.get_filter_and_order()['filter'] else "?"

        return context


    def get_queryset(self):
        filter = self.get_filter_and_order()['filter']
        order = self.get_filter_and_order()['order']

        return ProductAttribute.objects.filterBy(filter).order_by(order)

    def get_filter_and_order(self):

        filter = {}
        order = "product__name"

        for key,value in self.get_query_params().items():
            
            if value != "all" and key != "page":
                
                if key == "order_by":
                    order= value
                else:
                    filter.update({ key : value })


        return {"filter": filter, "order": order}

    def get_query_params(self):
        return dict(self.request.GET.items())



class ProductDetailView(DetailView):

    template_name = 'shop/product.html'

    def get(self, request, *args, **kwargs):

        context = {}
        query_param = self.get_query_param()
        product = self.get_queryset()

        context['main_attribute'] = product.get(id=query_param) if query_param else product.first()
        return self.render_to_response(context)


    def get_queryset(self, **kwargs):
        slug = self.kwargs.get('slug')
        product = Product.objects.getBySlug(slug).attributes_related
        return product

    def get_query_param(self):
        attributeID = self.request.GET.get('attributeID')
        return attributeID if attributeID else None



@method_decorator(csrf_exempt, name='dispatch')
class CartItemsListView(TemplateView):

    template_name = 'shop/cart.html'

    #start order
    def post(self, request):
    
        return redirect('') 

    def delete(self, request):
        
        cart = Cart(self.request)
        cart.removeAll()

        response = {
            'status': 'OK'
        }
        
        return JsonResponse(response,safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CartItemAddRemoveView(View):

    def post(self,request,**kwargs):

        data = json.loads(request.body)
        action = data['action']
        productID = kwargs.get('productID')


        cart = Cart(self.request)

        if action == 'A':
            
            cart.add(productID, data['specificationID'])
        else:
            cart.remove(productID, data['specificationID'])

        response = {
            'productID': productID,
            'status': 'OK'
        }
        
        return JsonResponse(response,safe=False)

    def delete(self, request, **kwargs):

        data = json.loads(request.body)
        productID = kwargs.get('productID')
        cart = Cart(self.request)

        cart.delete(productID, data['specificationID'])

        return JsonResponse({"status":"OK"},safe=False)


