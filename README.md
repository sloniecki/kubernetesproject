# Kubernetes project
## Summary
This project is (video to mp3 converter with authorization function) aplication build with multiple dockerized services and deployed to K8s loccaly with use of minikube.<br />
!!!This app dont have UI yet, so all operations must be done via curl!!!<br />
<br />
<br />
Stack:<br />
-Kubernetes<br />
-Docker<br />
-Python/flask<br />
-rabbitMQ<br />
-MySQL<br />
-MongoDB<br />
<br />
##Overview
![Blank diagram (2)](https://github.com/sloniecki/kubernetesproject/assets/125316037/37394e35-c4f4-4982-887a-10d54093a4b8)<br />
<br />
1) Gateway service - allow user comunicate with login service and upload/download files.
2) Authentication service - validate user credentials then creates JWT Token.
3) MySQL - stores user login credentials. 
4) RabitMQ - 


