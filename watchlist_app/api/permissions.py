from rest_framework import permissions

'''
.has_permission(self, request, view)
hanya perlu check user memilikipermission atau tidak

.has_object_permission(self, request, view, obj)
permission untuk owner, object tertentu hanya bisa di edit oleh sang pembuat
'''
class AdminOrReadOnly(permissions.IsAdminUser):
  def has_permission(self, request, view):
    # return super().has_permission(request, view)
    admin_permission = bool(request.user and request.user.is_staff)
    return request.method == "GET" or admin_permission

class ReviewUserOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    # return super().has_object_permission(request, view, obj)
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD or OPTIONS requests.
    if request.method in permissions.SAFE_METHODS:
        return True

    # Instance must have an attribute named `owner`.
    return obj.review_user == request.user