import subprocess
import json

class Proxinator:
    def getProxy(address, infura_key):
        result = subprocess.run(
            ["node", "./proxy_detect.js", address, infura_key], 
            capture_output=True, 
            text=True
        )

        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return None

        return json.loads(result.stdout)

### Example Usage
# print(Proxinator.getProxy("0x92274793a65a0de42bb4bf19b393930863877630","skjadb_infura_api_key_aslkdnaslkndasdal"))