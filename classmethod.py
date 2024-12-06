class Hello:
    
    @classmethod
    def main(cls, *args):
        print('Hello World')
        Salut.dis_bonjour()

class Salut:
    
    @classmethod
    def dis_bonjour(cls):
        print('Bonjour')

if __name__ == '__main__':
    Hello.main()