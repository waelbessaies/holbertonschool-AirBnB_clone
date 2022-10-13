![AIRBNB](assets/airbnb.png)
<h1>Welcome to our AirBnB clone project</h1>

## ***Description***
This project is about a command line interpreter with the ability of manipulating objects like creating, deleting, retrieving even operations

## ***Classes***

These are the classes included in the project
-BaseModel
-User
-Place
-Review
-State
-City
-Amenity

## Classes Table

N° |Class|Description
---|---|---
1|[Console](./console.py)|This is the command line interpreter
2|[FileStorage](./models/engine/file_storage.py)|FileStorage class that serializes instances to a JSON file and deserializes JSON file to instances.
3|[BaseModel](./models/base_model.py)|This is the BaseModel class from which the other classes will inherit
4|[Amenity](./models/amenity.py)|Amenity Class
5|[User](./models/user.py)|User Class
6|[Place](./models/place.py)|Place Class
7|[State](./models/state.py)|State Class
8|[Review](./models/review.py)|Review Class
9|[Test](./tests/test_models/)|Unittest for each class

## Storage
Every time the backend is initialized, HBnB instantiates an instance of FileStorage called storage. The storage object is loaded/re-loaded from any class instances stored in the JSON file, file.json. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.

## Testing 
To run unittests for this program, cd into root directory and run the following command:
`python3 -m unittest discover tests`


## Authors

Wael Bessaies < 4405@holbertonschool.com > Ali Dehissy < 4411@holbertonschool.com >
