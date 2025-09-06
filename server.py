#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import os
import sys

# Change to the VideoTube app directory
app_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(app_dir)

PORT = 8081

class VideoTubeHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        # CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def main():
    try:
        with socketserver.TCPServer(("", PORT), VideoTubeHTTPRequestHandler) as httpd:
            print("🎥 WithLove - Advanced Video Platform")
            print("=" * 50)
            print(f"🚀 Server running at: http://localhost:{PORT}")
            print(f"📁 Serving from: {app_dir}")
            print("=" * 50)
            print("Features Available:")
            print("✅ User Authentication (Login/Register)")
            print("✅ Video Upload & Streaming")
            print("✅ Video Player with Controls")
            print("✅ Like/Dislike System")
            print("✅ Comments & Replies")
            print("✅ Subscribe/Unsubscribe")
            print("✅ Notifications")
            print("✅ User Profiles & Channels")
            print("✅ Search Functionality")
            print("✅ Watch History")
            print("✅ Responsive Design")
            print("=" * 50)
            print("Press Ctrl+C to stop the server")
            print("=" * 50)
            
            # Try to open the browser automatically
            try:
                webbrowser.open(f'http://localhost:{PORT}')
                print("🌐 Opening browser automatically...")
            except:
                print("🌐 Please open http://localhost:8080 in your browser")
                
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped gracefully.")
        print("Thank you for using WithLove!")
    except OSError as e:
        if e.errno == 10048:  # Port already in use on Windows
            print(f"❌ Port {PORT} is already in use.")
            print("Please try a different port or stop the other server.")
        else:
            print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main()