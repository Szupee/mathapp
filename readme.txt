https://jolly-mud-0ccb18c10.2.azurestaticapps.net

Hello,

This is a very rudimental and overenginered calculator. 

Main focus is to separeta the operation between microservices using Azure Cloud services.
Services:
-App Service
-App Gateway
-Static Web app
-Virtual network
-Azure Function
-Azure Container registry

Other tools and languages:
-Docker
-Python
-HTML/JS
-Yaml


Structure

-Frontend is running on Azure Static Web app and sending the request to an Azure App Gateway
	Any updates will be deployed automaticcaly by github action

-APIs
   -Azure Function 
   -Flask based API run in docker container, Container run in App service. 
	- Github action updates the docker container and push it to Azure Container reqistry.

-Azure App gateway
Listener is on the port 80, A path based rule connected to the listener.
The /add and /subtract need an URL rewrite to call the Azure Functions.



Other:
Error.html added to the static website and used in APP Gateway in case the backend not running


FUTURE UPDATE:
Implement HTTPS
Set up own Domain name