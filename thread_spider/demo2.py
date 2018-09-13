from time import ctime,sleep

def music(func):
    for i in range(2):
        print('I was listening to %s. %s' %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print('I was at the %s! %s' %(func,ctime()))
        sleep(5)


if __name__ == '__main__':
    music(u'爱情买卖')
    move(u'阿凡达')
    print('all over %s' %ctime())