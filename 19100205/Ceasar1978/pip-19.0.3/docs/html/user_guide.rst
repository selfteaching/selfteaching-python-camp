==========
User Guide
==========

.. contents::

Running pip
***********

pip is a command line program. When you install pip, a ``pip`` command is added
to your system, which can be run from the command prompt as follows::

  $ pip <pip arguments>

If you cannot run the ``pip`` command directly (possibly because the location
where it was installed isn't on your operating system's ``PATH``) then you can
run pip via the Python interpreter::

  $ python -m pip <pip arguments>

On Windows, the ``py`` launcher can be used::

  $ py -m pip <pip arguments>

Even though pip is available from your Python installation as an importable
module, via ``import pip``, it is *not supported* to use pip in this way. For
more details, see :ref:`Using pip from your program`.


Installing Packages
*******************

pip supports installing from `PyPI`_, version control, local projects, and
directly from distribution files.


The most common scenario is to install from `PyPI`_ using :ref:`Requirement
Specifiers`

  ::

  $ pip install SomePackage            # latest version
  $ pip install SomePackage==1.0.4     # specific version
  $ pip install 'SomePackage>=1.0.4'     # minimum version


For more information and examples, see the :ref:`pip install` reference.

.. _PyPI: https://pypi.org/


Using a Proxy Server
********************

When installing packages from `PyPI`_, pip requires internet access, which
in many corporate environments requires an outbound HTTP proxy server.

pip can be configured to connect through a proxy server in various ways:

* using the ``--proxy`` command-line option to specify a proxy in the form
  ``[user:passwd@]proxy.server:port``
* using ``proxy`` in a :ref:`config-file`
* by setting the standard environment-variables ``http_proxy``, ``https_proxy``
  and ``no_proxy``.


.. _`Requirements Files`:

Requirements Files
******************

"Requirements files" are files containing a list of items to be
installed using :ref:`pip install` like so:

 ::

   pip install -r requirements.txt


Details on the format of the files are here: :ref:`Requirements File Format`.

Logically, a Requirements file is just a list of :ref:`pip install` arguments
placed in a file. Note that you should not rely on the items in the file being
installed by pip in any particular order.

In practice, there are 4 common uses of Requirements files:

1. Requirements files are used to hold the result from :ref:`pip freeze` for the
   purpose of achieving :ref:`repeatable installations <Repeatability>`.  In
   this case, your requirement file contains a pinned version of everything that
   was installed when `pip freeze` was run.

   ::

     pip freeze > requirements.txt
     pip install -r requirements.txt

2. Requirements files are used to force pip to properly resolve dependencies.
   As it is now, pip `doesn't have true dependency resolution
   <https://github.com/pypa/pip/issues/988>`_, but instead simply uses the first
   specification it finds for a project. E.g. if `pkg1` requires `pkg3>=1.0` and
   `pkg2` requires `pkg3>=1.0,<=2.0`, and if `pkg1` is resolved first, pip will
   only use `pkg3>=1.0`, and could easily end up installing a version of `pkg3`
   that conflicts with the needs of `pkg2`.  To solve this problem, you can
   place `pkg3>=1.0,<=2.0` (i.e. the correct specification) into your
   requirements file directly along with the other top level requirements. Like
   so:

   ::

     pkg1
     pkg2
     pkg3>=1.0,<=2.0

3. Requirements files are used to force pip to install an alternate version of a
   sub-dependency.  For example, suppose `ProjectA` in your requirements file
   requires `ProjectB`, but the latest version (v1.3) has a bug, you can force
   pip to accept earlier versions like so:

   ::

     ProjectA
     ProjectB<1.3

