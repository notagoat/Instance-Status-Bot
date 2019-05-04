import psutil, json
from mastodon import Mastodon
from collections import OrderedDict 
mastodon = Mastodon(
    access_token = "",
    api_base_url = "",
)

admin = "" #Your @ Here

def memoryhandler():
  memory = psutil.virtual_memory()

  mpercent = memory[2]

  if mpercent < 80:
    mstatus = 0
  elif mpercent > 80 and mpercent < 90:
    mstatus = 1
  elif mpercent > 90:
    mstatus = 2
  
  message['Memory Usage'] = mpercent
  return mstatus

def diskhandler():
  disk = psutil.disk_usage("/")
  dpercent = disk[3]

  if dpercent < 50:
    dstatus = 0
  elif dpercent > 50 and dpercent < 80:
    dstatus = 1
  elif dpercent > 90:
    dstatus = 2

  message['Disk Usage'] = dpercent
  return dstatus

def nethandler():
  net = psutil.net_connections()
  netstats = len(net)
  message['Active Connections'] = netstats

def processhandler(): 
  processes = psutil.pids()
  processestats = len(processes)
  message['Running Processes'] = processestats

def statushandlers(mstatus,dstatus):
  if mstatus == 0:
    message["Memory Status"] = "Nominal"
  elif mstatus == 1:
    message["Memory Status"] = "High"
  elif mstatus == 2:
    message["Memory Status"] = "Critical!"
    message["Alert!" ] = admin

  if dstatus == 0:
    message["Disk Status"] = "Nominal"
  elif dstatus == 1:
    message["Disk Status"] = "High"
  elif dstatus == 2:
    message["Disk Status"] = "Critical!"
    message["Alert!" ] = admin


def main():
  global message
  message = OrderedDict()
  mstatus = memoryhandler()
  dstatus = diskhandler()
  processhandler()
  nethandler()
  statushandlers(mstatus,dstatus)
  output = ""

  for item,value in message.items():
    output = output + "%s: %s\n" %(item,value)

  mastodon.toot(output)


if __name__ == '__main__':
  main()
