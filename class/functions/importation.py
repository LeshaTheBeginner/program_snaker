"""aaaa"""
import csv
import fileinput
import sys
class Importation:
    """add change write delete"""
    def __init__(self):
        pass
    def importall(self):
        with open("apps.csv","r") as apps:
            temp=[]
            reader = csv.reader(apps, delimiter=",", quotechar='"')
            for i in reader:
                #print(i)
                #a,b = str(i).split(",")
                #print(a)
                temp.append(i[0])
            return temp
            

    def importt(self,app):
        """aa aaaaa"""
        with open("apps.csv","r") as apps:
            reader = csv.reader(apps, delimiter=",", quotechar='"')
            for i in reader:
                if app in i[0]:
                    return i[1]
            return False
    """This exports files. As of 00:03 Dec 29, It got fixed. line 35 --> writer.writerows(temp1) --> writer.writerow(temp1)"""
    def export(self,app,path):
        if self.importt(app) is False:
            with open("apps.csv","a+") as apps:
                temp1 = [app,path]
                writer = csv.writer(apps,delimiter=",", quotechar="'")
                writer.writerow(temp1)
    """Changes a line in apps.csv. To use, first find the line you want to change, then 2 new values (name, and path)."""
    def change(self,app,newapp,newpath):
        temp2=[]
        for line in fileinput.input("apps.csv", inplace=True):
            #print(f'{app} {newapp}'.format(fileinput.filelineno(),line), end='') # apps.csv --> file line --> 1 file line --> 1 1 file line
            temp2.append(line)
            a,b = line.split(",")
            if app in a:
                print(f"{newapp},{newpath}", end='\n')
            else:
                print(f"{a},{b}",end='') 
    """This deletes a line in apps.csv. To use, first put in the app, then it will get deleted."""
    def delete(self,app):
        if self.importt(app) is not False:
            print(app)
            temp=[]
            for line in fileinput.input("apps.csv", inplace=True):
                temp.append(line)
                a,b = line.split(",")
                if app == a:
                    print("",end="")
                else:
                    print(f"{a},{b}",end='')


