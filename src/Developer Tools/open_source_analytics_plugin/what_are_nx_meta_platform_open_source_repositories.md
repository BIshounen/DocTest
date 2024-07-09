## What Are Nx Meta Platform Open Source Repositories?

Network Optix maintains two open source repositories: **Nx Meta Platform Open Source Components** and **Nx Meta Platform Open Source Integrations** . Each repository serves a different purpose, but they are both great places for developers to access source code, specs, and examples that we have made available.

Both repositories use Git as their version control system. Most of the source code and other files are licensed under the least restrictive terms through the Mozilla Public License 2.0 (unless specified otherwise in the files), which can be found in the license_mpl2.md file in the root directory of the repository.

### [Nx Meta Platform Open Source Components ](https://github.com/networkoptix/nx_open)

This repository contains open-source components used to test, build, or learn about Nx Meta and all other Powered-by-Nx products (see [Developer Program](https://meta.nxvms.com/docs/developers/knowledgebase/224-developer-program) for details). Our developers' commits are synced to the open-source repository allowing these changes to become available for you to see immediately.

Primary contents of the repository:

* Open-Source Desktop Client - the desktop client’s source code.
* Nx Kit - a kit of pure C99/C++11 platform-agnostic utilities useful for experimenting and debugging.
* Example Plugins
  * Sample - a simple plugin with limited capability.
  * Stub Analytics - a plugin that attempts to utilize and demonstrate some of the features present in Nx Meta (best shots, object detection, etc)

### [Nx Meta Platform Open Integrations](https://github.com/networkoptix/nx_open_integrations/tree/master)

This repository contains open-source source code and specifications that show how to integrate a third-party solution with Nx Meta (and all Powered-By-Nx products, including Nx Meta). This is useful for the rapid development of middleware to connect different systems together or to add custom web pages to the systems.

Primary contents of the repository:

* NodeJS Integration Examples - a framework that allows developers and integrators to quickly and easily make integrations with Nx Meta Server using server-side javascript.
* Docker Integration Example - a Dockerfile that can be used to install the Nx Server Ubuntu package.
* API Code Examples
  * Python - covers topics such as authentication and system management that can be used in a script or 3rd party program.
  * Javascript  - covers topics that can be used for web integrations, such as 2-way-audio and embedding videos into web pages.
* OpenVino & OpenCV - example plugins capable of advanced object detection analytics.
