# Logguard
Python log archiver util that allows to store logs in Apache/Nginx manner.
Log rotation based on time.

### Usage

```
Usage: python logguard.py [options]
Options:
  -h                Display help message
  -i, --infile      File to archive and clean
  -l, --logdir      Directory to store archive
```

### Usage example
```
python log_guard.py -i server_info.log -l /logs

Crontab example:
0 4 * * * python /path_to_script/log_guard.py -i /path_to_logfile/server_info.log -l /path_to_arhives/logs
```

### Results
```
\logs
    -logfile.log
    -0server.log.tar.gz
    -1server.log.tar.gz
    -2server.log.tar.gz
    -3server.log.tar.gz
    ...
```

