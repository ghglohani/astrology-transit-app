[app]
title = Astrology Transit App
package.name = astroapp
package.domain = org.astro
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Swiss Ephemeris और Kivy डिपेंडेंसीज़
requirements = python3,kivy,pyswisseph

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
