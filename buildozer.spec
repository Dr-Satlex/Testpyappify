[app]

# These four get overwritten by Piappify's patch step at build time —
# left here just so the file is valid if someone runs buildozer locally.
title = Piappify Test App
package.name = piappifytest
package.domain = org.piappify

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
