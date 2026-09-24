import os
import time
import random
import sys

# A collection of centering thoughts
QUOTES = [
    "You have power over your mind - not outside events. Realize this, and you will find strength. — Marcus Aurelius",
    "Breath is the bridge which connects life to consciousness. — Thich Nhat Hanh",
    "The mind is like water. When it's turbulent, it's difficult to see. When it's calm, everything becomes clear. — Prasad Mahes",
    "Within you, there is a stillness and a sanctuary to which you can retreat at any time. — Hermann Hesse"
]

def clear_screen():
    """Clears the terminal screen for a distraction-free experience."""
    os.system('cls' if os.name == 'nt' else 'clear')

def breathing_cycle():
    """Runs a single 4-4-6 breathing cycle."""
    instructions = [
        ("Inhale...", 4), 
        ("Hold...", 4), 
        ("Exhale...", 6)
    ]
    
    for text, duration in instructions:
        sys.stdout.write(f"\n{text}\n")
        sys.stdout.flush()
        
        # Countdown timer on the same line
        for i in range(duration, 0, -1):
            sys.stdout.write(f"\r{i}  ")
            sys.stdout.flush()
            time.sleep(1)
            
    print("\n")

def main():
    clear_screen()
    print("🌊 Welcome to Calm.")
    print("-" * 40)
    print(random.choice(QUOTES))
    print("-" * 40)
    
    input("\nPress [Enter] when you are ready to find clarity...")
    clear_screen()
    
    print("Let's take a moment to center your mind.")
    print("Follow the breathing prompts.\n")
    time.sleep(2)

    
    try:
        # Run 3 breathing cycles
        for cycle in range(1, 4):
            print(f"--- Cycle {cycle}/3 ---")
            breathing_cycle()
            
        clear_screen()
        print("🌿 You are calm. You are clear. You are ready to continue.")
        print("Press Ctrl+C anytime you need to stop during future sessions.\n")
        
    except KeyboardInterrupt:
        # Graceful exit if the user stops the script early
        clear_screen()
        print("\nSession ended early. Stay clear. 🌿\n")

if __name__ == "__main__":
    main()
