# Instructions to configure XAMPP
Find line ```ScriptAlias /cgi-bin/ "/opt/lampp/cgi-bin/"``` in /opt/lampp/etc/```httpd.conf```
##### Do not comment out this line as shown in offcial docs.
Below this line, paste
```
<Directory "/opt/lampp/cgi-bin/">
    AddHandler cgi-script .cgi .py
    AllowOverride All
    Options +ExecCGI
    Order allow,deny
    Allow from all
</Directory>
```
Then run ```sudo chmod a+x cgi-bin/file_name.py``` to change file permissions.
Open ```localhost/cgi-bin/file_name.py``` in browser.
```.html``` files won't run in ```cgi-bin``` folder.
Run them from ```htdocs```.

# Instructions for the ```py``` file to be run as ```cgi``` file
Add this line before ```print``` statement-
```python
print("Content-Type: application/json\n")
```
Change ```application/json``` as required and ```\n``` is compulsory according to official docs.