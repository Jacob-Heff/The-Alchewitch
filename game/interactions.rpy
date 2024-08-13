label woods_forage:
    if renpy.get_screen("map"):
        hide screen map
    $ label = "woods_forage"
    scene bg_mist_woods
    show screen hud
    show ghost at ghost_left
    show selene_wicked_grin at selene_bottom_left
    show screen button_screen
    if renpy.get_screen("map"):
        hide screen map
    if renpy.get_screen("time_display"):
        hide screen time_display
        show screen time_display
    else:
        show screen time_display

    "You are foraging in the woods.
    Click to continue..."
    define chance = renpy.random.randint(1, 11)
    if chance == 1:
        "You find a few herbs and mushrooms."
        $ add_to_ingredients("herbs", 3)
        $ add_to_ingredients("mushrooms", 2)
    if chance == 2:
        "You find a few berries and nuts."
        $ add_to_ingredients("berries", 3)
        $ add_to_ingredients("nuts", 2)
    if chance == 3:
        "You find a few herbs and berries."
        $ add_to_ingredients("herbs", 3)
        $ add_to_ingredients("berries", 2)
    if chance == 4:
        "You find a few mushrooms and nuts."
        $ add_to_ingredients("mushrooms", 3)
        $ add_to_ingredients("nuts", 2)
    if chance == 5:
        "You find a few herbs and nuts."
        $ add_to_ingredients("herbs", 3)
        $ add_to_ingredients("nuts", 2)
    if chance == 6:
        "You find a few mushrooms and berries."
        $ add_to_ingredients("mushrooms", 3)
        $ add_to_ingredients("berries", 2)
    if chance == 7:
        "You find a few herbs."
        $ add_to_ingredients("herbs", 5)
    if chance == 8:
        "You find a few mushrooms."
        $ add_to_ingredients("mushrooms", 5)
    if chance == 9:
        "You find a few berries."
        $ add_to_ingredients("berries", 5)
    if chance == 10:
        "You find a few nuts."
        $ add_to_ingredients("nuts", 5)
    if chance == 11:
        "You find nothing."
    call time_advance_and_check
    jump woods

label woods_interact:
    $ label = "woods_interact"
    scene bg_mist_woods
    show screen hud
    show ghost at ghost_left
    show selene_wicked_grin at selene_bottom_left
    if renpy.get_screen("map"):
        hide screen map
    if renpy.get_screen("time_display"):
        hide screen time_display
        show screen time_display
    else:
        show screen time_display
    define chance = renpy.random.randint(1, 2)
    if chance == 1:
        "You are walking through the forest and happen upon a woods nymph."
        show wood nymph at right
    if chance == 2:
        "You are walking through the forest and happen upon a deer."
        show deer at right
    call time_advance_and_check
    jump woods

label woods_combat:
    $ label = "woods_combat"
    scene bg_mist_woods
    show screen hud
    show ghost at ghost_left
    show selene_wicked_grin at selene_bottom_left
    if renpy.get_screen("map"):
        hide screen map
    if renpy.get_screen("time_display"):
        hide screen time_display
        show screen time_display
    else:
        show screen time_display
    define chance = renpy.random.randint(1, 2)
    if chance == 1:
        "You are walking through the forest and happen upon a wolf."
        show wolf at right
    if chance == 2:
        "You are walking through the forest and happen upon a bear."
        show bear at right
    call time_advance_and_check
    jump woods

label mountains_forage:
    $ label = "mountains_forage"
    scene bg_mountains
    show screen hud
    show ghost at ghost_left
    show selene_wicked_grin at selene_bottom_left
    show screen button_screen
    if renpy.get_screen("map"):
        hide screen map
    if renpy.get_screen("time_display"):
        hide screen time_display
        show screen time_display
    else:
        show screen time_display

    "You are foraging in the mountains.
    Click to continue..."
    define chance = renpy.random.randint(1, 11)
    if chance == 1:
        "You find a few herbs and mushrooms."
        $ add_to_ingredients("herbs", 3)
        $ add_to_ingredients("mushrooms", 2)
    if chance == 2:
        "You find a few berries and nuts."
        $ add_to_ingredients("berries", 3)
        $ add_to_ingredients("nuts", 2)
    if chance == 3:
        "You find a few herbs and berries."
        $ add_to_ingredients("herbs", 3)
        $ add_to_ingredients("berries", 2)
    if chance == 4:
        "You find a few mushrooms and nuts."
        $ add_to_ingredients("mushrooms", 3)
        $ add_to_ingredients("nuts", 2)
    if chance == 5:
        "You find a few herbs and nuts."
        $ add_to_ingredients("herbs", 3)
        $ add_to_ingredients("nuts", 2)
    if chance == 6:
        "You find a few mushrooms and berries."
        $ add_to_ingredients("mushrooms", 3)
        $ add_to_ingredients("berries", 2)
    if chance == 7:
        "You find a few herbs."
        $ add_to_ingredients("herbs", 5)
    if chance == 8:
        "You find a few mushrooms."
        $ add_to_ingredients("mushrooms", 5)
    if chance == 9:
        "You find a few berries."
        $ add_to_ingredients("berries", 5)
    if chance == 10:
        "You find a few nuts."
        $ add_to_ingredients("nuts", 5)
    if chance == 11:
        "You find nothing."
    call time_advance_and_check
    jump mountains

label mountains_interact:
    $ label = "mountains_interact"
    scene bg_mountains
    show screen hud
    show ghost at ghost_left
    show selene_wicked_grin at selene_bottom_left
    if renpy.get_screen("map"):
        hide screen map
    if renpy.get_screen("time_display"):
        hide screen time_display
        show screen time_display
    else:
        show screen time_display
    define chance = renpy.random.randint(1, 2)
    if chance == 1:
        "You are walking through the mountains and happen upon a mountain goat."
        show mountain goat at right
    if chance == 2:
        "You are walking through the mountains and happen upon a mountain lion."
        show mountain lion at right
    call time_advance_and_check
    jump mountains

label mountains_combat:
    $ label = "mountains_combat"
    scene bg_mountains
    show screen hud
    show ghost at ghost_left
    show selene_wicked_grin at selene_bottom_left
    if renpy.get_screen("map"):
        hide screen map
    if renpy.get_screen("time_display"):
        hide screen time_display
        show screen time_display
    else:
        show screen time_display
    define chance = renpy.random.randint(1, 2)
    if chance == 1:
        "You are walking through the mountains and happen upon a mountain lion."
        show mountain lion at right
    if chance == 2:
        "You are walking through the mountains and happen upon a mountain goat."
        show mountain goat at right
    call time_advance_and_check
    jump mountains