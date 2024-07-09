# Testcamera: IP Camera Emulator

# What is Testcamera?

Testcamera is an experimental application that allows users to stream a looped video file as an emulated camera. Testcamera is launched using a command-line interface (i.e., Terminal, CMD, etc.).

It solves several problems:

* **Development** : Developers can work on integrations without hardware devices (cameras, network gear, etc).
* **Debugging** : Create a predictable and replicable video stream for testing and debugging video analytics solutions
* **Performance testing** : Create hundreds of “cameras” to test hardware and software performance and reliability
* **Demonstrations** : Create a mobile software-only “camera” set to use in demos

# Installing Testcamera

## Windows

Testcamera is available to download as a separate application on the [Integrations Marketplace](https://meta.nxvms.com/integrations/34).

1. Create a folder in the directory of your choice and name it***test_camera*** (for example, C:\test_camera)
2. Download the Testcamera package and extract it to***C:\test_camera***
3. Place any video files you plan on using into***C:\test_camera***
4. Open CMD and navigate to the test_camera folder:

```
cd C:/test_camera
```

```
    5. Run the testcamera command with your desired parameters and values.
```

## Linux

Testcamera is included in the server package for all Ubuntu installations.

1. Using admin permissions, place any video files you plan on using into
   /opt/networkoptix-metavms/mediaserver/bin*

   * **Note** : If you do not have admin permissions to place video files in the same folder as the Testcamera application, you will have to use the full file path of the videos in the cameraSet.
2. Open Terminal and navigate to the folder the testcamera binary resides in:

```
      cd /opt/networkoptix-metavms/mediaserver/bin
```

```
    3. Run the ./testcamera command with your desired parameters and values.
```

# Using Testcamera

```
<filePath>/testcamera <option> <cameraSet>;<cameraSet2>
```

* **`<option>`** – the below options
  * **-I** – limit discoverability of testcameras to a specified network interface (for example, to limit the testcameras to your machine: -I=127.0.0.1). See*Testcamera Limitations* below for more information.
  * **-S** – create a separate Testcamera per primary video file
* **`<cameraSet>`** – at least one set of semi-colon separated parameters, such as below
  * **files="" ** – a comma-separated list of video files for high-quality/primary streams
  * **secondary-files=""** – a comma-separated list of video files for low-quality/secondary streams (optional)
  * **count** – number of testcameras to create, if more than one is needed (for example, count=5)

**NOTE: ** Run the testcamera command with no parameters to access the help function and see the complete list of commands.

## Create one Testcamera that can only be discovered by local servers:

```
testcamera -I 127.0.0.1 "files=C:/hq.mkv;secondary-files=lq.mkv"
```

## Create 100 identical Testcameras that can only be discovered by local Server:

```
testcamera -I 127.0.0.1 "files=hq1.mkv;secondary-files=lq1.mkv;count=100"
```

## Create three Testcameras from three different source files:

```
testcamera -S "files=hq1.mkv,hq2.mkv,hq3.mkv;secondary-files=lq1.mkv,lq2.mkv,lq3.mkv"
```

## Create three Testcameras from three different source files that can only be discovered by local Server:

```
testcamera -S -I 127.0.0.1 "files=hq1.mkv,hq2.mkv,hq3.mkv;secondary-files=lq1.mkv,lq2.mkv,lq3.mkv"
```

## Emulating 2-way audio capability

The Server can emulate 2-way audio capability on a Testcamera instance. To accomplish that, do the following.

1. On the Server, in the test_camera.ini enable 2-way audio for the Testcamera with the following edit:

```
      declareTwoWayAudio=true
```

```
 For more details on configuring the Server via .ini files, refer to the Configuring via .ini files—IniConfig article.

 2. Restart the Server
```

With this flag set, the Server will emulate 2-way audio with Testcamera instances.

# Best Practices

## Use Relevant Files

Create and utilize video files similar to the conditions you would like to replicate. The easiest way to get such a sample is to set the real camera to record a sample and then export that part of the archive.

## Adjusting the Frame Rate (FPS)

If you want to change the camera frame-per-second (fps) rate, you can modify the frame rate using camera settings using the Desktop Client:

Select all Testcameras you want to modify (drag across cameras in the Desktop Client to choose multiple), open the Camera Settings Dialog, adjust the recording schedule to the desired FPS, and save to apply the changes.

## Network Loading

Be careful when using Testcamera on a network with several Servers running on the same LAN subnet. Each Server will discover the Testcamera “cameras” and add them to their database.

**Note:** Use the **-I**  key to limit availability by network.

## Quick Start

We recommended creating an executable script (.bat for Windows, .sh for Linux) to start Testcamera quickly.

# Testcamera Limitations

* Testcamera loads every file to memory, so using it with many different files requires additional memory.
* Testcamera uses only the first 100 MB of a file.
* Testcamera is only compatible with the same version of the Server.

# Available Sample Files

Select “Save link as..” to download these sample video files:

* [Timer High stream](https://meta.nxvms.com/static/media/testcamera--ip-camera-emulator/-additional-file-1--556/Timer_High_Stream.mkv)
* [Timer Low stream](https://meta.nxvms.com/static/media/testcamera--ip-camera-emulator/-additional-file-2--557/Timer_Low_Stream.mkv)
* [Traffic High stream](https://meta.nxvms.com/static/media/testcamera--ip-camera-emulator/-additional-file-3--797/Traffic_High_Stream.mkv)
* [Traffic Low stream](https://meta.nxvms.com/static/media/testcamera--ip-camera-emulator/-additional-file-4--559/Traffic_Low_Stream.mkv)
