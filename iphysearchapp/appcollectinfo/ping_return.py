import subprocess
import time

def ping_ip(ip_address):
   
    reply = subprocess.run(['ping',  ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    reply.wait()
    if reply.returncode == 0:
        print(reply.returncode)
        return True, reply.stdout
    else:
        return False, reply.stderr

def ping_ip_ip(host):
  cmd = ['ping', '-c', '1', host]
  start = time.time()
  
  try:
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communicate()[0]
    se = p.communicate()
    print(p)

  except Exception:
    # On error, return 0
    print ("Error running %s" % cmd)
    print ("stderr:\n%s" % se)
    return 0

  else:
    end = time.time()
    return (end-start)*1000