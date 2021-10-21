import jwt
import base64
# middleware.py

class AuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.COOKIES.get('auth_token')

        if not token:
            response = self.get_response(request)
            return response

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except Exception:
            response = self.get_response(request)
            return response

        request.userid = payload['id']
        request.username = payload['name']
        request.country = payload['country']
        
        response = self.get_response(request)
        return response