
class PermissionManager:

    def check(self, request):

        return {
            "request": request,
            "permission": "GRANTED"
        }
