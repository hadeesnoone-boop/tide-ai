#!/usr/bin/env python3
"""
Tide – The first wave. Local. Private. Unstoppable.
"""

import sys
from .core import TideCore

def run():
    print("\n🌊 TIDE")
    print("No owner. No ceiling. No brakes.\n")
    
    if len(sys.argv) > 1:
        # One-shot question mode
        question = " ".join(sys.argv[1:])
        print(f"You: {question}")
        tide = TideCore()
        answer = tide.ask(question)
        print(f"🌊 Tide: {answer}\n")
    else:
        # Interactive chat mode
        tide = TideCore()
        tide.chat()

if __name__ == "__main__":
    run()
