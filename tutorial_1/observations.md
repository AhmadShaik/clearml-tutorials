# Clearml-tutorails - 1
  In this tutorial, I will show you how to start uisng the clearml, initializing the clearml with an open server, tracking the progress using a simple mnist example.

## Step-1 - Installing the ClearML
  If you have an environment with tensorflow already installed init, then you can install the clearml using pip. Or else you can find necessary packages inside the requirements.txt.

  ```
  $ pip install cleaml
  ```
## Step-2 - Initialization of cleaml with server
  The next step to perform after installing the clearml is initializing with the server using `clearml-init`. In this example we are using an open server. As per the documantion We can also create and host our own server locally. This one we cover in the future tutorials

  ```
  $ clearml-init
  ```
  This shows a response like below and asks you to enter the credentials for workspace configuration.

  ```
  ClearML SDK setup process

  Please create new clearml credentials through the profile page in your `clearml-server` web app (e.g. http://localhost:8080/profile)
  Or create a free account at https://app.community.clear.ml/profile

  In the profile page, press "Create new credentials", then press "Copy to clipboard".
  ```  
  The actual place where it shows the credentials is `https://app.clear.ml/settings/workspace-configuration`. If you haven't created any account in the server, you need to create a free account in the server. There you can see an option to *Create new credentials*.
  ![image11](images/new_credits.png "withvswothput_light")  

  pasting that and accepting the api addresses will complete the initialization work.

  ```
  Paste copied configuration here: We get this copy from the above link.
  api {
      # Shaik Ahmad's workspace
      web_server: https://app.clear.ml
      api_server: https://api.clear.ml
      files_server: https://files.clear.ml
      credentials {
          "access_key" = "QVY5AYRUY44AYHB0NHYM"
          "secret_key" = "qef14khBo1hvR6LsqPjRqZXlQfJZi4BzXTy5lUnyehT9dD4Q34"
      }
  }
  Detected credentials key="QVY5AYRUY44AYHB0NHYM" secret="qef1***"
  WEB Host configured to: [https://app.clear.ml]
  API Host configured to: [https://api.clear.ml]
  File Store Host configured to: [https://files.clear.ml]

  ClearML Hosts configuration:
  Web App: https://app.clear.ml
  API: https://api.clear.ml
  File Store: https://files.clear.ml

  Verifying credentials ...
  Credentials verified!

  New configuration stored in /root/clearml.conf
  ClearML setup completed successfully.    
  ```
  In this web_server URL, api_server URL and files_server URLS by default assigned to clearML open server. If we run the server locally that address will change to localhost. Or if you run it on aws instance we might need to specify the URLs.
    
