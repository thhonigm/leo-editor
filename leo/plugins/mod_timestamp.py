#@+leo-ver=4-thin
#@+node:edream.110203113231.727:@thin mod_timestamp.py
"""Timestamp all save operations to show when they occur"""

#@@language python
#@@tabwidth -4

# By Paul Paterson.
import leo.core.leoGlobals as g
import leo.core.leoPlugins as leoPlugins

import time

__version__ = "0.1"

#@+others
#@+node:ekr.20100128073941.5374:init
def init():

    # Register the handlers...
    leoPlugins.registerHandler("command1", timestamp)

    g.plugin_signon(__name__)

    return True # OK for unit testing.
#@-node:ekr.20100128073941.5374:init
#@+node:edream.110203113231.728:timestamp
def timestamp(tag=None, keywords=None):

    cmd = keywords.get('label','save')

    if cmd.startswith("save") or cmd.startswith("tangle"):
        g.es("%s: %s" % (cmd, time.ctime()))
#@-node:edream.110203113231.728:timestamp
#@-others
#@-node:edream.110203113231.727:@thin mod_timestamp.py
#@-leo
