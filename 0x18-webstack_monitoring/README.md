# 0x18. Webstack monitoring
>Project Done in 1 days

![DevOps](https://img.shields.io/badge/-DevOps-yellow)
![SysAdmin](https://img.shields.io/badge/-SysAdmin-yellowgreen)
![monitor](https://img.shields.io/badge/-monitoring-brightgreen)

## Background Context
<p align="center">
  <img src="assets/1.png" width="450" title="gif">
</p>
“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

* Application monitoring: getting data about your running software and making sure it is behaving as expected
* Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

<p align="center">
  <img src="assets/2.jpg" width="450" title="gif">
</p>


## Resources
* _**[What is server monitoring](https://www.sumologic.com/glossary/server-monitoring/)**_
* _**[What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management)**_
* _**[System monitoring by Google](https://sre.google/sre-book/monitoring-distributed-systems/)**_
* _**[Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)**_
* _**[Monitoring](MON.md)**_
* _**[Server](SERVER.md)**_

## Learning Objectives
* Why is monitoring needed
* What are the 2 main area of monitoring
* What are access logs for a web server (such as Nginx)
* What are error logs for a web server (such as Nginx)

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## My servers
| Name | Username | IP | State |
| :--- | :--- | :--- | :--- |
| 96808-web-01 | `ubuntu` | `54.196.27.216` | running |
| 96808-web-02 | `ubuntu`	| `100.26.173.67`	| running	|
| 96808-lb-01	| `ubuntu` | `54.84.8.177` | running |

## Tasks
+ [x] 0\. Sign up for Datadog and install datadog-agent<br/>For this task head to https://www.datadoghq.com/ and sign up for a free `Datadog` account. When signing up, you’ll have the option of selecting statistics from your current stack that `Datadog` can monitor for you. Once you have an account set up, follow the instructions given on the website to install the `Datadog` agent.
  <p align="center">
    <img src="assets/s0.png" width="450" title="gif">
  </p>
  
  * Sign up for Datadog - __Please make sure you are using the US website of Datagog (.com)__
  * Install `datadog-agent` on `web-01`
  * Create an `application key`
  * Copy-paste in your Intranet user profile your DataDog `API key` and your DataDog `application key`.
  * Your server `web-01` should be visible in Datadog under the host name `XX-web-01`
    * You can validate it by using this _**[API](https://docs.datadoghq.com/api/latest/hosts/)**_
    * If needed, you will need to update the hostname of your server
+ [x] 1\. Monitor some metrics<br/>Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some `monitors` within the `Datadog` dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: _**[System Check](https://docs.datadoghq.com/integrations/system/)**_.
  <p align="center">
    <img src="assets/s1.png" width="450" title="gif">
  </p>
  * Set up a monitor that checks the number of read requests issued to the device per second.
  * Set up a monitor that checks the number of write requests issued to the device per second.
+ [x] 2\. Create a dashboard<br/>Now create a dashboard with different metrics displayed in order to get a few different visualizations.

  + Create a new `dashboard`
  + Add at least 4 `widgets` to your dashboard. They can be of any type and monitor whatever you’d like
  + Create the answer file `2-setup_datadog` which has the `dashboard_id` on the first line. __Note__: in order to get the id of your dashboard, you may need to use _**[Datadog’s API](https://docs.datadoghq.com/api/latest/)**_

  __Ans__:- _**[2-setup_datadog](2-setup_datadog)**_

