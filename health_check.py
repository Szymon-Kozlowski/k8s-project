import os
import subprocess
import time

def check_k8s_status():
    print("Checking Kubernetes Pod Health...")
    result = subprocess.run(['kubectl', 'get', 'pods'], capture_output=True, text=True)

    if "Running" in result.stdout:
        print("All pods are operational.")
    else:
        print("Pods are down or starting up.")
        print(result.stdout)

if __name__ == "__main__":
    while True:
        check_k8s_status()
        print("Waiting 10 seconds for next check...")
        time.sleep(1)
