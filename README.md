## HTTP ARchive File Reader

HAR.py is a CLI tool to allow users to inspect and replay HTTP browsing sessions.  

## How to get a HAR file

Right click in FireFox and select inspect element to access developer tools. Click on the network tab and peruse the website you wish to inspect. Right click on the log messages and select 'Save All as HAR'  

## Run Harpy  

To run as part of an interactive python3 session in the REPL:

python3 -m pip install -R requirements.txt  
chmod +x harpy  
./harpy path/to/har/file

## Using Harpy

View the schema of the file  
har.getSchema()  
har.filter('response.status.404')  
har.filter('request.url.*.com*')  
res=har.repeater(42)  
res.text  


## Contributing  

Using pytest for testing, run with ./run_tests.sh

Features to add:  
* Anomaly detection
* Prettify printing
* Repeating session
