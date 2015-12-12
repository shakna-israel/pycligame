pycligame
=========


**pycligame** is a package containing several tools to ease generating games 
written in Python.

Though originally developed for command-line games, many of its tools are 
applicable to graphics-driven games.

The package contains the following modules:

* player
* validation
* prettyprint
* common


Installation
============

We always recomend you use Virtualenv: 
<https://virtualenv.readthedocs.org/en/latest/>

The easiest way is to install via PyPI:

::
    
    pip install pycligame

However, you can also install via git:

::
    git clone https://github.com/shakna-israel/pycligame
    cd pycligame
    python setup.py install


Usage
=====


player
------

The **player** module contains several classes, aimed at easing the generation 
of Player and Non-Player objects.

Each object inherits from the previous, and can be programmatically generated.

**player.Player()** is a basic player object, and supports the following 
attributes:

* Health
* Strength
* Food

Along with these attributes, it can take the following actions:

* damage
* heal
* weaken
* strengthen
* starve
* feed
* attack
* defend

As well as the special **make** function to generate a new object.
::

    from pycligame import player
    pl = player.Player()
    pl = player.Player.make(health=20)

The other objects, NonPlayer, and NonPlayerBoss inherit these same actions, for 
consistent API.


validation
----------

The validation module is designed to make it easier to enforce values on your 
objects.

It contains the following objects:

* Player

::
    
    from pycligame import player
    from pycligame import validation
    
    validatePlayer = validation.Player()
    pl = player.Player()
    pl.damage(600)
    # pl is -500 now!
    validatePlayer(pl)
    # pl is now 0


prettyprint
-----------

**prettyprint** is mainly aimed at those developing console-based games.

It contains the following functions:

* player_stats

::
    
    from pycligame import player
    from pycligame import prettyprint
    pl = player.Player()
    prettyprint.player_stats(pl)
    # Health: 100%
    # Strength: 100%
    # Hunger: 100%


common
------

**common** contains some wrappers for functions found throughout the package, 
to make life easier.

For example, the **common.printstats()** function both checks for validation 
and calls **prettyprint.player_stats**.


LICENSE
=======

MIT License.

See <https://github.com/shakna-israel/pycligame/master/LICENSE>.
