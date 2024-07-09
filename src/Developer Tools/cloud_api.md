## Cloud API: Route API Calls via Nx Meta Developer

### Sending API Calls to a System via Nx Meta Developer

Sending Generic Events/API Calls to an Nx Meta System via Nx Meta Developer is both possible and pretty straightforward.

Every API call (like an [HTTP Generic Event](https://meta.nxvms.com/docs/developers/knowledgebase/213)) has a standard structure that begins with [https://address:port/api/](http://addressport/) - which includes:

* the protocol (http, https)
* domain (IP address + port or domain name)
* and path to api (/api).

When sending an API call on a local or virtual network most often the domain is the IP address (either public or private) of the computer running the Nx Meta Server application followed by port 7001 (the default port when installing Nx Meta).

When sending an API call via Nx Meta Developer the request will be transferred through the Nx Meta Developer proxy service (e.g. 3rd Party --> Nx Meta Developer --> Nx Meta Server) and, as a result, you'll need to:

* modify the URL structure
* include the**cloudSystemId**

Below we outline how to do that in a bit more detail.

A few things to consider before you begin:

* Only* HTTPS* calls will work using this method.
* Browser based requests will not work ([CORS protection](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing))
* Supports HLS streams but doesn’t support RTSP streams

### Step 1: Find your cloudSystemId

There are three different methods to find the cloudSystemId:

#### Method 1: Find cloudSystemId in a Browser

This is the simplest method.

1. Log in to Nx Meta Developer ([https://meta.nxvms.com/systems](https://meta.nxvms.com/systems))
2. Select the target System (the System you'd like send API calls to)
3. In the browser check the URL - the cloudSystemId is the long string after https://meta.nxvms.com/systems/

   Example:
   https://meta.nxvms.com/systems/397f56fb-4c5c-485e-a923-9bea345fa7ba
   **397f56fb-4c5c-485e-a923-9bea345fa7ba** is the ID you need

#### Method 2: Find cloudSystemId via a direct API call

Make sure you're logged into the Nx Meta Server Web Admin interface or include

1. Send a direct API call to a Server in your System to request moduleInformation
   * API format:[https://serverIPaddress/api/moduleInformation](https://serveripaddress/api/moduleInformation)
2. Search through the Json response for**cloudSystemId** and you should be good to go.

#### Method 3: Find cloudSystemId via an Nx Meta Developer API call

1. Make a cloud request[https://meta.nxvms.com/cdb/system/get](https://meta.nxvms.com/cdb/system/get) using digest
   authentication and your Nx Meta Developer credentials (username, password).
2. The response will contain a list of all cloud-connected Systems available for the credentials you use.

### Step 2: Update your API call URL to include the Nx Meta Developer relay.

1. Replace the local IP and port of your original request with
   ```
   https://{systemId}.relay.vmsproxy.com
   ```
   Example
   Before:[http://127.0.0.1:7001/api/createEvent?source=Cloud&amp;caption=Test
   ](http://127.0.0.1:7001/api/createEvent?source=Cloud&caption=Test)After:[https://397f56fb-4c5c-485e-a923-9bea345fa7ba.relay.vmsproxy.com](https://397f56fb-4c5c-485e-a923-9bea345fa7ba.relay.vmsproxy.com/)[/api/createEvent?source=Cloud&amp;caption=Test](http://127.0.0.1:7001/api/createEvent?source=Cloud&caption=Test)
