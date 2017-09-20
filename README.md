# update-test
Quick&amp;dirty tools to test webextension updates

The attached server.py script runs a simple web server that serves
a webextension plus an update for that webextension, useful for testing
the browser update path.

The `server.py` script takes two parameters, the IP address on which it
should listen, and the port on which it should listen.  For testing on
Android from the emulator (or for testing from a different host), this
obviously needs to be a non-loopback address.

Since these extensions are unsigned, you must first go to about:config
and flip the preference xpinstall.signatures.required to false.

Once the server is running, visit `http://IP:PORT/install.html` and
click on the "Install v1" link.  The browser should present some prompts,
accept these, and the first version of the extension should be installed.
From here, to trigger an update on desktop Firefox, navigate to
about:addons, click on "Extensions", then click on the gear icon and choose
"Check for updates".  On mobile, either go to about:config and set
extensions.autoupdate.interval to a small value (eg 1) and wait for an update
check, or connect to the main process with the debugger and evaluate the
statement:

```
AddonManagerPrivate.backgroundUpdateCheck()
```

This should trigger the browser to check for an update and show the update
indicator (a badge on the hamburger menu on desktop, or an icon next to the
top-level Add-ons menu item in the application menu on mobile)
