import sys
import subprocess
import json

iot_hub = 'dhub'
connection_string_format = 'HostName=dhub.azure-devices.net;DeviceId={};SharedAccessKey={}'

def exec(cmd):
    process = subprocess.Popen(cmd,stdout=subprocess.PIPE)
    return json.loads(process.stdout.read().decode())

def dumpkeys(keys):
    print(keys)
    fh = open('keys.txt','w')
    for k in keys:
        fh.write('{}\n'.format(k))
    fh.close()

def createdevices(totalDevices, device_prefix):
    keys = []
    for i in range(totalDevices):
        create_device_cmd = ['az', 'iot', 'hub', 'device-identity', 'create', '-n', iot_hub, '-d', '{}{}'.format(device_prefix, i+1)]
        print('{} executing [{}]'.format(i+1, ' '.join(create_device_cmd)))
        response = exec(create_device_cmd)
        key = response['authentication']['symmetricKey']['primaryKey'] 
        conn_s = connection_string_format.format(response['deviceId'], key)
        keys.append(conn_s)
        print('{} {}\n'.format(i+1, conn_s))

    dumpkeys(keys)

createdevices(500, 'd')

