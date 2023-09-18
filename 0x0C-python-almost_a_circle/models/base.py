
"""module"""
import json


class Base:
    """Class of base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init of base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """dict to json"""
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json to file"""
        name = cls.__name__ + ".json"
        with open(name, "w") as jsonf:
            if list_objs:
                dictions = [opj.to_dictionary() for opj in list_objs]
                jsonf.write(Base.to_json_string(dictions))
            else:
                jsonf.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """json to dict"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create new opj"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                opj = cls(1, 1)
            else:
                opj = cls(1)
            opj.update(**dictionary)
            return opj

    @classmethod
    def load_from_file(cls):
        """create opj instants from json file"""
        name = str(cls.__name__) + ".json"
        try:
            with open(name, "r") as jsonf:
                dictions = Base.from_json_string(jsonf.read())
                return [cls.create(**dic) for dic in dictions]
        except IOError:
            return []
