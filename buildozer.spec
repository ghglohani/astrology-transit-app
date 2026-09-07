[app]
title = Real Astro Transit
package.name = astrotransit
package.domain = org.astro.transit
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# PySwissEph और Kivy
requirements = python3,kivy,pyswisseph

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
