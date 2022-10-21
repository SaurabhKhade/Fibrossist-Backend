# API response structure 

def home():
    return {
        'status': 200,
        'message': 'Welcome to the API',
        'data': {
            'routes': [
                {'url': '/validate', 'method': 'POST',
                    'description': 'Validates the whether the given is a valid X-Ray or not'},
                {'url': '/detect', 'method': 'POST',
                    'description': 'Detects whether the patient has Pulmonary Fibrosis or not'},
                {'url': '/signin', 'method': 'POST',
                    'description': 'Signs in the user'},
                {'url': '/signup', 'method': 'POST',
                    'description': 'Signs up the user'},
                {'url': '/log/save', 'method': 'POST',
                    'description': 'Saves the disease detection log of the user'},
                {'url': '/log/retrieve', 'method': 'POST',
                    'description': 'Retrieves the disease detection log of the user'},
            ],
            'Response Format': {
                'status': 'Status Code',
                'message': 'Message related response',
                'data': 'Actual data'
            }
        }
    }, 200
