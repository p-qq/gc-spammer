import requests, threading
from discord.ext import commands
client = commands.Bot(command_prefix=".", self_bot= True)
token = "token.YXvmcw.yuh-qvd6bsDfyb4gY"
users = ['811042929040687177','903621585053835275','791835116980666418','903244322181361755'] #users aka the victims
gcs = ['904174831707250750','904174832642568273','904174835285000262','904174878138204240','904174879862042624','904174881200041985','903624652549672980','903624649777233961','904120310272491530'] 
# gc ids ^^^^^ for inviting and kicking out
#t = input("threads: ")
#gc = int(input("gc you wanna fuck them in: "))


def login(): #making it automated i'll finish it up in the future
    data = {}
    
    @client.event
    async def on_ready():
      data['friendsID'] = [freind.id for freind in client.user.friends]
      data['channelsID'] = [channel.id for channel in client.private_channels]
       
      await client.close()
    try:
        client.run(token)
    except Exception as error:
        print(f"Incorrect Token", error)
        return None
    return data

def add(i2):
    for i in users:
        headers = {"Authorization": token}
        r = requests.put(f'https://discordapp.com/api/v6/channels/{i2}/recipients/{i}', headers=headers)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"added {i} to gc {i2}")
        elif r.status_code == 429:
            print(f"ratelimited")
def remove(i2):
    for i in users:
        headers = {"Authorization": token}
        r = requests.delete(f'https://discordapp.com/api/v6/channels/{i2}/recipients/{i}', headers=headers)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"removed {i} from gc {i2}")
        elif r.status_code == 429:
            print(f"ratelimited")
def creategc():
    for i in users:
        headers = {"Authorization": token}
        json = {"recipients":['811042929040687177','903621585053835275','791835116980666418','903244322181361755']}
        r = requests.post('https://discordapp.com/api/v6/users/@me/channels', headers=headers, json=json)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            print(f"created gcs with\n {json}")
        elif r.status_code == 429:
            print(f"ratelimited")
while True:
    try:
        for i2 in gcs:
            threading.Thread(target=remove, args=(i2,)).start()
            threading.Thread(target=add, args=(i2,)).start()
    except:
        print("process couldn't start")
