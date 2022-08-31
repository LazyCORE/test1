from rest_framework import pagination

class CustomPagination(pagination.LimitOffsetPagination):
    page_size = 2