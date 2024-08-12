rpy monologue none

default ingredients_list = []
default potions_list = []

init python:
    def add_to_ingredients(item, amount):
        x=0
        while True:
            x += 1
            ingredients_list.append(item)
            if x == amount:
                break

default hud_display = ""

default label = ""

default hud_should_be_modal = True

default trouble = False

define cauldron = "images/lab/cauldron.png"
image aether = "images/display/Bottled Aether.png"
image affection = "images/display/Bottled Affection.png"
image cooling = "images/display/Bottled Cooling.png"
image heating = "images/display/Bottled Heating.png"
image light = "images/display/Bottled Light.png"
image shadows = "images/display/Bottled Shadows.png"
image stone = "images/display/Bottled Stone.png"
image truth = "images/display/Bottled Truth.png"

screen hud:
    tag persistent

    modal False

    frame:
        background "#1a1a1ab1"
        xalign 0.5
        yalign 0.0
        grid 3 1:
            imagebutton:
                idle "images/hud/icons/Icon Ingredients Menu.png"
                hover "images/hud/icons/Icon Ingredients Menu.png"
                action SetVariable("hud_display", "ingredients"), Show("hud")
                tooltip "Ingredients"
            imagebutton:
                idle "images/hud/icons/Icon Map Menu.png"
                hover "images/hud/icons/Icon Map Menu.png"
                action Jump("map")
                tooltip "Map"
            imagebutton:
                idle "images/hud/icons/Icon Potion Menu.png"
                hover "images/hud/icons/Icon Potion Menu.png"
                action SetVariable("hud_display", "potions"), Show("hud")
                tooltip "Potions"
    
    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                text tooltip
    
    # if hud_display == "ingredients":
    #     frame:
    #         background "#1a1a1ab1"
    #         xalign 0.0
    #         yalign 0.25
    #         xsize 250
    #         ysize 500
    #         grid 1 2:
    #             grid 1 4:
    #                 textbutton "   X   " action SetVariable("hud_display", ""), Show("hud")
    #                 imagebutton:
    #                     idle "images/hud/icons/Icon Ingredients Menu.png"
    #                     hover "images/hud/icons/Icon Ingredients Menu.png"
    #                     action NullAction()
    #                 imagebutton:
    #                     idle "images/hud/icons/Icon Map Menu.png"
    #                     hover "images/hud/icons/Icon Map Menu.png"
    #                     action NullAction()
    #                 imagebutton:
    #                     idle "images/hud/icons/Icon Potion Menu.png"
    #                     hover "images/hud/icons/Icon Potion Menu.png"
    #                     action NullAction()

    if hud_display == "potions":
        frame:
            background "#1a1a1ab1"
            xalign 0.0
            yalign 0.25
            xsize 340
            ysize 500
            grid 2 5:
                textbutton "   X   " action SetVariable("hud_display", ""), Show("hud")
                text ""
                if "aether" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Aether.png"
                            hover "images/hud/potions/empty/Bottled Aether.png"
                            action NullAction()
                        text "Bottled Aether | 0":
                            size 16
                if "affection" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Affection.png"
                            hover "images/hud/potions/empty/Bottled Affection.png"
                            action NullAction()
                        text "Bottled Affection | 0":
                            size 16
                if "cooling" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Cooling.png"
                            hover "images/hud/potions/empty/Bottled Cooling.png"
                            action NullAction()
                        text "Bottled Cooling | 0":
                            size 16
                if "heating" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Heating.png"
                            hover "images/hud/potions/empty/Bottled Heating.png"
                            action NullAction()
                        text "Bottled Heating | 0":
                            size 16
                if "light" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Light.png"
                            hover "images/hud/potions/empty/Bottled Light.png"
                            action NullAction()
                        text "Bottled Light | 0":
                            size 16
                if "shadows" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Shadows.png"
                            hover "images/hud/potions/empty/Bottled Shadows.png"
                            action NullAction()
                        text "Bottled Shadows | 0":
                            size 16
                if "stone" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Stone.png"
                            hover "images/hud/potions/empty/Bottled Stone.png"
                            action NullAction()
                        text "Bottled Stone | 0":
                            size 16
                if "truth" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Truth.png"
                            hover "images/hud/potions/empty/Bottled Truth.png"
                            action NullAction()
                        text "Bottled Truth | 0":
                            size 16


