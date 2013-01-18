finally
=======

finally: a decent file manager

in my spare time i'm trying to make a common lisp file manager.

some of the goals of this project:

* graphical
* thumbnails for EVERYTHING (even directories - to preview contents)
* do things as intelligently as possible
* everything should be able to be done with the keyboard
* lots of commands, some of which imitate shell counterparts (i.e. "cd" to change directory; "ls" would refresh the view of the current directory)
* use mcclim for the GUI (i don't know much about mcclim so this is my way to learn it, as well as common lisp)
* easily scriptable/changable by the user
* logical & consistent
* use settings from other things (i.e. `.dircolors`, maybe copy a few settings from `.zshrc` or something; but always allow settings to be overridden by finally's config file)
* play well with tiling window managers (and everything else, ideally)
* fast & responsive
* waste as little screen space as possible.
* sensible defaults
* display a lot of (useful) information

why?
====

to learn common lisp, to finally write an actual application instead of just scripts, but most importantly, to Finally have A Decent File Manager.

decent?
=======

maybe using lisp is "indecent" to you. feel free to use your own (probably boring) favorite language to write your own file manager.

and no, i haven't really found any file managers i consider to be "decent". a few come close:

* `thunar` is my current default. simple, fast, isn't obnoxious, is kind of customizable, and doesn't totally ignore the keyboard. could be better though.
* `spacefm` is uh... weird? i can't figure it out, and it doesn't inspire me enough to make me want to.
* `dolphin` - that's the name of kde's file manager, right? well, i don't use kde. i recall it having great thumbnail capabilities when i did use it - including the directory thumbnails that i wish others had - but it takes too long to start up and also would require me to have a bunch of other kde stuff on my computer.
* `nautilus` - lol. gnome sucks. also, i don't need a desktop when i start up a file manager (i really have no idea what that's about)
* `emacs dired with images` - i tried this once and it took a long time to generate thumbnails for a directory. and while it was doing so, it was unresponsive. plus emacs is definitely not the ideal environment for thumbnails and the like. i'd prefer a grid.

maybe i haven't given some of these enough of a chance, but i kind of just want to write my own anyway.

