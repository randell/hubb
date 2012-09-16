Hubb
========

Hubb is a high-performance hub implementation of [PubSubHubbub](http://code.google.com/p/pubsubhubbub/) written with Twisted Python.

Implementation Details
----------------------
Currently the hub is stateless and subscriptions are lost when the process finished, so it's not really production ready. BUT that's the first thing to be added once tests are in place. ;)

Installing
----------
Installing Hubb is a walk in the park:

`sudo python setup.py install`

You can run the tests to be sure everything is OK:

`trial hubb`

Using Hubb
--------------
You can start Hubb with `hubb -p 8123`, which will launch a web server running on port 8123. The root path is the hub endpoint. There is a preliminary/debug interface if you browse to it.

License
-------
MIT