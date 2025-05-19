class Question:
    def __init__(self,path):
        with open(path,'r') as file:
            data = file.read()
        data = data.split('\n')
        self.question = data[0]
        self.answers = [data[1],data[2],data[3],data[4]]
        self.corr