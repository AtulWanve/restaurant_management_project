from datetime import datetime

def current_year(request):
    # add current year to all templates
    return {
        'current_year': datetime.now().year
    }
    
def restaurant_info(request):
    return {
        'restaurant_name': 'My Restaurant',
        'restaurant_phone': '+91-9876543210',
        'restaurant_adress': '123 MG Road, Bangaluru, Karnatake, India',
    }