screen hud_modal:
    tag persistent

    modal True

    frame:
        background "#1a1a1ab1"
        xalign 0.5
        yalign 0.0
        grid 3 1:
            imagebutton:
                idle "images/hud/icons/Icon Ingredients Menu.png"
                hover "images/hud/icons/Icon Ingredients Menu.png"
                action SetVariable("hud_display", "ingredients"), Show("hud")
                tooltip "Ingredients"
            imagebutton:
                idle "images/hud/icons/Icon Map Menu.png"
                hover "images/hud/icons/Icon Map Menu.png"
                action Jump("map")
                tooltip "Map"
            imagebutton:
                idle "images/hud/icons/Icon Potion Menu.png"
                hover "images/hud/icons/Icon Potion Menu.png"
                action SetVariable("hud_display", "potions"), Show("hud")
                tooltip "Potions"
    
    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                text tooltip
    
    # if hud_display == "ingredients":
    #     frame:
    #         background "#1a1a1ab1"
    #         xalign 0.0
    #         yalign 0.25
    #         xsize 250
    #         ysize 500
    #         grid 1 2:
    #             grid 1 4:
    #                 textbutton "   X   " action SetVariable("hud_display", ""), Show("hud")
    #                 imagebutton:
    #                     idle "images/hud/icons/Icon Ingredients Menu.png"
    #                     hover "images/hud/icons/Icon Ingredients Menu.png"
    #                     action NullAction()
    #                 imagebutton:
    #                     idle "images/hud/icons/Icon Map Menu.png"
    #                     hover "images/hud/icons/Icon Map Menu.png"
    #                     action NullAction()
    #                 imagebutton:
    #                     idle "images/hud/icons/Icon Potion Menu.png"
    #                     hover "images/hud/icons/Icon Potion Menu.png"
    #                     action NullAction()

    if hud_display == "potions":
        frame:
            background "#1a1a1ab1"
            xalign 0.0
            yalign 0.25
            xsize 340
            ysize 500
            grid 2 5:
                textbutton "   X   " action SetVariable("hud_display", ""), Show("hud")
                text ""
                if "aether" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Aether.png"
                            hover "images/hud/potions/empty/Bottled Aether.png"
                            action NullAction()
                        text "Bottled Aether | 0":
                            size 16
                if "affection" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Affection.png"
                            hover "images/hud/potions/empty/Bottled Affection.png"
                            action NullAction()
                        text "Bottled Affection | 0":
                            size 16
                if "cooling" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Cooling.png"
                            hover "images/hud/potions/empty/Bottled Cooling.png"
                            action NullAction()
                        text "Bottled Cooling | 0":
                            size 16
                if "heating" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Heating.png"
                            hover "images/hud/potions/empty/Bottled Heating.png"
                            action NullAction()
                        text "Bottled Heating | 0":
                            size 16
                if "light" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Light.png"
                            hover "images/hud/potions/empty/Bottled Light.png"
                            action NullAction()
                        text "Bottled Light | 0":
                            size 16
                if "shadows" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Shadows.png"
                            hover "images/hud/potions/empty/Bottled Shadows.png"
                            action NullAction()
                        text "Bottled Shadows | 0":
                            size 16
                if "stone" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Stone.png"
                            hover "images/hud/potions/empty/Bottled Stone.png"
                            action NullAction()
                        text "Bottled Stone | 0":
                            size 16
                if "truth" in potions_list:
                    pass
                else:
                    grid 1 2:
                        imagebutton:
                            idle "images/hud/potions/empty/Bottled Truth.png"
                            hover "images/hud/potions/empty/Bottled Truth.png"
                            action NullAction()
                        text "Bottled Truth | 0":
                            size 16

screen lab_clickable:
    imagebutton at cauldron_right:
        idle cauldron
        hover cauldron
        action Jump("brew_potions")
        tooltip "Brew Potions"
    
    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                text tooltip
    

