# from rest_framework.permissions import BasePermission
#
#
# class CustomIsAuthenticated(BasePermission):
#     """
#     Allows access only to authenticated users.
#     """
#
#     def has_permission(self, request, view):
#         if request.method == 'GET':
#             return True
#         else:
#             return bool(request.user and request.user.is_authenticated)