class Entry():

      Entries=[]

@classmethod
    
    def get_id_entry(self, date, entry):
        self.date = date
        self.entry = entry
    
        return {'date': 'entry': 'entry id'}
    

    def get_entry(self, get):
        self.get = get
    
        return {'date': 'entry'}


    def add_entry(self, add, id):
        self.add = add
    
        return {'update entry'}


    def modify_entry(self, modify):
        self.modify = modify
    
        return {'modified entry'}  


    def delete_entry(self, delete):
        self.delete = delete

        return {'deleted entry'}


    def __str__(self, str):
        
        return(str(self.Entries))"""returns an object as a string"""

    def __len__(self, len):
        
        return (len(self.Entries)"""returns the length of an object"""