label start:
    scene bg alchemist lab with dissolve
    show selene wicked grin at selene_bottom_left
    show cauldron at cauldron_right
    show ghost at ghost_left

    """
    You are Selene, THE Alchewitch.
    You are not like any other witch.
    You have the power to manipulate the elements.
    You can bottle them up and use them to your advantage.
    """

    scene bg forest
    """
    The world you live in is in chaos.
    A force of darkness is taking over the land.
    You must use your powers to stop it.
    """
    jump potion_intro

label potion_intro:
    scene bg alchemist lab with dissolve
    """
    You have nine potions at your disposal.
    Each potion has a unique property that can help you in your quest.
    """
    """
    Choose wisely and brew the potions you need.
    The fate of the world is in your hands.
    """

    scene bg display with dissolve
    show aether at bottle_display
    """
    The Potion of Aether:
    Changes the properties of other elements
    Crafted with ___, ___ and ____.
    Use: Throw at an enemy or oject to change or weaken an element within it
    """
    hide aether
    
    show affection at bottle_display
    """
    The Potion of Affection, AKA The Love Potion:
    Makes people fall in love with the first person they see
    Crafted with ___, ___ and ____.
    Use: Target must drink the potion, can be poured and mixed with other drinks
    """
    hide affection
    
    show cooling at bottle_display
    """
    The Potion of Cooling:
    Freezes things and people in place
    Crafted with ___, ___ and ____.
    Use: Throw at an enemy or object to freeze it in place
    """
    hide cooling

    show heating at bottle_display
    """
    The Potion of Heating:
    Burns things and people
    Crafted with 2 sticks and a stone.
    Use: Throw at an enemy or object to burn it
    """
    hide heating

    show light at bottle_display
    """
    The Potion of Light:
    Illuminates dark places
    Crafted with ___, ___ and ____.
    Use: Throw at a dark place to illuminate it
    """
    hide light

    show shadows at bottle_display
    """
    The Potion of Shadows:
    Creates darkness
    Crafted with ___, ___ and ____.
    Use: Throw at a lit place to create darkness
    """
    hide shadows

    show stone at bottle_display
    """
    The Potion of Stone:
    Turns an object or enemy into stone
    Crafted with ___, ___ and ____.
    Use: Throw at an enemy or object to turn it into stone
    """
    hide stone

    show truth at bottle_display
    """The Potion of Truth:
    Makes people tell the truth
    Crafted with ___, ___ and ____.
    Use: Target must drink the potion, can be poured and mixed with other drinks
    """
    hide truth

    jump lab

label lab:
    $ _skipping = False
    $ label = "lab"
    scene bg alchemist lab
    show screen hud_modal
    show screen lab_clickable
    show ghost at ghost_left
    show selene wicked grin at selene_bottom_left
    if renpy.get_screen("map"):
        hide screen map
    """
    This is your lab. You can brew potions here.
    Click on the cauldron to start brewing.
    """


label map:
    scene bg map
    show screen map
    if renpy.get_screen("hud"):
        hide screen hud
    if renpy.get_screen("lab_clickable"):
        hide screen lab_clickable
    $ renpy.pause(hard=True)

label woods:
    chance = renpy.random.randint(1, 10)
    if chance > 5 and chance < 8:
        jump woods_interact
    if chance <= 8:
        jump woods_combat
    $ label = "woods"
    scene bg mist woods
    show screen hud_modal
    show ghost at ghost_left
    show selene wicked grin at selene_bottom_left
    show screen button_screen
    if renpy.get_screen("map"):
        hide screen map
    """
    This is the mist woods. You can find __ and __ by foraging, 
    you can fight monsters, or you can interact with the woodland creatures that live here.
    """
    $ renpy.pause(hard=True)

label mountain:
    $ label = "mountain"
    scene bg mountains
    show screen hud_modal
    show ghost at ghost_left
    show selene wicked grin at selene_bottom_left
    if renpy.get_screen("map"):
        hide screen map
    """
    This is the mountains. You can find __ and __ by mining,
    you can fight monsters, or you can interact with the mountain creatures that live here.
    """
    $ renpy.pause(hard=True)