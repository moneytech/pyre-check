# pyre-unsafe

class Manager:
    def aggregate(self, *args, **kwargs): ...
    def all(self): ...
    def create(self, **kwargs): ...
    def filter(self, *args, **kwargs): ...
    def get(self, *args, **kwargs): ...
    def get_or_create(self, defaults=None, **kwargs): ...
    def raw(self, raw_query, params=None, translations=None, using=None): ...
    def bulk_create(self, *args): ...
    def using(self, *args): ...
    def defer(self, *args, **kwargs): ...