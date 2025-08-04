import time
import sys
import random

class TemporalExplorer:
    def __init__(self):
        # Initialize player's inventory and game state
        self.inventory = []
        self.current_time = "present"
        self.game_over = False
        self.time_periods = {
            "present": "Research Lab (2025)",
            "ancient": "Ancient Egypt (2500 BCE)",
            "renaissance": "Renaissance Italy (1500)",
            "future": "Neo Tokyo (2250)"
        }
        
    def print_slow(self, text):
        """Print text with a typewriter effect"""
        try:
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
            print()
        except KeyboardInterrupt:
            print("\nText display interrupted.")

    def clear_screen(self):
        """Clear the console screen"""
        print("\n" * 50)

    def show_inventory(self):
        """Display the player's inventory"""
        if not self.inventory:
            self.print_slow("\nYour inventory is empty.")
        else:
            self.print_slow("\nInventory:")
            for item in self.inventory:
                self.print_slow(f"- {item}")

    def get_valid_input(self, options):
        """Get and validate user input"""
        while True:
            try:
                choice = input("\nWhat would you like to do? ").lower().strip()
                if choice in options:
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except KeyboardInterrupt:
                self.print_slow("\nGame paused. Press Enter to continue or type 'quit' to exit.")
                try:
                    response = input().lower().strip()
                    if response == 'quit':
                        self.game_over = True
                        return 'quit'
                except:
                    continue

    def present_scene(self):
        """Handle the present-day research lab scene"""
        self.print_slow("\nYou're in your research lab. The time machine is ready.")
        self.print_slow("Where would you like to travel?")
        
        options = ["ancient", "renaissance", "future", "inventory", "quit"]
        self.print_slow("\nOptions: ancient, renaissance, future, inventory, quit")
        
        choice = self.get_valid_input(options)
        
        if choice == "inventory":
            self.show_inventory()
            return self.present_scene()
        elif choice == "quit":
            self.game_over = True
        else:
            self.current_time = choice
            return choice

    def ancient_scene(self):
        """Handle the Ancient Egypt scene"""
        self.print_slow("\nYou materialize in Ancient Egypt.")
        self.print_slow("You see a mysterious hieroglyph and a golden scarab.")
        
        if "scarab" not in self.inventory:
            options = ["take scarab", "examine hieroglyph", "return", "inventory", "quit"]
            self.print_slow("\nOptions: take scarab, examine hieroglyph, return, inventory, quit")
        else:
            options = ["examine hieroglyph", "return", "inventory", "quit"]
            self.print_slow("\nOptions: examine hieroglyph, return, inventory, quit")
        
        choice = self.get_valid_input(options)
        
        if choice == "take scarab":
            self.inventory.append("scarab")
            self.print_slow("You picked up the golden scarab.")
        elif choice == "examine hieroglyph":
            self.print_slow("The hieroglyph shows a warning about temporal anomalies.")
        elif choice == "inventory":
            self.show_inventory()
        elif choice == "return":
            self.current_time = "present"
        elif choice == "quit":
            self.game_over = True
            
        return self.current_time

    def renaissance_scene(self):
        """Handle the Renaissance scene"""
        self.print_slow("\nYou arrive in Renaissance Italy.")
        self.print_slow("You're in an artist's workshop with various tools and sketches.")
        
        options = ["examine sketches", "return", "inventory", "quit"]
        self.print_slow("\nOptions: examine sketches, return, inventory, quit")
        
        choice = self.get_valid_input(options)
        
        if choice == "examine sketches":
            if "scarab" in self.inventory:
                self.print_slow("You notice the scarab symbol in one of the sketches!")
            else:
                self.print_slow("The sketches show various mechanical inventions.")
        elif choice == "inventory":
            self.show_inventory()
        elif choice == "return":
            self.current_time = "present"
        elif choice == "quit":
            self.game_over = True
            
        return self.current_time

    def future_scene(self):
        """Handle the Future scene"""
        self.print_slow("\nYou emerge in Neo Tokyo, 2250.")
        self.print_slow("Holographic displays float in the air around you.")
        
        options = ["check displays", "return", "inventory", "quit"]
        self.print_slow("\nOptions: check displays, return, inventory, quit")
        
        choice = self.get_valid_input(options)
        
        if choice == "check displays":
            if "scarab" in self.inventory:
                self.print_slow("The displays show that the scarab is a key to preventing a temporal disaster!")
            else:
                self.print_slow("The displays show various timeline anomalies.")
        elif choice == "inventory":
            self.show_inventory()
        elif choice == "return":
            self.current_time = "present"
        elif choice == "quit":
            self.game_over = True
            
        return self.current_time

    def play_game(self):
        """Main game loop"""
        self.clear_screen()
        self.print_slow("Welcome to Temporal Explorer!")
        self.print_slow("You are a time traveler tasked with preventing temporal anomalies.")
        self.print_slow("Explore different time periods and solve the mystery!")
        
        while not self.game_over:
            try:
                if self.current_time == "present":
                    self.present_scene()
                elif self.current_time == "ancient":
                    self.ancient_scene()
                elif self.current_time == "renaissance":
                    self.renaissance_scene()
                elif self.current_time == "future":
                    self.future_scene()
                    
                if "scarab" in self.inventory and self.current_time == "present":
                    self.print_slow("\nCongratulations! You've solved the temporal mystery!")
                    self.print_slow("The scarab was the key to stabilizing the timeline.")
                    self.game_over = True
                    
            except Exception as e:
                self.print_slow(f"\nAn error occurred: {str(e)}")
                self.print_slow("The game will continue from your last valid position.")
                continue

        self.print_slow("\nThank you for playing Temporal Explorer!")

# Start the game
if __name__ == "__main__":
    game = TemporalExplorer()
    game.play_game()