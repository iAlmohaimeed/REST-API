<p align="center">
    
  <a href="https://opensource.org/licenses/mit-license.php" alt="Contributors">
        <img src="https://badges.frapsoft.com/os/mit/mit.svg?v=103" /></a>
  <a href="http://flask.pocoo.org/"><img src="http://flask.pocoo.org/static/badges/made-with-flask-s.png"
   border="0"
   alt="made with Flask"
   title="made with Flask"></a>
  <a href="https://github.com/" alt="Contributors">
        <img src="https://aleen42.github.io/badges/src/github.svg" /></a>
</p>

## What Is This?
This is the most simplified form of a [RESTful-API](https://en.wikipedia.org/wiki/Representational_state_transfer).

## How To Use This
1. **Install** requirements
    ```console
    $ pip install -r requirements.txt
    ```
2. **Run** the server.py file.
    ```console
    $ python server.py
    ```
3. **Call** the endpoints specified for the server.
    * You can use [POSTMAN](https://www.getpostman.com/) to test the api.
    * Server output:
        ```console
        127.0.0.1 - [28/Apr/2019 17:31:54] "GET /employee/testGet HTTP/1.1" 200 
        127.0.0.1 - [28/Apr/2019 17:31:54] "POST /employee/testPost HTTP/1.1" 200 
        127.0.0.1 - [28/Apr/2019 17:31:54] "PUT /employee/testPut HTTP/1.1" 200 
        127.0.0.1 - [28/Apr/2019 17:31:54] "PATCH /employee/testPatch HTTP/1.1" 200 
        127.0.0.1 - [28/Apr/2019 17:31:54] "DELETE /employee/testDelete HTTP/1.1" 200 
        ```
## Endpoint specification
  > Syntax: URL/"endpointName" 


- localhost:5000/**employee**/<_employee_name_> 
  1. This endpoint support the follwonig Http requests:
      * GET
      * POST
      * PUT
      * PATCH
      * DELETE 
  2. This endpoint require a single parameter to be passed <_employee_name_>.

## Note
  * Flask uses port number 5000 as the default port.
  * Each Http request has its own handler, which must be implemented by the developer inside the _server.py_ file. 

## Built With
* [Python](https://www.python.org/) - Python
* [Flask](http://flask.pocoo.org/) - Web development microframework for Python

## Versioning

We use [Github](https://github.com/) for versioning. For the versions available, see the [tags on this repository](https://github.com/IbrahimNM/BudgetOrganizer/tags).

## Authors

* **Ibrahim Almohaimeed** - [Github account](https://github.com/IbrahimNM)

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

