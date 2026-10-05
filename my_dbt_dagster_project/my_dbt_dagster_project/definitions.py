from dagster import Definitions
 
from .schedules import schedules

from .jobs import (

    staging_job,

    dimensions_facts_job,

    marts_job,

)
 
 
defs = Definitions(

    jobs=[

        staging_job,

        dimensions_facts_job,

        marts_job,

    ],

    schedules=schedules,

)
 