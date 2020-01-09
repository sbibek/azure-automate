import sys
import subprocess
import json

iot_hub = 'dhub'

def get_all_devices(hub):
    cmd = ['az', 'iot', 'hub', 'device-identity', 'list','-n',hub]
    process = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    return json.loads(process.stdout.read().decode())


def deleteall(hub):
    devices_list = get_all_devices(hub)
    for device in devices_list:
        d = device['deviceId']
        cmd = ['az', 'iot', 'hub', 'device-identity', 'delete', '-d', d, '-n', hub]
        process = subprocess.Popen(cmd,stdout=subprocess.PIPE)
        print(process.stdout.read().decode())
        print('deleted {}'.format(d))

deleteall(iot_hub)
