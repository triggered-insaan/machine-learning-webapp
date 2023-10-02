from pickle import load

class Model:
    def __init__(self, name):
        global model
        self.name = name
        file = open(self.name, 'rb')
        import pickle
        model = pickle.load(file)

    def predict(self, data):
        from numpy import array
        return model.predict(array([data]))[0]
