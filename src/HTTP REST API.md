## HTTP REST API

### What is Nx Meta Server API?

The Server API provides a standard set of HTTP calls for 3rd party systems. Using the Server API, developers have the ability to access nearly every feature available in the system's thick client, including but not limited to:

* query/manage system resources (servers, cameras, users)
* manage users and permissions
* pull live or recorded video out of the system
* generate events
* create rules
* control PTZ cameras, and more

### How to use Nx Meta Server API?

Nx Meta provides documentation to help developers work with the Nx Meta Server. All parameters and expected returns are listed.

The APIs are all under the RESTFUL standard, so developers are able to simply interact with Nx Meta Server via HTTP using POST or GET requests. With the latest release, PUT, PATCH, and DELETE requests will also be possible. No matter which programming language you use, you can always retrieve the data and integrate your system with Nx Meta.

### How to access the API Documentation?

#### Method 1

Navigate to the online REST API documentation through **[THIS](https://meta.nxvms.com/doc/developers/api-tool/)** link.

#### Method 2

If you have the latest Nx Meta (Client & Server) installed, you can access the new API, with the updated Swagger UI, by visiting the WebAdmin (using the format below) and clicking on **API Documentation** at the bottom of the page.

```
http://<server_ip>:<server_port>
```

The API is divided into 3 main sections:

* Nx Meta VMS Server API — contains the new API calls.
* Nx Meta VMS Server legacy API — contains API calls from the previous versions that still work.
* Nx Meta VMS Server deprecated API — contains the deprecated API calls that may still work, but are not recommended for use.

**Note** : Some API calls may have been deprecated in this update. If you refer to the API calls under *Nx Meta VMS Server deprecated API* , the description in the deprecated calls will refer you to the new API calls to use that fulfill the same purpose; this will appear as text in the request description that says "Deprecated in favor of X", where "X" will be the new call.

### Testing the API

To help our users get started with Nx Meta, we provide a simple tool for you to test the API and view readable return data.

1. Open the Web Admin interface and visit the API trial page:

   ```
   http://<server_ip>:<server_port>/static/index.html#/developers
   ```
2. On the page, you will be able to find the “**API Testing Tool (new)** ” under the **Server API** section.

   <details><summary><span>Visual Example</span></summary>

   ![image.png (2039×1522)](https://meta.nxvms.com/static/media/server-http-rest-api/body-617/body-baeb050d-6ec5-4de4-abab-740664a89382.png)

   </details>
3. Click the link of “**API Testing Tool (new)** ”. You will then see the list of all server APIs, and you could click any of them to test and try the API.

   <details><summary data-gramm="false" data-lt-tmp-id="lt-540734" spellcheck="false"><span>Visual Example</span></summary>

   ![image.png (2388×1404)](https://meta.nxvms.com/static/media/server-http-rest-api/body-618/body-32bd034f-f6c5-4dae-b306-c1345785a5d2.png)

   ![193BD301-70F4-4F14-86B3-0A7121F2ACdAB.jpeg](https://meta.nxvms.com/static/media/server-http-rest-api/body-619/body-9c7c6b9f-393d-424c-9bd1-06f7e6c37e22.png)

   </details>

[© Network Optix](http://networkoptix.com/meta/)* [Downloads](https://meta.nxvms.com/download)

* [Terms](https://meta.nxvms.com/content/eula)
* [Privacy](http://www.networkoptix.com/privacy-policy/)
* [System Calculator](http://nx.networkoptix.com/calculator/)
* [Support](https://support.networkoptix.com/hc/en-us/community/topics/115000552988-Developer-Forum)
