######################## STATUS FLAGS
# Ai route
define died = False
$ achievement.register("Stabbed in the back")
define num_deaths=0
$ achievement.register("Some chuunibyo BS") # >2 deaths

# Aoi route
define knows_about_aoi_parents = False
$ achievement.register("A mysterious photograph")
define knows_about_missing_lab_notebook = False
# The knows_about_missing_lab_notebook flag opens up several options:
# * one that makes us able to hide in the science club room's locker after school and verify that Aoi took the book
define knows_aoi_took_lab_notebook = False
$ achievement.register("In the closet")
# * one that makes us able to ask shironeko about the 199X Z-Prize (like trying to get the papers entered)
define read_z_prize_papers = False
$ achievement.register("Peer review")
# * one that lets us skip school at the very beginning of the game by climbing out the window to go investigate in person at Yomiyama Poly's research facility
# That last one branches out: we get killed by a guard having a smoke break behind a pole when we go straight into the employees-only area,
# which opens up a new option to hide behind a neighbouring pole until the guard leaves to do rounds.
define knows_poly_guard_position = False
# We then go up against a keypad lock.
define knows_about_keypad = False
# We inevitably get killed here but now that we know there's a keypad lock we can dare shironeko to get the combination (which will be randomly 
# generated and then stored in persistent storage, so that it's unique to the game copy but the same each time we ask her)
define keycode_try = "0000" # this is input
define keycode_success = False
define keycode = False # this is defined in a python block in start
# Entering the code lets us enter the facility where we eventually find the clone racks. Aoi, who has followed us, kills us here.
define knows_about_clone_racks = False
# Following that death if we do the same operation we open up dialogue trees that will allow us to get Aoi's backstory & info about the clones.
# (But some of the info about the clones should be able to come from getting a copy of the paper from shironeko -- a proposal that probably has 
# fully disconnected cerebellums instead of hypoxic cerebellums. It will be hard to explain the technical details of the cloning in a way consistent
# with even yandere-mode Aoi.)
define knows_whole_aoi_story = False

# Kuroneko route
define knows_about_kuroneko_concert = False
$ achievement.register("Some Eyes-Wide-Shut MFers")
define knows_about_kuroneko_books = False
define knows_about_oss = False

# Koneko route
define knows_about_koneko_telepathy = False
$ achievement.register("Touch telepathy")
define saw_milpsi_symbol = False
define knows_about_stargate = False
define knows_milpsi_shell_co_name = False

# Shironeko route
define knows_about_alien_tech = False
$ achievement.register("The truth is out there")
