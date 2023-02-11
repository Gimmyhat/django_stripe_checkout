import stripe
from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.base import TemplateView, View

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'items'


class ItemView(TemplateView):
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['item_id']
        item = get_object_or_404(Item, pk=item_id)
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'item': item,
                'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY
            }
        )
        return context


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['item_id']
        item = get_object_or_404(Item, pk=item_id)
        domain_url = 'http://localhost:8000/'
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': item.price,
                            'product_data': {
                                'name': item.name,
                                'description': item.description,
                            },
                        },
                        'quantity': 1,
                    },
                ],
            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)})


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'