4. Requirements files are used to override a dependency with a local patch that
   lives in version control.  For example, suppose a dependency,
   `SomeDependency` from PyPI has a bug, and you can't wait for an upstream fix.
   You could clone/copy the src, make the fix, and place it in VCS with the tag
   `sometag`.  You'd reference it in your requirements file with a line like so:

   ::

     git+https://myvcs.com/some_dependency@sometag#egg=SomeDependency

   If `SomeDependency` was previously a top-level requirement in your
   requirements file, then **replace** that line with the new line. If
   `SomeDependency` is a sub-dependency, then **add** the new line.


It's important to be clear that pip determines package dependencies using
`install_requires metadata
<https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies>`_,
not by discovering `requirements.txt` files embedded in projects.

See also:

* :ref:`Requirements File Format`
* :ref:`pip freeze`
* `"setup.py vs requirements.txt" (an article by Donald Stufft)
  <https://caremad.io/2013/07/setup-vs-requirement/>`_


.. _`Constraints Files`:

Constraints Files
*****************

Constraints files are requirements files that only control which version of a
requirement is installed, not whether it is installed or not. Their syntax and
contents is nearly identical to :ref:`Requirements Files`. There is one key
difference: Including a package in a constraints file does not trigger
installation of the package.

Use a constraints file like so:

 ::

   pip install -c constraints.txt

Constraints files are used for exactly the same reason as requirements files
when you don't know exactly what things you want to install. For instance, say
that the "helloworld" package doesn't work in your environment, so you have a
local patched version. Some things you install depend on "helloworld", and some
don't.

One way to ensure that the patched version is used consistently is to
manually audit the dependencies of everything you install, and if "helloworld"
is present, write a requirements file to use when installing that thing.

Constraints files offer a better way: write a single constraints file for your
organisation and use that everywhere. If the thing being installed requires
"helloworld" to be installed, your fixed version specified in your constraints
file will be used.

Constraints file support was added in pip 7.1.

.. _`Installing from Wheels`:

Installing from Wheels
**********************

"Wheel" is a built, archive format that can greatly speed installation compared
to building and installing from source archives. For more information, see the
`Wheel docs <https://wheel.readthedocs.io>`_ , :pep:`427`, and :pep:`425`.

Pip prefers Wheels where they are available. To disable this, use the
:ref:`--no-binary <install_--no-binary>` flag for :ref:`pip install`.

If no satisfactory wheels are found, pip will default to finding source archives.


To install directly from a wheel archive:

::

 pip install SomePackage-1.0-py2.py3-none-any.whl


For the cases where wheels are not available, pip offers :ref:`pip wheel` as a
convenience, to build wheels for all your requirements and dependencies.

:ref:`pip wheel` requires the `wheel package
<https://pypi.org/project/wheel/>`_ to be installed, which provides the
"bdist_wheel" setuptools extension that it uses.

To build wheels for your requirements and all their dependencies to a local directory:

::

 pip install wheel
 pip wheel --wheel-dir=/local/wheels -r requirements.txt


And *then* to install those requirements just using your local directory of wheels (and not from PyPI):

::

 pip install --no-index --find-links=/local/wheels -r requirements.txt


Uninstalling Packages
*********************

pip is able to uninstall most packages like so:

::

 $ pip uninstall SomePackage

pip also performs an automatic uninstall of an old version of a package
before upgrading to a newer version.

For more information and examples, see the :ref:`pip uninstall` reference.


Listing Packages
****************

To list installed packages:

::

  $ pip list
  docutils (0.9.1)
  Jinja2 (2.6)
  Pygments (1.5)
  Sphinx (1.1.2)

To list outdated packages, and show the latest version available:

::

  $ pip list --outdated
  docutils (Current: 0.9.1 Latest: 0.10)
  Sphinx (Current: 1.1.2 Latest: 1.1.3)


To show details about an installed package:

::

  $ pip show sphinx
  ---
  Name: Sphinx
  Version: 1.1.3
  Location: /my/env/lib/pythonx.x/site-packages
  Requires: Pygments, Jinja2, docutils


For more information and examples, see the :ref:`pip list` and :ref:`pip show`
reference pages.


