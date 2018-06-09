from django.shortcuts import render, get_object_or_404
from .models import Account, List, Item


def index(request):
    return render(request, 'accounts/index.html', {'all_accounts': Account.objects.all()})


def account(request, account_id):
    return render(request, 'accounts/account.html', {
        'account': get_object_or_404(Account, id=account_id)
    })


def list(request, account_id, list_id):
    return render(request, 'accounts/list.html', {
        'account': get_object_or_404(Account, id=account_id),
        'list': get_object_or_404(List, id=list_id)
    })


def lists(request, account_id):
    return render(request, 'accounts/lists.html', {
        'account': get_object_or_404(Account, id=account_id),
        'lists': List.objects.filter(account=account_id)})


def item(request, account_id, list_id, item_id):
    return render(request, 'accounts/item.html', {
        'account': get_object_or_404(Account, id=account_id),
        'item': get_object_or_404(Item, id=item_id)
    })


def prioritized(request, account_id, list_id):
    list = get_object_or_404(List, id=list_id)
    try:
        selected_item = list.item_set.get(id=request.POST['item'])
    except (KeyError, Item.DoesNotExist):
        return render(request, 'accounts/list.html', {
            'account': get_object_or_404(Account, id=account_id),
            'list': list,
            'error_message': 'You did not select any valid item'
        })
    else:
        selected_item.is_prioritized = True
        selected_item.save()
        return render(request, 'accounts/list.html', {
            'account': get_object_or_404(Account, id=account_id),
            'list': list
        })
