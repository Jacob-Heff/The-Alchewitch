rpy monologue none

label brew_potions:
    scene bg alchemist lab with dissolve
    hide screen hud
    hide screen lab_clickable
    show cauldron at cauldron_right
    show selene wicked grin at selene_bottom_left
    show ghost at ghost_left
    nvl clear

    nvlChar'''
    You can brew potions here.
    What potion would you like to brew?"
    '''
    menu(nvl=True):
        "Bottled Aether":
            jump brew_potions
            # jump brew_aether
        "Bottled Affection":
            jump brew_potions
            #jump brew_affection
        "Bottled Cooling":
            jump brew_potions
            #jump brew_cooling
        "Bottled Heating":
            jump brew_potions
            #jump brew_heating
        "Bottled Light":
            jump brew_potions
            #jump brew_light
        "Bottled Shadows":
            jump brew_potions
            #jump brew_shadows
        "Bottled Stone":
            jump brew_potions
            #jump brew_solidifier
        "Bottled Truth":
            jump brew_potions
        "Back":
            jump lab

# label brew_aether:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom, left
#     show cauldron at right

#     nvlChar"""
#     You are brewing the Potion of Aether."
#     You need the following ingredients:"
#     """
#     nvlChar"""
#     1. Bottled Light
#     2. Bottled Shadows
#     3. Bottled Cooling
#     """
#     menu:
#         "Brew Potion of Aether":
#             jump brew_aether_check
#         "Back":
#             jump brew_potions
    
# label brew_aether_check:
#     if light_num >= 1 and shadows_num >= 1 and cooling_num >= 1:
#         jump brew_aether_result
#     else:
#         "You do not have enough ingredients to brew the Potion of Aether."
#         jump brew_potions

# label brew_aether_result:
#     scene bg display
#     show aether at bottle_display

#     call remove_from_inventory("Bottled Light")
#     call remove_from_inventory("Bottled Shadows")
#     call remove_from_inventory("Bottled Cooling")

#     "You have successfully brewed the Potion of Aether."

#     call add_to_inventory("Bottled Aether")

#     jump brew_potions

# label brew_affection:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom
#     show affection at bottle_display

#     "You are brewing the Potion of Affection."

#     "You need the following ingredients:"

#     "1. Bottled Light"
#     "2. Bottled Shadows"
#     "3. Bottled Cooling"

#     menu:
#         "Brew Potion of Affection":
#             jump brew_affection_check
#         "Back":
#             jump brew_potions

# label brew_affection_check:
#     if light_num >= 1 and shadows_num >= 1 and cooling_num >= 1:
#         jump brew_affection_success
#     else:
#         "You do not have enough ingredients to brew the Potion of Affection."
#         jump brew_potions

# label brew_affection_success:
#     scene bg display
#     show affection at bottle_display

#     call remove_from_inventory("Bottled Light")
#     call remove_from_inventory("Bottled Shadows")
#     call remove_from_inventory("Bottled Cooling")
#     "You have successfully brewed the Potion of Affection."
#     call add_to_inventory("Bottled Affection")

#     jump brew_potions

# label brew_cooling:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom
#     show cooling at bottle_display

#     "You are brewing the Potion of Cooling."

#     "You need the following ingredients:"

#     "1. Bottled Light"
#     "2. Bottled Shadows"
#     "3. Bottled Cooling"

#     menu:
#         "Brew Potion of Cooling":
#             jump brew_cooling_checking
#         "Back":
#             jump brew_potions

# label brew_cooling_checking:
#     if light_num >= 1 and shadows_num >= 1 and cooling_num >= 1:
#         jump brew_cooling_success
#     else:
#         "You do not have enough ingredients to brew the Potion of Cooling."
#         jump brew_potions

# label brew_cooling_success:
#     scene bg display
#     show cooling at bottle_display

#     "You have successfully brewed the Potion of Cooling."

#     call remove_from_inventory("Bottled Light")
#     call remove_from_inventory("Bottled Shadows")
#     call remove_from_inventory("Bottled Cooling")

#     call add_to_inventory("Bottled Cooling")

#     jump brew_potions

# label brew_envy:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom
#     show envy at bottle_display

#     "You are brewing the Potion of Envy."

#     "You need the following ingredients:"

#     "1. Bottled Light"
#     "2. Bottled Shadows"
#     "3. Bottled Cooling"

#     menu:
#         "Brew Potion of Envy":
#             jump brew_envy_check
#         "Back":
#             jump brew_potions

# label brew_envy_check:
#     if light_num >= 1 and shadows_num >= 1 and cooling_num >= 1:
#         jump brew_envy_success
#     else:
#         "You do not have enough ingredients to brew the Potion of Envy."
#         jump brew_potions

# label brew_envy_success:
#     scene bg display
#     show envy at bottle_display

#     "You have successfully brewed the Potion of Envy."

#     call add_to_inventory("Bottled Envy")

#     jump brew_potions

# label brew_heating:
#     scene bg display
#     show heating at bottle_display

#     "You are brewing the Potion of Heating."

#     "You need the following ingredients:"

#     "1. Bottled Light"
#     "2. Bottled Shadows"
#     "3. Bottled Cooling"

#     menu:
#         "Brew Potion of Heating":
#             jump brew_heating_success
#         "Back":
#             jump brew_potions

# label brew_heating_success:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom
#     show heating at bottle_display

#     "You have successfully brewed the Potion of Heating."

#     call add_to_inventory("Bottled Heating")

#     jump brew_potions

# label brew_light:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom
#     show light at bottle_display

#     "You are brewing the Potion of Light."

#     "You need the following ingredients:"

#     "1. Bottled Light"
#     "2. Bottled Shadows"
#     "3. Bottled Cooling"

#     menu:
#         "Brew Potion of Light":
#             jump brew_light_success
#         "Back":
#             jump brew_potions

# label brew_light_success:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom
#     show light at bottle_display

#     "You have successfully brewed the Potion of Light."

#     call add_to_inventory("Bottled Light")

#     jump brew_potions

# label brew_shadows:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom
#     show shadows at bottle_display

#     "You are brewing the Potion of Shadows."

#     "You need the following ingredients:"

#     "1. Bottled Light"
#     "2. Bottled Shadows"
#     "3. Bottled Cooling"

#     menu:
#         "Brew Potion of Shadows":
#             jump brew_shadows_success
#         "Back":
#             jump brew_potions

# label brew_shadows_success:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom
#     show shadows at bottle_display

#     "You have successfully brewed the Potion of Shadows."

#     call add_to_inventory("Bottled Shadows")

#     jump brew_potions

# label brew_solidifier:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom
#     show solidifier at bottle_display

#     "You are brewing the Potion of Solidifier."

#     "You need the following ingredients:"

#     "1. Bottled Light"
#     "2. Bottled Shadows"
#     "3. Bottled Cooling"

#     menu:
#         "Brew Potion of Solidifier":
#             jump brew_solidifier_success
#         "Back":
#             jump brew_potions

# label brew_solidifier_success:
#     scene bg alchemist lab with dissolve
#     show selene at selene_bottom
#     show solidifier at bottle_display

#     "You have successfully brewed the Potion of Solidifier."

#     call add_to_inventory("Bottled Solidifier")

#     jump brew_potions