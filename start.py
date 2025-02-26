"""
Movie Recommendation System Starter
---------------------------------
Launches main program and all microservices as separate processes.
"""

import subprocess
import sys
import time
import os

def start_system():
    """Start main program and all microservices"""
    print("Starting Movie Recommendation System...\n")
    
    # Start server
    print("Step 1: Starting main server")
    if sys.platform == 'win32':
        server = subprocess.Popen(['start', 'Movie Server', 'cmd', '/k', 'python server.py'], shell=True)
    else:
        server = subprocess.Popen(['python', 'server.py'], start_new_session=True)
    
    # Start microservices
    print("\nStep 2: Starting microservices")
    
    # Microservice B - Recommendation Engine
    print("  - Starting Recommendation Engine Service (Microservice B)")
    if sys.platform == 'win32':
        ms_b = subprocess.Popen(['start', 'Microservice B', 'cmd', '/k', 'python microservices/service_b.py'], shell=True)
    else:
        ms_b = subprocess.Popen(['python', 'microservices/service_b.py'], start_new_session=True)
    
    # Microservice C - Genre Analysis
    print("  - Starting Genre Analysis Service (Microservice C)")
    if sys.platform == 'win32':
        ms_c = subprocess.Popen(['start', 'Microservice C', 'cmd', '/k', 'python microservices/service_c.py'], shell=True)
    else:
        ms_c = subprocess.Popen(['python', 'microservices/service_c.py'], start_new_session=True)
    
    # Microservice D - Watch History
    print("  - Starting Watch History Service (Microservice D)")
    if sys.platform == 'win32':
        ms_d = subprocess.Popen(['start', 'Microservice D', 'cmd', '/k', 'python microservices/service_d.py'], shell=True)
    else:
        ms_d = subprocess.Popen(['python', 'microservices/service_d.py'], start_new_session=True)
    
    # Microservice A - Movie Quotes
    print("  - Starting Movie Quotes Service (Microservice A)")
    if sys.platform == 'win32':
        ms_a = subprocess.Popen(['start', 'Microservice A', 'cmd', '/k', 'python microservices/service_a/service.py'], shell=True)
    else:
        ms_a = subprocess.Popen(['python', 'microservices/service_a/service.py'], start_new_session=True)
    
    # Wait for services to start
    print("\nWaiting for services to initialize...")
    time.sleep(5)
    
    # Start client
    print("\nStep 3: Starting client")
    if sys.platform == 'win32':
        client = subprocess.Popen(['start', 'Movie Client', 'cmd', '/k', 'python client.py'], shell=True)
    else:
        client = subprocess.Popen(['python', 'client.py'], start_new_session=True)
    
    print("\nStarted! Use the client window to interact with the system.")
    print("Type 'help' in the client window to see available commands.")
    print("\nAll components are running in separate processes:")
    print("  - Main Server: http://127.0.0.1:8000")
    print("  - Microservice A (Movie Quotes): http://127.0.0.1:5004")
    print("  - Microservice B (Recommendation): http://127.0.0.1:8001")
    print("  - Microservice C (Genre Analysis): http://127.0.0.1:8002")
    print("  - Microservice D (Watch History): http://127.0.0.1:8003")

if __name__ == "__main__":
    start_system()
