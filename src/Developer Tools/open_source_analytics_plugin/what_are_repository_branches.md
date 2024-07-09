## What Are Repository Branches?

Version Control Systems such as Git organize changes that are made during development in branches. This allows developers to keep creating new features or changes to the software without affecting the main product. There are three types of branches in the Open Source Components repository:

* Master (master)
* Release (e.g. vms_4.2, vms_5.0)
* Patch (e.g. vms_4.2_patch)

![](https://meta.nxvms.com/static/media/what-are-repository-branches-/body-757/538-d06704e9-b1ca-4545-88e4-a4cf1c247a48.png)

The **master ** branch is the primary branch that contains the most up to date commits. **Release ** branches contain commits from the Master branch up until a point, these commits are reviewed and tested by developers. **Patch ** branches are created from Release branches and contain fixes which are released as monthly updates after the official release.

Compatibility is guaranteed only for Desktop Clients built from the same commit as the Nx Meta Server. The particular commit can be identified in the repository by its git tag. The public release tags look like `vms/4.2/12345_release_all` or `vms/5.0/34567_beta_meta_R2`.

Desktop Clients built from further commits in the same branch may retain compatibility with the publicly released Nx Meta Server for a while, but will eventually lose compatibility due to how changes are introduced synchronously into different parts of the source code.

In addition to having compatible code, the Desktop Client and Server have to use the same customization package to be able to work together. If you need to connect to a Server with a different customization for experimental/testing purposes, you can bypass this restriction  by adding the following option to desktop_client.ini: developerMode=true.

For additional information about this IniConfig mechanism, see the readme in the GitHub repository.
