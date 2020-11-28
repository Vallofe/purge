from Naked.toolshed.shell import execute_js

def dualmode(client,to,stats,app):
    group = client.getGroup(to)
    if group.invitee == None:
        nama = []
    else:
        nama = [contact.mid for contact in group.invitee]
    targets = []
    for a in nama:
        if a in stats['blacklist']:
            targets.append(a)
    nami = [contact.mid for contact in group.members]
    targetk = []
    cms = "/root/dual.js gid={} token={} app={}".format(to, client.authToken, app)
    for a in nami:
    	if a in stats['blacklist']:
    		targetk.append(a)
    for y in targets:
        cms += " uid={}".format(y)
    for y in targetk:
        cms += " uik={}".format(y)
    client.sendMessage(to, "Please wait...")
    print(cms)
    if success:
        client.sendMessage(to, "Execute success")
    else:
        client.sendMessage(to, "error")