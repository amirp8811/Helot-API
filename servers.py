from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        # Mock servers data
        servers = [
            {
                "name": "Gaming Community",
                "member_count": 450,
                "bot_status": True,
                "permissions": "Full"
            },
            {
                "name": "Study Group", 
                "member_count": 120,
                "bot_status": True,
                "permissions": "Basic"
            },
            {
                "name": "Art Club",
                "member_count": 89,
                "bot_status": False,
                "permissions": "None"
            },
            {
                "name": "Music Lovers",
                "member_count": 234,
                "bot_status": True,
                "permissions": "Full"
            },
            {
                "name": "Tech Hub",
                "member_count": 354,
                "bot_status": True,
                "permissions": "Basic"
            }
        ]
        
        response = {
            "servers": servers,
            "total": len(servers),
            "online_servers": len([s for s in servers if s["bot_status"]])
        }
        
        self.wfile.write(json.dumps(response).encode())
        return

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        return 