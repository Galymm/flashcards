from django.shortcuts import render, get_object_or_404, redirect
from .models import Card, Category
from .forms import CardForm, CategoryForm

def home(request):
    query = request.GET.get('q', '')
    category_name = request.GET.get('category', '')
    subcategory_name = request.GET.get('subcategory', '')

    categories = Category.objects.filter(parent__isnull=True)
    cards = Card.objects.all()

    if query:
        cards = cards.filter(question__icontains=query)

    if category_name:
        cards = cards.filter(category__name=category_name) | cards.filter(category__parent__name=category_name)

    if subcategory_name:
        cards = cards.filter(category__name=subcategory_name)

    return render(request, 'cards/home.html', {
        'cards': cards,
        'categories': categories,
        'selected_category': category_name,
        'selected_subcategory': subcategory_name,
    })


def add_card(request):
    if Category.objects.count() == 0:
        return render(request, 'cards/no_category.html')

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CardForm()

    return render(request, 'cards/add_card.html', {'form': form})


def edit_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CardForm(instance=card)
    return render(request, 'cards/edit_card.html', {'form': form})


def delete_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    card.delete()
    return redirect('home')


def add_category(request, parent_id=None):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        if parent_id:
            parent = Category.objects.get(id=parent_id)
            form = CategoryForm(initial={'parent': parent})
        else:
            form = CategoryForm()
    return render(request, 'cards/add_category.html', {'form': form})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.subcategories.all()
    cards = Card.objects.filter(category=category)
    return render(request, 'cards/category_detail.html', {
        'category': category,
        'subcategories': subcategories,
        'cards': cards,
    })
