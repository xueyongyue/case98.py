class animal:
    def sleep(self):
        print("睡")
    def eat(self):
        print("吃")
class dog(animal):
    def run(self):
        print("跑")
    def eat(self):
        print("吃肉")
# 对父类的 sleep 方法进行了扩展
    def sleep(self):
        super().sleep()
        print("睡的更多")

dog().sleep()