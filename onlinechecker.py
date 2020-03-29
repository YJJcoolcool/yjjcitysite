import socket,datetime;
def pingServer():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
  sock.settimeout(2);
  result = sock.connect_ex(('yjjcity.ddns.net',25565));
  if result == 0:
    print('ONLINE');
    htmlfile = open("C:\Program Files\Apache Software Foundation\Apache2.4\htdocs\index.html","r")
    html = htmlfile.read().split("\n")
    for i in range(len(html)):
      test=html[i]
      if test.replace("\t","")[:16]=='<h2 id="yc-ping"':
        html[i]='\t\t\t\t<h2 id="yc-ping" style="color: rgb(255, 255, 255);">YJJ City is ONLINE!</h2>'
      htmlfile = open("C:\Program Files\Apache Software Foundation\Apache2.4\htdocs\index.html","w")
      for i in range(len(html)):
        thing=str(html[i])+"\n"
        htmlfile.write(thing)
      htmlfile.close()
    # online code (I haven't figured this part out yet)
  else:
    print('OFFLINE');
    htmlfile = open("C:\Program Files\Apache Software Foundation\Apache2.4\htdocs\index.html","r")
    html = htmlfile.read().split("\n")
    for i in range(len(html)):
      test=html[i]
      if test.replace("\t","")[:16]=='<h2 id="yc-ping"':
        html[i]='\t\t\t\t<h2 id="yc-ping" style="color: rgb(255, 255, 255);">YJJ City is OFFLINE.</h2>'
      htmlfile = open("C:\Program Files\Apache Software Foundation\Apache2.4\htdocs\index.html","w")
      for i in range(len(html)):
        thing=str(html[i])+"\n"
        htmlfile.write(thing)
      htmlfile.close()
    # offline code (I haven't figured this part out yet)

while True:
  if int(datetime.datetime.now().strftime('%S'))==10:
    pingServer()
  
