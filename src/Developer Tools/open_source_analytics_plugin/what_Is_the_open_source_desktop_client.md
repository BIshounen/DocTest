## What Is the Open-Source Desktop Client?

The primary VMS component in the Nx Meta Platform Open Source Components repository is the Desktop Client. Nx Meta’s Desktop Client code gives developers the freedom to create an identical Desktop Client to the official version from Nx Meta, modify the UI to satisfy unique project requirements or create an entirely new client experience or even a new product. Open the .readme file while going through this article so you can reference it when needed.

Two things are required to build an open-source Desktop Client:

1. [Customization Package](https://meta.nxvms.com/docs/developers/knowledgebase/317-obtaining-a-customization-package-for-the-desktop-client) - contains all the needed branding information: software name, logos, images, support links, etc.
2. Sources from the[GitHub repository](https://github.com/networkoptix/nx_open).

No special skills are necessary to build open source components. Senior/Lead developers with expertise in Windows, MacOs, or Linux development involving C++, Qt framework, Qt Widgets, and QML should have the necessary skills to modify open source components. Developers are welcome to introduce improvements/features into their own custom client to avoid waiting for the Network Optix team to potentially bring requested features to the official version of Nx Meta.

Network Optix is happy to help developers in situations where there is an issue with building unmodified code or instructions on how to build the code are unclear. We are actively working on documenting all parts of the process, so that it will be easier to learn and introduce changes, but we will not support and analyze code samples that developers create using our sources. Additionally, we will not be able to support and investigate issues that are only reproduced in modified clients. Currently, we do not accept external contributions back to the main code, although this may change in the future.

The burden of supporting new products that are built using our sources will be on the external developers that created the modified client. The Nx support team also will not be able to answer extensive questions regarding different modules of our Desktop Client (what are they, what are the functions, etc.). We are actively creating documentation for the different modules that will eventually be released, but for now, external developers will have to figure it out by themselves.
