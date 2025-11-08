import csv
class Importation:
    def __init__(self):
        pass
    
    def importt(self,app):
        with open("/home/leshathebeginner/Documents/python/python_stuff/class/apps.csv","r") as apps:
            reader = csv.reader(apps, delimiter=",", quotechar='"')
            for i in reader:
                if app in i[0]:
                    return i[1]
            return print("Not found")

    def export(self,app,PATH):
        with open("/home/leshathebeginner/Documents/python/python_stuff/class/apps.csv","r") as apps:
            temp = []
            reader = csv.reader(apps, delimiter=",", quotechar='"')
            for i in reader:
                temp.append(i)
                if app in i[0]:
                    return print("already exists")
            apps.close()
        with open("/home/leshathebeginner/Documents/python/python_stuff/class/apps.csv","w") as apps:
            temp1 = [app,PATH]
            temp.append(temp1)
            writer = csv.writer(apps,delimiter=",", quotechar='"')
            writer.writerows(temp)