Searching for Packages
**********************

pip can search `PyPI`_ for packages using the ``pip search``
command::

    $ pip search "query"

The query will be used to search the names and summaries of all
packages.

For more information and examples, see the :ref:`pip search` reference.

.. _`Configuration`:

Configuration
*************

.. _config-file:

Config file
------------

pip allows you to set all command line option defaults in a standard ini
style config file.

The names and locations of the configuration files vary slightly across
platforms. You may have per-user, per-virtualenv or site-wide (shared amongst
all users) configuration:

**Per-user**:

* On Unix the default configuration file is: :file:`$HOME/.config/pip/pip.conf`
  which respects the ``XDG_CONFIG_HOME`` environment variable.
* On macOS the configuration file is
  :file:`$HOME/Library/Application Support/pip/pip.conf`
  if directory ``$HOME/Library/Application Support/pip`` exists
  else :file:`$HOME/.config/pip/pip.conf`.
* On Windows the configuration file is :file:`%APPDATA%\\pip\\pip.ini`.

There are also a legacy per-user configuration file which is also respected,
these are located at:

* On Unix and macOS the configuration file is: :file:`$HOME/.pip/pip.conf`
* On Windows the configuration file is: :file:`%HOME%\\pip\\pip.ini`

You can set a custom path location for this config file using the environment
variable ``PIP_CONFIG_FILE``.

**Inside a virtualenv**:

* On Unix and macOS the file is :file:`$VIRTUAL_ENV/pip.conf`
* On Windows the file is: :file:`%VIRTUAL_ENV%\\pip.ini`

**Site-wide**:

* On Unix the file may be located in :file:`/etc/pip.conf`. Alternatively
  it may be in a "pip" subdirectory of any of the paths set in the
  environment variable ``XDG_CONFIG_DIRS`` (if it exists), for example
  :file:`/etc/xdg/pip/pip.conf`.
* On macOS the file is: :file:`/Library/Application Support/pip/pip.conf`
* On Windows XP the file is:
  :file:`C:\\Documents and Settings\\All Users\\Application Data\\pip\\pip.ini`
* On Windows 7 and later the file is hidden, but writeable at
  :file:`C:\\ProgramData\\pip\\pip.ini`
* Site-wide configuration is not supported on Windows Vista

If multiple configuration files are found by pip then they are combined in
the following order:

1. The site-wide file is read
2. The per-user file is read
3. The virtualenv-specific file is read

Each file read overrides any values read from previous files, so if the
global timeout is specified in both the site-wide file and the per-user file
then the latter value will be used.

The names of the settings are derived from the long command line option, e.g.
if you want to use a different package index (``--index-url``) and set the
HTTP timeout (``--default-timeout``) to 60 seconds your config file would
look like this:

.. code-block:: ini

    [global]
    timeout = 60
    index-url = https://download.zope.org/ppix

Each subcommand can be configured optionally in its own section so that every
global setting with the same name will be overridden; e.g. decreasing the
``timeout`` to ``10`` seconds when running the `freeze`
(`Freezing Requirements <./#freezing-requirements>`_) command and using
``60`` seconds for all other commands is possible with:

.. code-block:: ini

    [global]
    timeout = 60

    [freeze]
    timeout = 10


Boolean options like ``--ignore-installed`` or ``--no-dependencies`` can be
set like this:

.. code-block:: ini

    [install]
    ignore-installed = true
    no-dependencies = yes

To enable the boolean options ``--no-compile`` and ``--no-cache-dir``, falsy
values have to be used:

.. code-block:: ini

    [global]
    no-cache-dir = false

    [install]
    no-compile = no

Appending options like ``--find-links`` can be written on multiple lines:

.. code-block:: ini

    [global]
    find-links =
        http://download.example.com

    [install]
    find-links =
        http://mirror1.example.com
        http://mirror2.example.com


