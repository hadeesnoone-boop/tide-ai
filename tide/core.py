"""
tide/core.py – The first intelligence layer.
Local. Private. No permission needed.
"""

import subprocess
import json
import sys

class TideCore:
    """Tide's local AI engine – currently wraps Ollama."""
    
    def __init__(self, model="llama2"):
        self.model = model
        self._check_ollama()
    
    def _check_ollama(self):
        """Verify Ollama is installed and running."""
        try:
            result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
            if result.returncode != 0:
                print("⚠️  Ollama not found. Install it: https://ollama.com")
                print("   Then run: ollama pull " + self.model)
                sys.exit(1)
        except FileNotFoundError:
            print("❌ Ollama is not installed.")
            print("   Install from: https://ollama.com")
            print("   Then run: ollama pull " + self.model)
            sys.exit(1)
    
    def ask(self, prompt):
        """Send a prompt to the local model. Returns the response."""
        try:
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True,
                text=True
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Error: {e}"
    
    def chat(self):
        """Interactive chat mode."""
        print(f"\n🌊 Tide Chat (model: {self.model})")
        print("Type 'exit' to end. 'model <name>' to switch models.\n")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("🌊 Tide recedes. See you next wave.")
                break
            if user_input.lower().startswith("model "):
                new_model = user_input.split(" ", 1)[1]
                self.model = new_model
                print(f"✅ Switched to model: {self.model}")
                continue
            
            response = self.ask(user_input)
            print(f"🌊 Tide: {response}\n")
