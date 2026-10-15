[app]

# (str) Title of your application
title = Workout Regimen Selector

# (str) Package name
package.name = workoutregimenselector

# (str) Package domain (required by Android)
package.domain = org.example

# (str) Source code directory
source.dir = .

# (str) Application version
version = 1.0

# (str) Python requirements
requirements = python3,kivy

# (str) Files that Buildozer should include in the APK
source.include_exts = py,txt,png,jpg,jpeg,kv,atlas

# (str) Application orientation
orientation = portrait

# (bool) Fullscreen application
fullscreen = 0

# (str) Presplash image
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon
# icon.filename = %(source.dir)s/data/icon.png


[buildozer]

# (str) Log level
log_level = 2

# (int) Display warning if buildozer is running as root
warn_on_root = 1


[app:android]

# (str) Android API target
android.api = 35

# (str) Minimum Android API
android.minapi = 21

# (str) Android architecture
android.arch = arm64-v8a

# (str) Android application permissions
android.permissions =

# (str) Android backup
android.allow_backup = True

# (str) Android theme
android.entrypoint = org.kivy.android.PythonActivity


# (buildozer.spec documentation)
#
# Project files expected:
#
# WorkoutApp/
#   BMIcreation.py
#   buildozer.spec
#   build_muscle.txt
#   loseweightburnfat.txt
#   Strenghth&endursnce.txt
#
# Build command:
#
#   buildozer android debug
#
# The APK will be created in the bin/ directory.
