# OWASP Threat Dragon RPM SPEC

This is currently a WIP SPEC file for
[OWASP/Threat-Dragon](https://github.com/owasp/threat-dragon). Threat Dragon's
website and build system creates an RPM by default, since it is an Electron App.
We are not using that RPM because the Fedora packaging guidelines require that
the SPEC file in the repo works.

## Goals

1) Comply with Fedora guidelines
2) Remove packaged-in dependencies (libffmpeg needs to be its own RPM for
instance)
3) Distribute packaging details in the FS appropriately
4) Provide Man-Pages for the tool
