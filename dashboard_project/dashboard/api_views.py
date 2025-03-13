import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Item

def get_items(request):
    """
    GET /api/items/ - Return all items
    GET /api/items/?search=Item - Filter items using a query parameter
    """
    search_query = request.GET.get('search', '')
    
    if search_query:
        items = Item.objects.filter(name__icontains=search_query)
    else:
        items = Item.objects.all()
    
    items_data = list(items.values('id', 'name', 'description', 'price', 'created_at', 'updated_at'))
    
    return JsonResponse({
        'status': 'success',
        'count': len(items_data),
        'items': items_data
    })

def get_item(request, item_id):
    """
    GET /api/items/<int:item_id>/ - Get a single item
    """
    try:
        item = Item.objects.get(id=item_id)
        item_data = {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': float(item.price),
            'created_at': item.created_at,
            'updated_at': item.updated_at
        }
        return JsonResponse({
            'status': 'success',
            'item': item_data
        })
    except Item.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': f'Item with id {item_id} does not exist'
        }, status=404)

@csrf_exempt
def add_item(request):
    """
    POST /api/items/add/ - Add a new item (JSON or form data)
    """
    if request.method != 'POST':
        return JsonResponse({
            'status': 'error',
            'message': 'Only POST method is allowed'
        }, status=405)
    
    try:
        # Try to parse JSON data
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            # Handle form data
            data = request.POST.dict()
        
        # Validate required fields
        if not data.get('name'):
            return JsonResponse({
                'status': 'error',
                'message': 'Name is required'
            }, status=400)
        
        if not data.get('price'):
            return JsonResponse({
                'status': 'error',
                'message': 'Price is required'
            }, status=400)
        
        # Create new item
        item = Item.objects.create(
            name=data.get('name'),
            description=data.get('description', ''),
            price=data.get('price')
        )
        
        return JsonResponse({
            'status': 'success',
            'message': 'Item created successfully',
            'item': {
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'price': float(item.price),
                'created_at': item.created_at,
                'updated_at': item.updated_at
            }
        }, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@csrf_exempt
def update_item(request, item_id):
    """
    PUT /api/items/update/<int:item_id>/ - Update an item (JSON)
    """
    if request.method != 'PUT':
        return JsonResponse({
            'status': 'error',
            'message': 'Only PUT method is allowed'
        }, status=405)
    
    try:
        item = get_object_or_404(Item, id=item_id)
        
        # Parse JSON data
        data = json.loads(request.body)
        
        # Update fields if provided
        if 'name' in data:
            item.name = data['name']
        
        if 'description' in data:
            item.description = data['description']
        
        if 'price' in data:
            item.price = data['price']
        
        item.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Item updated successfully',
            'item': {
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'price': float(item.price),
                'created_at': item.created_at,
                'updated_at': item.updated_at
            }
        })
    
    except Item.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': f'Item with id {item_id} does not exist'
        }, status=404)
    except json.JSONDecodeError:
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500) 