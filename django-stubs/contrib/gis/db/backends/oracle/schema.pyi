from django.db.backends.oracle.schema import DatabaseSchemaEditor
from typing import Any

class OracleGISSchemaEditor(DatabaseSchemaEditor):
    sql_add_geometry_metadata: str = ...
    sql_add_spatial_index: str = ...
    sql_drop_spatial_index: str = ...
    sql_clear_geometry_table_metadata: str = ...
    sql_clear_geometry_field_metadata: str = ...
    geometry_sql: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def geo_quote_name(self, name: Any): ...
    def column_sql(self, model: Any, field: Any, include_default: bool = ...): ...
    def create_model(self, model: Any) -> None: ...
    def delete_model(self, model: Any) -> None: ...
    def add_field(self, model: Any, field: Any) -> None: ...
    def remove_field(self, model: Any, field: Any) -> None: ...
    def run_geometry_sql(self) -> None: ...
