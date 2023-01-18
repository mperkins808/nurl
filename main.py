import shlex
import subprocess
import json
import asyncio
async def call_curl(curl):
    args = shlex.split(curl)
    process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return json.loads(stdout.decode('utf-8'))

async def main():
    print("server running x")
    curl = '''curl https://google.com.au'''
    output = await call_curl(curl)
    print(output)

if  __name__ == '__main__':
    asyncio.run(main())
