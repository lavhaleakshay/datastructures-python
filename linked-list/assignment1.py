import os
import stat
import time
import datetime
import json


#filePath = '/home/corporate-plan/Desktop/hack/ooppython/datastructures-python/linked-list'

def delete_timestamp(timestamp_id, reg):
    print "Deleting timestamp %s " % (timestamp_id)
    try:  
        ec2resource = boto3.resource('ec2', region_name=reg)
        snapshot = ec2resource.Snapshot(snapshot_id)
        snapshot.delete()
    except ClientError as e:
        print "Caught exception: %s" % e
        
    return

count = 0
def main():
    f = open("image.json", "r").read() #Read image.json file
    who = input('Enter creation timestamp: ') #"Enter the creating timestamp string value"
    count = f.count(who) #find out the count of string in image.json file
    print(count) #print creation timestamp count

    a = json.dumps({"creationTimestamp": "2018-06-13T00:10:56.515-07:00"})
    a_dict = json.loads(a)
    for value in a_dict.values():
        print(value)

    now = datetime.now()
    retention_days = 10

    if (now - snapshot_time) > timedelta(retention_days):
        print "Snapshot is older than configured retention of %d days" % (retention_days)
        delete_snapshot(snapshot['SnapshotId'], reg)
    else:
        print "Snapshot is newer than configured retention of %d days so we keep it" % (retention_days) 

	


 

if __name__ == "__main_l_":
    main()

