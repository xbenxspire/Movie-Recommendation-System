"""
Movie Recommendation System Starter
---------------------------------
Launches both server and client components.
"""

import subprocess
import sys
import time
import os

def start_system():
    """Start both server and client processes"""
    print("Starting Movie Recommendation System...\n")
    
    # Start server
    print("Step 1: Starting server")
    if sys.platform == 'win32':
        server = subprocess.Popen(['start', 'Movie Server', 'cmd', '/k', 'python server.py'], shell=True)
    else:
        server = subprocess.Popen(['python', 'server.py'], start_new_session=True)
    
    # Wait for server to start
    print("Waiting for server to initialize...")
    time.sleep(5)
    
    # Start client
    print("\nStep 2: Starting client")
    if sys.platform == 'win32':
        client = subprocess.Popen(['start', 'Movie Client', 'cmd', '/k', 'python client.py'], shell=True)
    else:
        client = subprocess.Popen(['python', 'client.py'], start_new_session=True)
    
    print("\nStarted! Use the client window to interact with the system.")
    print("Type 'help' in the client window to see available commands.")

if __name__ == "__main__":
    start_system()
