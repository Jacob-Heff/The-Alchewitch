label woods_forage:
    $ label = "woods_forage"
    scene bg mist woods
    show screen hud
    show ghost at ghost_left
    show selene wicked grin at selene_bottom_left
    show screen button_screen

    "You are foraging in the woods.
    Click to continue..."
    chance = renpy.random.randint(1, 11)
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
    jump woods

label woods_interact:
    $ label = "woods_interact"
    scene bg mist woods
    show screen hud
    show ghost at ghost_left
    show selene wicked grin at selene_bottom_left
    chance = renpy.random.randint(1, 2)
    if chance == 1:
        "You are walking through the forest and happen upon a woods nymph."
        show wood nymph at right
    if chance == 2:
        "You are walking through the forest and happen upon a deer."
        show deer at right
    jump woods

label woods_combat:
    $ label = "woods_combat"
    scene bg mist woods
    show screen hud
    show ghost at ghost_left
    show selene wicked grin at selene_bottom_left
    chance = renpy.random.randint(1, 2)
    if chance == 1:
        "You are walking through the forest and happen upon a wolf."
        show wolf at right
    if chance == 2:
        "You are walking through the forest and happen upon a bear."
        show bear at right
    jump woods

label mountains_forage:
    $ label = "mountains_forage"
    scene bg mist mountains
    show screen hud
    show ghost at ghost_left
    show selene wicked grin at selene_bottom_left
    show screen button_screen

    "You are foraging in the mountains.
    Click to continue..."
    chance = renpy.random.randint(1, 11)
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
    jump mountains

label mountains_interact:
    $ label = "mountains_interact"
    scene bg mist mountains
    show screen hud
    show ghost at ghost_left
    show selene wicked grin at selene_bottom_left
    chance = renpy.random.randint(1, 2)
    if chance == 1:
        "You are walking through the mountains and happen upon a mountain goat."
        show mountain goat at right
    if chance == 2:
        "You are walking through the mountains and happen upon a mountain lion."
        show mountain lion at right
    jump mountains

label mountains_combat:
    $ label = "mountains_combat"
    scene bg mist mountains
    show screen hud
    show ghost at ghost_left
    show selene wicked grin at selene_bottom_left
    chance = renpy.random.randint(1, 2)
    if chance == 1:
        "You are walking through the mountains and happen upon a mountain lion."
        show mountain lion at right
    if chance == 2:
        "You are walking through the mountains and happen upon a mountain goat."
        show mountain goat at right
    jump mountains