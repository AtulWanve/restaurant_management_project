from datetime import datetime

def current_year(requests):
    return {
        'current_year': datetime.now().year
    }
    