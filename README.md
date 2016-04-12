# pika-tornado-leak

To replicate:
- Run the Docker-Compose file
- Make a request to http://localhost:8000/garbage
- Make a request to http://localhost:8000/freeze
- Make many requests to http://localhost:8000/garbage
- Examine console output and see that tornado.ioloop._Timeout grows by 2 each time, increasing memory usage

If you comment out the Tornado Pika connection (rmq.run() in app.py, or the connection itself in TornadoPikaPublisher()), you can see the issue does not occur.
