name='adersh'#global
def myname():
    name='lalla'#enclosed
    print(name)

    def oname():
        name='bababu'#local
        print(name)
    oname()    

myname()
print(name)