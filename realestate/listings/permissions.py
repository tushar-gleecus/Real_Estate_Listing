from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAgentOrAdmin(BasePermission):
    """
    Allow only agents or admins to create or update properties.
    Everyone can view.
    """
    def has_permission(self, request, view):
        # Safe methods are GET, HEAD, OPTIONS (read-only)
        if request.method in SAFE_METHODS:
            return True
        # Only allow agents and admins for other methods
        return request.user.is_authenticated and request.user.role in ['agent', 'admin']

class IsBuyerOrAdmin(BasePermission):
    """
    Allow only buyers or admins to POST favorites or inquiries.
    Everyone can view.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role in ['buyer', 'admin']
