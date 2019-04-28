## What Is This?
This most simplified form of a [RESTful-API](https://en.wikipedia.org/wiki/Representational_state_transfer).

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

## Endpoint specification
  > Syntax: URL/"endpointName" 


- localhost:5000/**endpoint1** (GET)
  1. This endpoint delivers the number of ....   
  2. This endpoint does not require any parameters to be passed.


- localhost:5000/**endpoint2** (GET)
  1. This endpoint allows users get information about an employee.
  2. This endpoint requires the **employee ID** to be passed as in Integer.

## Note
  * Flask uses port number 5000 as a default.

## Built With
* [Python](https://www.python.org/) - Python
* [Flask](http://flask.pocoo.org/) - Web development microframework for Python

## Versioning

We use [Github](https://github.com/) for versioning. For the versions available, see the [tags on this repository](https://github.com/IbrahimNM/BudgetOrganizer/tags).

## Authors

* **Ibrahim Almohaimeed** - [Github account](https://github.com/IbrahimNM)

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

