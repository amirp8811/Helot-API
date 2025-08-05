from http.server import BaseHTTPRequestHandler
import json
import os
from datetime import datetime
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        # Mock data for now - replace with actual bot data
        stats = {
            "servers": 5,
            "users": 1247,
            "uptime": "2h 15m 30s",
            "commands": 12,
            "bot_name": "Helot",
            "bot_id": "your_bot_id_here",
            "status": "online"
        }
        
        self.wfile.write(json.dumps(stats).encode())
        return

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        return 