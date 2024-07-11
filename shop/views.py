from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView
from .models import Category, Product, Comment
from .forms import CommentForm
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()


    comments = Comment.objects.filter(product=product)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product  
            new_comment.save()
            return redirect('shop:product_detail', id=id, slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'shop/product/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'comments': comments,
        'comment_form': comment_form,
    })


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'shop/add_comment.html'
    def form_valid(self, form):
        form.instance.product_id = self.kwargs['id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('shop:product_detail', kwargs={'id': self.kwargs['id'], 'slug': self.kwargs['slug']})