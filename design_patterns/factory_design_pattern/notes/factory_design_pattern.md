# 工厂模式(factory_design_pattern)

## 使用场景
1.代码中存在if-else分支判断, 动态的根据不同的类型创建不同的对象.针对这种情况,考虑用工厂模式,将这一大坨if-else创建对象的代码抽离出来,放到工厂类  
2.尽管我们不需要根据不同的类型创建不同的对象，但是，单个对象本身的创建过程比较复杂，比如前面提到的要组合其他类对象，做各种初始化操作。在这种情况下，我们也可以考虑使用工厂模式，将对象的创建过程封装到工厂类中  

第一种情况,如果对象创建逻辑比较简单,推荐使用简单工厂模式, 如果复杂建议使用工厂方法  
第二种情况使用工厂方法模式

## 工厂模式最本质的参考标准
1. 封装变化：创建逻辑有可能变化，封装成工厂类之后，创建逻辑的变更对调用者透明。  
2. 代码复用：创建代码抽离到独立的工厂类之后可以复用。  
3. 隔离复杂性：封装复杂的创建逻辑，调用者无需了解如何创建对象。  
4. 控制复杂度：将创建代码抽离出来，让原本的函数或类职责更单一，代码更简洁