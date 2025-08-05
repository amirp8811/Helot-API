from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        # Get bot ID from environment or use default
        bot_id = os.getenv('BOT_ID', 'your_bot_id_here')
        
        # Generate invite URL with comprehensive permissions
        invite_url = f"https://discord.com/api/oauth2/authorize?client_id={bot_id}&permissions=8&scope=bot%20applications.commands"
        
        response = {
            "invite_url": invite_url,
            "bot_id": bot_id,
            "permissions": [
                "Administrator",
                "Send Messages",
                "Read Messages", 
                "Use Slash Commands",
                "Embed Links",
                "Attach Files",
                "Manage Messages",
                "Manage Channels",
                "Kick Members",
                "Ban Members"
            ]
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