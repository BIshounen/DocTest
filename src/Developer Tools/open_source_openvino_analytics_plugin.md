## Open-Source OpenVINO Analytics Plugin

### What is OpenVINO Analytics Plugin?

OpenVINO Object Detection Analytics Plugin is an open-source plugin created for Nx Meta to demonstrate person detection and tracking.

It is meant to be used as an example of what an Analytics Plugin integrated with Nx Meta could look like, and not for end-user purposes. It may or may not fulfill the requirements of a video management system in terms of reliability and detection quality — use at your own risk.

It is based on the OpenVINO technology by Intel and runs on Intel processors only. See [System Requirements for Intel® Distribution of OpenVINO™ Toolkit](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit/system-requirements.html).

#### OpenVINO plugin features

* Person detection
* Line crossing detection
* Loitering detection
* Motion detection

### How can I use the OpenVINO Analytics Plugin source code?

You can build your own OpenVINO plugin by retrieving the source code from our [open-source repository](https://github.com/networkoptix/nx_open_integrations/tree/master/cpp/vms_server_plugins/openvino_object_detection_analytics_plugin) and replacing the training models with your own.

Alternatively, you can use the source code as an example to base your own plugin on.

### Getting started

Visit the [OpenVINO Analytics Plugin repository](https://github.com/networkoptix/nx_open_integrations/tree/master/cpp/vms_server_plugins/openvino_object_detection_analytics_plugin) and clone it to get started on your own Plugin.

* For the build requirements, see[*readme.md*](https://github.com/networkoptix/nx_open_integrations/blob/master/cpp/vms_server_plugins/openvino_object_detection_analytics_plugin/readme.md) in the repository.
* For guidance on creating Analytics Plugins, refer to[How to Create a Video Analytics Plugin](https://meta.nxvms.com/docs/developers/metaknowledgebase/200).
* For guidance on debugging plugin issues, refer to[Nx Meta Server Plugin Debugging](https://meta.nxvms.com/docs/developers/metaknowledgebase/212)

For general information on building and installing Plugins for Nx Meta Server, see *readme.md* in the [Metadata SDK](https://meta.nxvms.com/download/sdk).
