import datetime
import logging

import azure.functions as func
import azure.storage.blob as blob
from azure.storage.blob.post_policy import BlobPostPolicy
import azure.cosmosdb.table as table

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    
    # Create and send the email here
    # ...

    cur_time = datetime.datetime.utcnow().replace(
            tzinfo=datetime.timezone.utc).isoformat()
    next_time =  cur_time[:18] + '00:00+00:00' # Every day at 00:00 UTC
    logging.info('Setting next run time for %s', next_time)

    mytimer.wait_for_next_run(next_run_time=datetime.datetime.strptime(next_time, "%Y-%m-%dT%H:%M:%S+00:00"))