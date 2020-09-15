# -*- coding: UTF-8 -*-


#使用类的方法来创建我们的这家奶茶店
class Milk_tea_shop(object):
    def __init__(self):
        self.mike = ['招牌香醇奶茶\t','香甜布丁奶茶\t','相思红豆奶茶\t']    #奶茶名称
        self.price = [8,11,9]                                                   #对应价格
        self.other = ['椰果\t','珍珠\t','红豆\t','不添加配料\t']                                   #奶茶配料,加收1元
        self.user_buy = ['继续购买\t','不购买,直接结账\t']
        self.discount = [0.7,0.8]                                               #优惠折扣
        self.mike_number = []                    #所有商品的编号存储
        self.other_numner = []                  #所有配料的存储

    #判断用户所选择的饮品是否符合存在
    def is_number(self,number,user_number):
        #奶茶商品的判断
        if user_number.isdigit():
            if number == 0:
                for x in  range(0,len(self.mike)):
                    self.mike_number.append(x)
                if int(user_number) in self.mike_number:
                    return int(user_number)
                else:
                    print('该商品尚未推出,请选择其他饮品!')
                self.line()
            elif number == 1:
                for x in  range(0,len(self.other)):
                    self.other_numner.append(x)
                if int(user_number) in self.other_numner:
                    return int(user_number)
                else:
                    print('该商品尚未推出,请选择其他配料!')
                self.line()
            elif number == 2:
                if int(user_number) in [0,1]:
                    return user_number
                else:
                    print('请重新选择')
                    self.line()

            elif number == 3:
                if int(user_number) <= 0:
                    print('请输入正确的杯数!')
                else:
                    return int(user_number)

        else:
            print('不符合规则,请输入数字编号!')
            self.line()


    #杯数以及配料的选择
    def goods_print(self,user_number_one):
        self.mike_number = []
        self.other_numner = []
        while True:
            cup_number = self.is_number(3,input(self.mike[user_number_one] + '请选择杯数:'))             #杯数
            self.line()
            if cup_number:
                break
        while True:
            for x,y in zip(range(0,len(self.other)),self.other):
                print(x,y)
            self.line()
            user_other_number = self.is_number(1,input('您选择了\t'+self.mike[user_number_one]+'\t' + str(cup_number) + '杯\t请选择其他的配料:'))
            self.line()
            if user_other_number == 0:
                return cup_number,user_other_number
            elif user_other_number:
                break
        #返回杯数和佐料的编号
        return cup_number,user_other_number



    #是否继续购买
    def is_buy(self):
        while True:
            for x,y in zip(range(0,2),self.user_buy):
                print(x,y)
            self.line()
            user_buy = self.is_number(2,input('是否还需要购买:'))                                  #用户是否选择继续购买的编号
            if user_buy == None:
                continue
            else:
                return int(user_buy)


    #辅助线
    def line(self):
        print('---------------------------------------')



    #客户点单
    def user_order(self):
        print('您好,请选择需要购买的饮品!-(根据编号选择)')
        self.line()
        user_data_mike = []
        user_data_cup = []
        user_data_other = []
        all_price = []
        while True:
            for (z,x,y,) in zip(range(0,3),self.mike,self.price,):
                print(z,x,str(y)+'(元/杯)')
            self.line()
            mikes_fit = self.is_number(0,input('请选择:'))                                           #选择的奶茶编号
            if mikes_fit == None:
                continue
            cup_fit,user_fit = self.goods_print(mikes_fit)                                #倍数以及配料数
            #存储用户购买的数据
            user_data_mike.append(mikes_fit)
            user_data_cup.append(cup_fit)
            user_data_other.append(user_fit)
            user_buy = self.is_buy()                                                                    #是否继续购买
            if user_buy == 0:           #为0时继续购买
                continue
            else:
                for x,y,z in zip(user_data_mike,user_data_cup,user_data_other):
                    if z == 3:
                        user_price = (self.price[x] * y)
                    else:
                        user_price = self.price[x] * y + 1
                    all_price.append(user_price)
                    print('您购买了\t' + self.mike[x] + str(y) +'杯\t配料选择：' + self.other[z] + '价钱为:' + str(user_price))
                print('合计'+str(sum(all_price)) + '元')
                if input('任意键退出!'):
                    break







    #启动项目
    def running(self):
        self.user_order()







#运行这个奶茶店的结账系统了
if __name__ == '__main__':
    mike = Milk_tea_shop()
    mike.running()