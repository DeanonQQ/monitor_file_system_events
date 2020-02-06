# Monitoring File System Events

## Tracking changes to files in a folder

1. The first application (client) recursively scans a specific folder on the hard disk every 2 seconds (the folder is passed through the application argument) and passes the path and size of files to the second application via TCP connection (the ip address and port are passed through the argument) when they are changed (including appearing and deleting) in these folders.

2. The second application (server) accepts all TCP connections from any number of running first applications (in parallel) and outputs the file path, size, and type of change (new file, deleted file, modified file) to the console, adding information about the time when the message was received.
Example of usage: the first application is launched on a set of workstations that we need
interesting. The second application runs on the system administrator's workstation for
analysis of user behavior in a specific (each with its own) folder on their computers.
