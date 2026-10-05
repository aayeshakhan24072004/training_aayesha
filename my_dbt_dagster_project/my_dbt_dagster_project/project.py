from pathlib import Path
 
from dagster_dbt import DbtProject
 
 
# Dagster project directory

DAGSTER_PROJECT_DIR = Path(__file__).resolve().parents[1]
 
# Your dbt project

DBT_PROJECT_DIR = Path(

    r"C:\Users\Administrator\Training_Workspace\training"

)
 
# Your standard dbt profiles directory

DBT_PROFILES_DIR = Path(

    r"C:\Users\Administrator\.dbt"

)
 
 
training_project = DbtProject(

    project_dir=DBT_PROJECT_DIR,

    profiles_dir=DBT_PROFILES_DIR,

)
 