import socket;
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sock.settimeout(2);
result = sock.connect_ex(('yjjcity.ddns.net',25565));

if result == 0:
  print('ONLINE');
  # online code (I haven't figured this part out yet)
else:
  print('OFFLINE');
  # offline code (I haven't figured this part out yet)
