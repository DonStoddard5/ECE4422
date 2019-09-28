
<h1>Connecting PyCharm to remote debug and file transfer to Raspberry Pi</h1>

<h2>File Transfer to Raspberry Pi</h2>

From your desired project, go to the settings menu

![PyCharm settings dropdown](/ConnectingPyCharm/Images/Settings_Menu.JPG)

Under "Build, Execution, Deployment", select "Deployment"

![Deployment Settings](/ConnectingPyCharm/Images/Deployment.JPG)

**Type:** Choose 'SFTP'
**Host:** This is your local IP address, the port is 22
**User Name:** Is the user name for the remote host
**Authentication:** Choose 'Password'
**Password:** Is the password for the user name for the remote host.

Next, select the "Mappings" tab

![Mapping Settings](/ConnectingPyCharm/Images/Deployment_Mappings.JPG)

**Local Path:** This is where files will be stored on your local machine.
**Deployment path:** This is where files will be uploaded to your remote machine.
