import json
import urllib.request
import os

def call_mcp(tool_name, arguments={}):
    with open('.appdeploy', 'r') as f:
        config = json.load(f)
    
    api_key = config['api_key']
    endpoint = config['endpoint']
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }
    
    req = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode('utf-8'),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "Authorization": f"Bearer {api_key}"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as res:
            response = json.loads(res.read().decode('utf-8'))
            return response
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        print(e.read().decode('utf-8'))
        return None

if __name__ == "__main__":
    import sys
    tool = sys.argv[1] if len(sys.argv) > 1 else 'get_deploy_instructions'
    args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    res = call_mcp(tool, args)
    with open('mcp_response.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, indent=2)
    print("Wrote response to mcp_response.json")
