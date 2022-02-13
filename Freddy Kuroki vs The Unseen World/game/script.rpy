init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve

label start:
    window hide
    nvl hide
    jump index
    return

define menuTitle = Character(None, kind=nvl, what_prefix="{b}{size=+20}", what_suffix="{/size}{/b}")
