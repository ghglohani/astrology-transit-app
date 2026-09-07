[app]
title = Real Astro Transit
package.name = astrotransit
package.domain = org.astro.transit
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Dependencies required for Swiss Ephemeris and Kivy
requirements = python3,kivy,pyswisseph,sqlite3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
