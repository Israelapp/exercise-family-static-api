"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
<<<<<<< HEAD
        # example list of members
        self._members = [
            {
                "first_name": "Jhon",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers":[7, 13, 22],
                "id": self._generateId()
            },
        
      {
                "first_name": "Jane",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers":[10, 14, 3],
                "id": self._generateId(),
            },
              {
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers":[1],
                "id": self._generateId(),
            },
        ]
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        new_id = self._next_id
        self._next_id +=1
        return new_id

    def add_member(self, member):
        member["last_name"] = self.last_name
        member["id"] = self._generateId()
        self._members.append(member)
        return member

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

        # fill this method and update the return

    def get_member(self, id):
        for member in self._members:
            return member
        # fill this method and update the return
        return None
=======
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## You have to implement this method
        ## Append the member to the list of _members
        pass

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        pass

    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        pass
>>>>>>> a1a1ab1119abf44f79085201974fa9b7474571c0

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members