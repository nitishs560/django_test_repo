import os

def readlogs():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'logs/honeypot-iplist.log')  # full path to text.
    fp = open(file_path, 'r')
    biplist = []
    while True:
        line = fp.readline()
        if not line:
            break
        biplist.append(line.strip())

    fp.close()
    datalist=[]

    for ipstr in biplist:
        if ipstr!='':
            data=[]
            ipstr=ipstr.split(" ")
            if len(ipstr) == 8:
                data.append(ipstr[0]+ipstr[1])
                ip=ipstr[-1].split("\t")
                data.append(ip[0])
                data.append(ip[1])
                datalist.append(data)
    print(datalist)
    return datalist

def readunplogs():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'logs/honeypot-usernames-and-passwords.log')  # full path to text.
    fp = open(file_path, 'r')  # I used'rb' here since I got an 'gbk' decode error

    uplist = []
    while True:
        line = fp.readline()
        if not line:
            break
        uplist.append(line.strip())
    print(uplist)
    print(uplist[0].split(' '))
    fp.close()
    datalist=[]
    for user in uplist:
      unp=user.split(' ')
      data=[]
      if len(unp)==8:
          data.append(unp[0]+unp[1])
          usp=unp[-1][unp[-1].find(':')+1:]
          usp=usp.split("\t")
          print(usp)
          if len(usp)==2:
              data.append(usp[0])
              data.append(usp[1])
              datalist.append(data)
    return datalist