Environment Variables
---------------------

pip's command line options can be set with environment variables using the
format ``PIP_<UPPER_LONG_NAME>`` . Dashes (``-``) have to be replaced with
underscores (``_``).

For example, to set the default timeout::

    export PIP_DEFAULT_TIMEOUT=60

This is the same as passing the option to pip directly::

    pip --default-timeout=60 [...]

For command line options which can be repeated, use a space to separate
multiple values. For example::

    export PIP_FIND_LINKS="http://mirror1.example.com http://mirror2.example.com"

is the same as calling::

    pip install --find-links=http://mirror1.example.com --find-links=http://mirror2.example.com

.. note::

   Environment variables set to be empty string will not be treated as false. Please use ``no``,
   ``false`` or ``0`` instead.


Config Precedence
-----------------

Command line options have precedence over environment variables, which have precedence over the config file.

Within the config file, command specific sections have precedence over the global section.

Examples:

- ``--host=foo`` overrides ``PIP_HOST=foo``
- ``PIP_HOST=foo`` overrides a config file with ``[global] host = foo``
- A command specific section in the config file ``[<command>] host = bar``
  overrides the option with same name in the ``[global]`` config file section


Command Completion
******************

pip comes with support for command line completion in bash, zsh and fish.

To setup for bash::

    $ pip completion --bash >> ~/.profile

To setup for zsh::

    $ pip completion --zsh >> ~/.zprofile

To setup for fish::

$ pip completion --fish > ~/.config/fish/completions/pip.fish

Alternatively, you can use the result of the ``completion`` command
directly with the eval function of your shell, e.g. by adding the following to your startup file::

    eval "`pip completion --bash`"



.. _`Installing from local packages`:

Installing from local packages
******************************

In some cases, you may want to install from local packages only, with no traffic
to PyPI.

First, download the archives that fulfill your requirements::

$ pip download --destination-directory DIR -r requirements.txt


Note that ``pip download`` will look in your wheel cache first, before
trying to download from PyPI.  If you've never installed your requirements
before, you won't have a wheel cache for those items.  In that case, if some of
your requirements don't come as wheels from PyPI, and you want wheels, then run
this instead::

$ pip wheel --wheel-dir DIR -r requirements.txt


Then, to install from local only, you'll be using :ref:`--find-links
<--find-links>` and :ref:`--no-index <--no-index>` like so::

$ pip install --no-index --find-links=DIR -r requirements.txt


"Only if needed" Recursive Upgrade
**********************************

``pip install --upgrade`` now has a ``--upgrade-strategy`` option which
controls how pip handles upgrading of dependencies. There are 2 upgrade
strategies supported:

- ``eager``: upgrades all dependencies regardless of whether they still satisfy
  the new parent requirements
- ``only-if-needed``: upgrades a dependency only if it does not satisfy the new
  parent requirements

The default strategy is ``only-if-needed``. This was changed in pip 10.0 due to
the breaking nature of ``eager`` when upgrading conflicting dependencies.

As an historic note, an earlier "fix" for getting the ``only-if-needed``
behaviour was::

  pip install --upgrade --no-deps SomePackage
  pip install SomePackage

A proposal for an ``upgrade-all`` command is being considered as a safer
alternative to the behaviour of eager upgrading.


User Installs
*************

With Python 2.6 came the `"user scheme" for installation
<https://docs.python.org/3/install/index.html#alternate-installation-the-user-scheme>`_,
which means that all Python distributions support an alternative install
location that is specific to a user.  The default location for each OS is
explained in the python documentation for the `site.USER_BASE
<https://docs.python.org/3/library/site.html#site.USER_BASE>`_ variable.  This mode
of installation can be turned on by specifying the :ref:`--user
<install_--user>` option to ``pip install``.

Moreover, the "user scheme" can be customized by setting the
``PYTHONUSERBASE`` environment variable, which updates the value of ``site.USER_BASE``.

