class Destination:
    def __init__(self,dest_name, dest_id):
        self.dest_name = dest_name
        self.dest_id = dest_id
        self.d_data ={}

    def update_data(self, new_dname, new_did):
        self.d_data['dest_name'] = self.dest_name
        self.d_data['dest_id'] = self.dest_id