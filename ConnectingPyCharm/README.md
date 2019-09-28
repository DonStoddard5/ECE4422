
<h1>Connecting PyCharm to remote debug and file transfer to Raspberry Pi</h1>

<h2>Remote depugging</h2>

From your desired project, go to the settings menu

![PyCharm settings dropdown](/ConnectingPyCharm/Images/Settings_Menu.JPG)

Under "Project: your_project_name", select "Project Interpreter"

![Project Interpreter](/ConnectingPyCharm/Images/Project_Interpeter.JPG)

From here, either select settings you've already chosen from the "Project Interpreter:" list, or click the gear on the far right and click "Add..."

From the new window, click on "SSH Interpreter" in the left panel.

![SSH Interpreter](/ConnectingPyCharm/Images/sshInterpreter.JPG)

**Host:** This is your remote machine's local IP address

**Port:** Leave as "22"

**Username:** This is the user login for the remote machine

Click "Next" and the "Add Python Interpreter" window will appear

[Add Python INterpreter](/ConnectingPyCharm/Images/Add_Python_Interpreter.JPG)

**Interpreter:** This is where you select where the interpreter is on your remote machine. By deafault on Raspberry Pi, it's under "/usr/bin/python". You can leave this unchaned.

**Sync Folders:** This is where your project folders will be synced. Either change it here, or see the next section for instructions.

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

Last, click "OK" or "Apply" and you're done!
