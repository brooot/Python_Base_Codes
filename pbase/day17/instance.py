class Dog:
    def say(self):
        '小狗的沟通方式'
        print('忘')
    def eat(self,that):
        print('正在吃')
        self.food=that
    def food_info(self):
        print('小狗上次吃的是',self.food)
dog1=Dog()
dog2=Dog()
dog1.eat('骨头')
dog2.eat('狗良') 

dog1.food_info()
dog2.food_info()