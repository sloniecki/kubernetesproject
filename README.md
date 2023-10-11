# Kubernetes project
## Summary
This project is (video to mp3 converter with authorization function) aplication build with multiple contenerized services and deployed to K8s loccaly with use of minikube.<br />
<br />
!!!This app dont have UI yet, so all operations must be done via curl!!!<br />
<br />
Stack:<br />
-Kubernetes<br />
-Docker<br />
-Python/flask<br />
-rabbitMQ<br />
-MySQL<br />
-MongoDB<br />
<br />
## Overview
![Blank diagram (2)](https://github.com/sloniecki/kubernetesproject/assets/125316037/37394e35-c4f4-4982-887a-10d54093a4b8)<br />
<br />
1) Gateway service - allow user comunicate with login service and upload/download files.<br />
2) Authentication service - validate user credentials then creates JWT.<br />
3) MySQL - stores user login credentials. <br />
4) RabitMQ - has 2 queues video and mp3, when user uploads video gateway sends message throught video queue to converter service.<br />
   When conversion is finished conversion service sends message that contains mp3 id to mp3 queue which is designeted for notification service.<br />
5) Conversion service - uses moviepy library to convert video to mp3.<br />
6) MongoDB - stores video and mp3 files.<br />
7) Notification service - sends mail to user which contains mp3 id thats used to download converted file.<br />

