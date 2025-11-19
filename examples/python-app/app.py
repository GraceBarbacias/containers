from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

class GDDCalculator(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = '''<!DOCTYPE html>
<html>
<head>
    <title>GDD Calculator</title>
    <style>
        body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; }
        .container { background: #f5f5f5; padding: 20px; border-radius: 8px; }
        input, button { padding: 10px; margin: 5px; width: 100%; box-sizing: border-box; }
        button { background: #4CAF50; color: white; border: none; cursor: pointer; }
        .result { margin-top: 20px; padding: 15px; background: white; border-radius: 5px; }
        label { display: block; margin-top: 10px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>GDD Calculator</h1>
        <form onsubmit="calculate(event)">
            <label>Max Temp (Celsius):</label>
            <input type="number" id="tmax" step="0.1" value="25" required>
            
            <label>Min Temp (Celsius):</label>
            <input type="number" id="tmin" step="0.1" value="15" required>
            
            <label>Base Temp (Celsius):</label>
            <input type="number" id="tbase" step="0.1" value="10" required>
            
            <button type="submit">Calculate</button>
        </form>
        <div id="result" class="result" style="display:none;"></div>
    </div>
    
    <script>
    function calculate(e) {
        e.preventDefault();
        var tmax = document.getElementById('tmax').value;
        var tmin = document.getElementById('tmin').value;
        var tbase = document.getElementById('tbase').value;
        
        // Calculate GDD directly in JavaScript
        var tavg = (parseFloat(tmax) + parseFloat(tmin)) / 2;
        var gdd = Math.max(0, tavg - parseFloat(tbase));
        
        document.getElementById('result').style.display = 'block';
        document.getElementById('result').innerHTML = 
            '<h3>Results:</h3>' +
            '<p><strong>Daily GDD:</strong> ' + gdd.toFixed(2) + ' Celsius-days</p>' +
            '<p><strong>Average Temp:</strong> ' + tavg.toFixed(2) + ' Celsius</p>' +
            '<p><strong>Formula:</strong> (Tmax + Tmin) / 2 - Tbase</p>';
    }
    </script>
</body>
</html>'''
            self.wfile.write(html.encode())
            
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), GDDCalculator)
    print('🌱 GDD Calculator running on http://0.0.0.0:8000/')
    server.serve_forever()