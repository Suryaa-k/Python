class Student():
    batch="P2"
    def __init__(self,name):
        self.name=name
    def change_batch(self,new_batch):
        self.batch=new_batch
s1=Student("Surya")
s2=Student("Lokesh")
s3=Student("Shiva")
s1.change_batch("P3")
print(s1.batch)
print(s2.batch)
print(s3.batch)
