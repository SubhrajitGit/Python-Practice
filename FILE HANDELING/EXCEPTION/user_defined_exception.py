class MyExceptio(Exception):
    pass

c=25
if(c>5):
    raise MyExceptio("This is to throw error")