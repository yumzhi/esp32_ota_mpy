"""
A test file for OTA
"""

class Hello:
    
    def __init__(self):
        self.version = "1.0.0.202309221653"
        self.name = "E-Calendar"
        
        self.init()
        
    def init(self):
        print("version:", self.version)
        
    def say_hi(self):
        print("Welcome to the e-calendar!")
        
if __name__ == '__main__':
    hello = Hello()
    hello.say_hi()
    
