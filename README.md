# Web-Server-Logs-Analysis
## By Narotam Singh
An internal reporting tool that will use information from the database ( contains newspaper articles, as well as the web server log for the site) to discover what kind of articles the site's readers like. The log has a database row for each time a reader loaded a web page. 

## Output of code:
Using above information, this code will answer following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

## Requirements:
    Python
    Vagrant
    Virtual Box
    PostgreSQL
    
 ## How to install and use:
* Install [Virtual Box](https://www.virtualbox.org/wiki/Downloads), [Vagrant](https://www.vagrantup.com/downloads.html).
* Clone the VM configuration [vm](https://github.com/udacity/fullstack-nanodegree-vm)
* [Download this repo](https://github.com/narotamsingh/Web-Server-Logs-Analysis/archive/master.zip) Or [Clone](https://github.com/narotamsingh/Web-Server-Logs-Analysis.git) this repo into the `/vagrant` directory.
* Launch the VM:
  * `$ vagrant up`
* SSH into the VM:
  * `$ vagrant ssh`
* In the VM navigate to the `/vagrant` folder:
  * `vagrant@vagrant:~$ cd /vagrant`
* [Download Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
  The file inside is called `newsdata.sql`, put this file into the `vagrant` directory, which is shared with your virtual machine.
* Load the data into the `news` database already in the VM:
  * `vagrant@vagrant:~$ psql -d news -f newsdata.sql`
* Run application:
  * `vagrant@vagrant:~$ python wlogs_analysis.py`

 ## Output:
![Image for output](/image/output.png?raw=true "Output")
