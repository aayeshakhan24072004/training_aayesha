from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import training_project


@dbt_assets(manifest=training_project.manifest_path)
def training_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    