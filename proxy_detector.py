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
