

# pip install pyro4
# sepeeate terminal python -m Pyro4.naming
# run server 
# run clinet


import Pyro4

@Pyro4.expose
class MyRemoteClass(object):
    def addition(self, x, y):
        return x + y

    def mult(self, x, y):
        return x * y

def main():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(MyRemoteClass)
    ns.register("MyRemoteClass", uri)
    print("Server is ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
