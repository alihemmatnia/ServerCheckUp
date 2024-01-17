from python_on_whales import DockerClient
from requests import get
from time import sleep
from datetime import datetime
base_url = "https://limoonline.ir:9091/Home/vitrin?page=1&limit=1"
docker = DockerClient(compose_files=["./docker-compose.yml"])

def compose_up(date_time):
    print(f"docker compose started - {date_time}")
    docker.compose.up(force_recreate=True, quiet=True,detach=True)
    print("docker compose done")

while True:
    date_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    try:
        req = get(base_url)
        print(f"send request - code: {req.status_code} - time: {date_time}")
        if not req.ok or req.status_code != 200:
            compose_up(date_time)
            sleep(6)
            continue
        sleep(0.7)
    except:
        compose_up(date_time)
        sleep(6)
        continue
