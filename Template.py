import logging
from codecarbon import EmissionsTracker
# Import Other Libraries

# Setup CodeCarbon
## To see Data in the Grafana Dashboard use the save_to_prometheus
## else to see in csv save it in file format 
tracker = EmissionsTracker(
    project_name="GIATHEA_2",
    log_level=logging.INFO,
    output_file="profiler.csv",
    save_to_file=True,
    measure_power_secs=5,
    #save_to_prometheus=True
)


## Define Your Model here


tracker.start()

## Run your model Here

tracker.stop()

