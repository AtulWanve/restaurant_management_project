from datetime import datetime

def current_year(request):
    # add current year to all templates
    return {
        'current_year': datetime.now().year
    }
    