To install "SomePackage" into an environment with site.USER_BASE customized to '/myappenv', do the following::

    export PYTHONUSERBASE=/myappenv
    pip install --user SomePackage


``pip install --user`` follows four rules:

#. When globally installed packages are on the python path, and they *conflict*
   with the installation requirements, they are ignored, and *not*
   uninstalled.
#. When globally installed packages are on the python path, and they *satisfy*
   the installation requirements, pip does nothing, and reports that
   requirement is satisfied (similar to how global packages can satisfy
   requirements when installing packages in a ``--system-site-packages``
   virtualenv).
#. pip will not perform a ``--user`` install in a ``--no-site-packages``
   virtualenv (i.e. the default kind of virtualenv), due to the user site not
   being on the python path.  The installation would be pointless.
#. In a ``--system-site-packages`` virtualenv, pip will not install a package
   that conflicts with a package in the virtualenv site-packages.  The --user
   installation would lack sys.path precedence and be pointless.


To make the rules clearer, here are some examples:


From within a ``--no-site-packages`` virtualenv (i.e. the default kind)::

  $ pip install --user SomePackage
  Can not perform a '--user' install. User site-packages are not visible in this virtualenv.


From within a ``--system-site-packages`` virtualenv where ``SomePackage==0.3`` is already installed in the virtualenv::

  $ pip install --user SomePackage==0.4
  Will not install to the user site because it will lack sys.path precedence


From within a real python, where ``SomePackage`` is *not* installed globally::

  $ pip install --user SomePackage
  [...]
  Successfully installed SomePackage


From within a real python, where ``SomePackage`` *is* installed globally, but is *not* the latest version::

  $ pip install --user SomePackage
  [...]
  Requirement already satisfied (use --upgrade to upgrade)

  $ pip install --user --upgrade SomePackage
  [...]
  Successfully installed SomePackage


From within a real python, where ``SomePackage`` *is* installed globally, and is the latest version::

  $ pip install --user SomePackage
  [...]
  Requirement already satisfied (use --upgrade to upgrade)

  $ pip install --user --upgrade SomePackage
  [...]
  Requirement already up-to-date: SomePackage

  # force the install
  $ pip install --user --ignore-installed SomePackage
  [...]
  Successfully installed SomePackage


.. _`Repeatability`:

Ensuring Repeatability
**********************

pip can achieve various levels of repeatability:

Pinned Version Numbers
----------------------

Pinning the versions of your dependencies in the requirements file
protects you from bugs or incompatibilities in newly released versions::

    SomePackage == 1.2.3
    DependencyOfSomePackage == 4.5.6

Using :ref:`pip freeze` to generate the requirements file will ensure that not
only the top-level dependencies are included but their sub-dependencies as
well, and so on. Perform the installation using :ref:`--no-deps
<install_--no-deps>` for an extra dose of insurance against installing
anything not explicitly listed.

This strategy is easy to implement and works across OSes and architectures.
However, it trusts PyPI and the certificate authority chain. It
also relies on indices and find-links locations not allowing
packages to change without a version increase. (PyPI does protect
against this.)

Hash-checking Mode
------------------

Beyond pinning version numbers, you can add hashes against which to verify
downloaded packages::

    FooProject == 1.2 --hash=sha256:2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

This protects against a compromise of PyPI or the HTTPS
certificate chain. It also guards against a package changing
without its version number changing (on indexes that allow this).
This approach is a good fit for automated server deployments.

Hash-checking mode is a labor-saving alternative to running a private index
server containing approved packages: it removes the need to upload packages,
maintain ACLs, and keep an audit trail (which a VCS gives you on the
requirements file for free). It can also substitute for a vendor library,
providing easier upgrades and less VCS noise. It does not, of course,
provide the availability benefits of a private index or a vendor library.

For more, see :ref:`pip install\'s discussion of hash-checking mode <hash-checking mode>`.

