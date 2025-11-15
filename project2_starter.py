"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

import random

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    def __init__(self, name, health, strength, magic):
        # Initialize common attributes shared by all characters
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        # Basic attack method — deals damage equal to character's strength
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        # Calls the target's take_damage() method to apply damage
        target.take_damage(damage)
        
    def take_damage(self, damage):
        # Reduces the character's health by the amount of damage taken
        self.health -= damage
        # Prevents health from dropping below zero
        if self.health < 0:
            self.health = 0
            
        if self.health == 0:
            print("Character Defeated!")
            
    def display_stats(self):
        # Displays the character's current stats
        print(f"{self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")
        

class Player(Character):
    """
    The Player class extends Character.
    It adds level, experience, and character class information.
    """
    
    def __init__(self, name, character_class, health, strength, magic): 
        # Calls the parent constructor to set base stats
        super().__init__(name, health, strength, magic)
        # Adds new player-specific attributes
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        
    def display_stats(self):
        # Calls Character’s display_stats() and adds more info
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | XP: {self.experience}")
        

# ---------------------------------------------------------------------------
# WARRIOR CLASS - inherits from Player
# ---------------------------------------------------------------------------

class Warrior(Player):
    """
    Warrior class — strong in strength but weak in magic.
    Has a special ability called 'power_strike'.
    """
    
    def __init__(self, name):
        # Automatically sets the Warrior's stats
        super().__init__(name, "Warrior", 120, 15, 5)

    def power_strike(self, target):
        """Special warrior ability - powerful attack."""
        # Deals double damage using strength
        damage = self.strength * 2
        print(f"{self.name} uses POWER STRIKE on {target.name} for {damage} damage!")
        target.take_damage(damage)
        

# ---------------------------------------------------------------------------
# MAGE CLASS - inherits from Player
# ---------------------------------------------------------------------------

class Mage(Player):
    """
    Mage class — specializes in magic attacks.
    Has a special ability called 'fireball'.
    """
    
    def __init__(self, name):
        # Sets up Mage-specific stats
        super().__init__(name, "Mage", 80, 8, 20)
        
    def fireball(self, target):
        """Special mage ability - high magic damage attack."""
        # Deals extra magic damage
        damage = self.magic + 10
        print(f"{self.name} casts FIREBALL at {target.name} for {damage} damage!")
        target.take_damage(damage)

# ---------------------------------------------------------------------------
# ROGUE CLASS - inherits from Player
# ---------------------------------------------------------------------------

class Rogue(Player):
    """
    Rogue class — fast and stealthy.
    Has a special ability called 'sneak_attack'.
    """
    
    def __init__(self, name):
        # Sets up Rogue-specific stats
        super().__init__(name, "Rogue", 90, 12, 10)

    def sneak_attack(self, target):
        """Special rogue ability - guaranteed critical hit."""
        # Deals double damage using strength
        damage = self.strength * 2
        print(f"{self.name} performs a SNEAK ATTACK on {target.name} for {damage} damage!")
        target.take_damage(damage)


# ---------------------------------------------------------------------------
# WEAPON CLASS - Demonstrates COMPOSITION
# ---------------------------------------------------------------------------

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        """
        Create a weapon with a name and damage bonus.
        """
        # Store weapon name and damage bonus
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """
        Display information about this weapon.
        """
        # Print weapon name and damage bonus
        print(f"Weapon: {self.name} | Damage Bonus: +{self.damage_bonus}")

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # Test polymorphism
    print("\n⚔️ Testing Polymorphism:")
    dummy = Character("Training Dummy", 100, 0, 0)
    for c in [warrior, mage, rogue]:
        print(f"\n{c.name} attacks the dummy:")
        c.attack(dummy)
        dummy.health = 100  # reset health each time
    
    # Test special abilities
    print("\n✨ Testing Special Abilities:")
    warrior.power_strike(dummy)
    mage.fireball(dummy)
    rogue.sneak_attack(dummy)
    
    # Test weapon composition
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Test battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
