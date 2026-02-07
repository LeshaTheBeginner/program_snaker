import matplotlib.pyplot as plt
from network_connection import Requesting as net

class GraphBuilder:
    def __init__(self,datax,datay):
        self.net = net()
        self.datax,datay = self.net.get_it()
        plt.bar(range(len(datax)),datax)
        plt.ylabel("value")
        plt.show()

b = GraphBuilder("","")




#data = ['4','5','87','1','44','83','93','2','54','84','100','64'] 
#data = list(map(int, data))
#x = range(len(data))
#plt.bar(x,data)
#plt.ylabel('y-axis')
#plt.show()