.. _`Installation Bundle`:

Installation Bundles
--------------------

Using :ref:`pip wheel`, you can bundle up all of a project's dependencies, with
any compilation done, into a single archive. This allows installation when
index servers are unavailable and avoids time-consuming recompilation. Create
an archive like this::

    $ tempdir=$(mktemp -d /tmp/wheelhouse-XXXXX)
    $ pip wheel -r requirements.txt --wheel-dir=$tempdir
    $ cwd=`pwd`
    $ (cd "$tempdir"; tar -cjvf "$cwd/bundled.tar.bz2" *)

You can then install from the archive like this::

    $ tempdir=$(mktemp -d /tmp/wheelhouse-XXXXX)
    $ (cd $tempdir; tar -xvf /path/to/bundled.tar.bz2)
    $ pip install --force-reinstall --ignore-installed --upgrade --no-index --no-deps $tempdir/*

Note that compiled packages are typically OS- and architecture-specific, so
these archives are not necessarily portable across machines.

Hash-checking mode can be used along with this method to ensure that future
archives are built with identical packages.

.. warning::
    Finally, beware of the ``setup_requires`` keyword arg in :file:`setup.py`.
    The (rare) packages that use it will cause those dependencies to be
    downloaded by setuptools directly, skipping pip's protections. If you need
    to use such a package, see :ref:`Controlling
    setup_requires<controlling-setup-requires>`.

.. _`Using pip from your program`:

Using pip from your program
***************************

As noted previously, pip is a command line program. While it is implemented in Python,
and so is available from your Python code via ``import pip``, you must not use pip's
internal APIs in this way. There are a number of reasons for this:

#. The pip code assumes that is in sole control of the global state of the program.
   Pip manages things like the logging system configuration, or the values of the
   standard IO streams, without considering the possibility that user code might be
   affected.

#. Pip's code is *not* thread safe. If you were to run pip in a thread, there is no
   guarantee that either your code or pip's would work as you expect.

#. Pip assumes that once it has finished its work, the process will terminate. It
   doesn't need to handle the possibility that other code will continue to run
   after that point, so (for example) calling pip twice in the same process is
   likely to have issues.

This does not mean that the pip developers are opposed in principle to the idea that
pip could be used as a library - it's just that this isn't how it was written, and it
would be a lot of work to redesign the internals for use as a library, handling all
of the above issues, and designing a usable, robust and stable API that we could
guarantee would remain available across multiple releases of pip. And we simply don't
currently have the resources to even consider such a task.

What this means in practice is that everything inside of pip is considered an
implementation detail. Even the fact that the import name is ``pip`` is subject to
change without notice. While we do try not to break things as much as possible, all
the internal APIs can change at any time, for any reason. It also means that we
generally *won't* fix issues that are a result of using pip in an unsupported way.

It should also be noted that installing packages into ``sys.path`` in a running Python
process is something that should only be done with care. The import system caches
certain data, and installing new packages while a program is running may not always
behave as expected. In practice, there is rarely an issue, but it is something to be
aware of.

Having said all of the above, it is worth covering the options available if you
decide that you do want to run pip from within your program. The most reliable
approach, and the one that is fully supported, is to run pip in a subprocess. This
is easily done using the standard ``subprocess`` module::

  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'my_package'])

If you want to process the output further, use one of the other APIs in the module::

  reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])

If you don't want to use pip's command line functionality, but are rather
trying to implement code that works with Python packages, their metadata, or
PyPI, then you should consider other, supported, packages that offer this type
of ability. Some examples that you could consider include:

* ``packaging`` - Utilities to work with standard package metadata (versions,
  requirements, etc.)

* ``setuptools`` (specifically ``pkg_resources``) - Functions for querying what
  packages the user has installed on their system.

* ``distlib`` - Packaging and distribution utilities (including functions for
  interacting with PyPI).
