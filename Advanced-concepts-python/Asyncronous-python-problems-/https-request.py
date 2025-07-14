import requests
import time

start_time=time.time()

for i in range(1,100):
    url="https://pokeapi.co/api/v2/pokemon/1"+str(i)
    resp=requests.get(url)
    pokemon=resp.json()
    print(i,pokemon['name'])

end_time=time.time()
print("Extraction in second",(end_time-start_time))
