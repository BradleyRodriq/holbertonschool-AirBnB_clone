<h1 align="center">HBnB</h1>
<p align="center">AirBnB clone.</p>

---

## Description

HBnB is a clone of the popular AirBnB website.

The project currently only implements the back-end console.

## Classes

HBnB utilizes the following classes:


[BaseModel](./models/base_model.py):
*Attributes: id, created_at, updated_at, save, to_dict

[FileStorage](./models/engine/file_storage.py)
*Attributes: all, new, save, reload

[User](./models/user.py): inherits from [BaseModel](/models/base_model.py).
*Attributes: first_name, last_name, email

[State](./models/state.py): inherits from [BaseModel](./models/base_model.py).
*Attrubutes: name

[City](./models/city.py): inherits from [BaseModel](./models/base_model.py).
*Attributes: state_id, name

[Amenity](./models/amenity.py): inherits from [BaseModel](./models/base_model.py).
*Attributes: name

[Place](./models/place.py): inherits from [BaseModel](./models/base_model.py).
*Attributes: name, city_id, user_id, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids

[Review](./models/review.py): inherits from [BaseModel](./models/base_model.py).
*Attributes: place_id, user_id, text

## Storage

The above classes are handled by the abstracted storage engine defined in the
[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, HBnB instantiates an instance of
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from
any class instances stored in the JSON file `file.json`. As class instances are
created, updated, or deleted, the `storage` object is used to register
corresponding changes in the `file.json`.

## Console

The console is a command line interpreter that permits management of the backend
of HBnB.

### Using the Console

The HBnB console can be run both interactively and non-interactively.
To run the console in non-interactive mode, pipe any command(s) into an execution
of the file `console.py` at the command line.

```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
```

Alternatively, to use the HolbertonBnB console in interactive mode, run the
file `console.py` by itself:

```
$ ./console.py
```

While running in interactive mode, the console displays a prompt for input:

```
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit`, or input an EOF signal
(`ctrl-D`).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The HolbertonBnB console supports the following commands:

* **create**
  * Usage: `create <class>`

Creates a new instance of a given class. The class' ID is printed and
the instance is saved to the file `file.json`.

```
$ ./console.py
(hbnb) create BaseModel
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2019-02-17T2
1:30:42.215277", "created_at": "2019-02-17T21:30:42.215277", "__class__": "Base
Model", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}}
```

* **show**
  * Usage: `show <class> <id>`

Prints the string representation of a class instance based on a given id.

```
$ ./console.py
(hbnb) create User
1e32232d-5a63-4d92-8092-ac3240b29f46
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-a
c3240b29f46', 'created_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828),
'updated_at': datetime.datetime(2019, 2, 17, 21, 34, 3, 635828)}
(hbnb)
```
* **destroy**
  * Usage: `destroy <class> <id>`

Deletes a class instance based on a given id.

```
$ ./console.py
(hbnb) create State
d2d789cd-7427-4920-aaae-88cbcf8bffe2
(hbnb) destroy State d2d789cd-7427-4920-aaae-88cbcf8bffe2

$ cat file.json ; echo ""
{}
```

* **all**
  * Usage: `all <class>`

Prints a string representation of all instances of a given class.

```
$ ./console.py
(hbnb) create BaseModel
fce2124c-8537-489b-956e-22da455cbee8
(hbnb) create BaseModel
450490fd-344e-47cf-8342-126244c2ba99
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (450490fd-344e-47cf-8342-126244c2ba99) {'updated_at': datetime.da
tetime(2019, 2, 17, 21, 45, 5, 963516), 'created_at': datetime.datetime(2019, 2
, 17, 21, 45, 5, 963516), 'id': '450490fd-344e-47cf-8342-126244c2ba99'}", "[Bas
eModel] (fce2124c-8537-489b-956e-22da455cbee8) {'updated_at': datetime.datetime
(2019, 2, 17, 21, 43, 56, 899348), 'created_at': datetime.datetime(2019, 2, 17,
21, 43, 56, 899348), 'id': 'fce2124c-8537-489b-956e-22da455cbee8'}"]
(hbnb)
```

* **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"`

Updates an instance based on the class name and id.

```
$ ./console.py
(hbnb) create User
6f348019-0499-420f-8eec-ef0fdc863c02
(hbnb)
(hbnb) update User 6f348019-0499-420f-8eec-ef0fdc863c02 first_name "Holberton"
(hbnb) show User 6f348019-0499-420f-8eec-ef0fdc863c02
[User] (6f348019-0499-420f-8eec-ef0fdc863c02) {'created_at': datetime.datetime(
2019, 2, 17, 21, 54, 39, 234382), 'first_name': 'Holberton', 'updated_at': date
time.datetime(2019, 2, 17, 21, 54, 39, 234382), 'id': '6f348019-0499-420f-8eec-
ef0fdc863c02'}
(hbnb)
```
