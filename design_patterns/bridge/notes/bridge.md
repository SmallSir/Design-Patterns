## 桥接模式
可将一个大类或一系列紧密相关的类拆分为抽象和实现两个独立的层次结构,从而能在开发时分别使用


### 应用场景
1.如果你想要拆分或重组一个具有多重功能的庞杂类（例如能
与多个数据库服务器进行交互的类），可以使用桥接模式。  
2.如果你希望在几个独立维度上扩展一个类，可使用该模式。  
3.如果你需要在运行时切换不同实现方法，可使用桥接模式  