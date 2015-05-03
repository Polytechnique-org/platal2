Migration from plat/al 1
========================

For a smooth transition from the first version of plat/al,
some rules are required.


Coexistence
    * The new site **MUST** reuse most URLs from the old site
    * The Apache config can be used to switch sets of URLs to the new site

Database
    * The old MySQL database will be kept as the main storage engine
    * An additional database can be used for specific needs of the new stack
    * Old tables can be altered (e.g adding an ``auto_increment`` field) for greater compatibility

Authentication
    * Users **SHALL** authenticate only once during a session, even when switching versions
    * The password (for strong authentication with sensitive tasks) **MAY** be required twice,
      as few pages require this for common usage
    * Option 1: Use ``authgroupex`` from the new site to the old
    * Option 2: The new site reads the PHP sessions — but this might break logout

Design
    * Skin choice isn't available on the new site
    * Enforce the ``NewDefault`` skin for the old site once finished
    * Make sure the menu / header / footer have the same look between both sites


