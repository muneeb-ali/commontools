commontools
=============

Common functions that are often needed but don't really belong anywhere. To install:

> pip install commontools

Example use for easily configuring a logger:

```
from commontools import setup_logging
import logging
setup_logging()
log = logging.getLogger()
log.debug('this is a debug message')
```

=============

For the logging module, make sure to have a logs/ directory if using log files. Here is an example: 

```
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },

        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": "logs/info.log",
            "maxBytes": "10485760",
            "backupCount": "20",
            "encoding": "utf8"
        },

        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "simple",
            "filename": "logs/errors.log",
            "maxBytes": "10485760",
            "backupCount": "20",
            "encoding": "utf8"
        }
    },

    "loggers": {
        "my_module": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": "no"
        }
    },

    "root": {
        "level": "INFO",
        "handlers": ["console", "info_file_handler", "error_file_handler"]
    }
}
```

