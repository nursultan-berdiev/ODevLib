from .conf import settings as settings
from .constants import ALL_FIELDS as ALL_FIELDS
from .filters import BaseInFilter as BaseInFilter, BaseRangeFilter as BaseRangeFilter, BooleanFilter as BooleanFilter, CharFilter as CharFilter, ChoiceFilter as ChoiceFilter, DateFilter as DateFilter, DateTimeFilter as DateTimeFilter, DurationFilter as DurationFilter, Filter as Filter, ModelChoiceFilter as ModelChoiceFilter, ModelMultipleChoiceFilter as ModelMultipleChoiceFilter, NumberFilter as NumberFilter, TimeFilter as TimeFilter, UUIDFilter as UUIDFilter
from .utils import get_all_model_fields as get_all_model_fields, get_model_field as get_model_field, resolve_field as resolve_field, try_dbfield as try_dbfield
from _typeshed import Incomplete

def remote_queryset(field): ...

class FilterSetOptions:
    model: Incomplete
    fields: Incomplete
    exclude: Incomplete
    filter_overrides: Incomplete
    form: Incomplete
    def __init__(self, options: Incomplete | None = ...) -> None: ...

class FilterSetMetaclass(type):
    def __new__(cls, name, bases, attrs): ...
    @classmethod
    def get_declared_filters(cls, bases, attrs): ...

FILTER_FOR_DBFIELD_DEFAULTS: Incomplete

class BaseFilterSet:
    FILTER_DEFAULTS: Incomplete
    is_bound: Incomplete
    data: Incomplete
    queryset: Incomplete
    request: Incomplete
    form_prefix: Incomplete
    filters: Incomplete
    def __init__(self, data: Incomplete | None = ..., queryset: Incomplete | None = ..., *, request: Incomplete | None = ..., prefix: Incomplete | None = ...) -> None: ...
    def is_valid(self): ...
    @property
    def errors(self): ...
    def filter_queryset(self, queryset): ...
    @property
    def qs(self): ...
    def get_form_class(self): ...
    @property
    def form(self): ...
    @classmethod
    def get_fields(cls): ...
    @classmethod
    def get_filter_name(cls, field_name, lookup_expr): ...
    @classmethod
    def get_filters(cls): ...
    @classmethod
    def filter_for_field(cls, field, field_name, lookup_expr: Incomplete | None = ...): ...
    @classmethod
    def filter_for_lookup(cls, field, lookup_type): ...

class FilterSet(BaseFilterSet, metaclass=FilterSetMetaclass): ...

def filterset_factory(model, fields=...): ...
