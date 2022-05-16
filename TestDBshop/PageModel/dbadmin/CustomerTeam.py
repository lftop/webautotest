from base.BaseWeb import BaseWeb


class CustomerTeam(BaseWeb):
    def __init__(self):
        super(CustomerTeam, self).__init__()

    def prediction(self,params):
        print(params)

if __name__=="__main__":
    cu=CustomerTeam()