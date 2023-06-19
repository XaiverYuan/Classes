# 图像识别的攻击与防御
### 智能产业研究院 
##### 导师：刘云新
##### 学生：袁宜桢
### 讲课当天助教采纳：
1. 朱结奥
   * 请问现在的图像检测器为什么这么容易受攻击？
   人眼还是比较难欺骗的，除非对物体作物理上较大的调整以实现伪装。
   * 图像识别的判断方式和人类并不一样，比如人眼不可能通过看一小块猫的毛皮的纹路就识别是哪种猫————但是人工智能可以————
   说明人工智能识别物体的方式并不和人类一样（机器更依赖细节，人更依赖宏观），因而欺骗人类的方法与欺骗机器的方法并不相同。
   从另一方面来说，CNN也有感受域这个概念（多大的一个区域能使某一个神经元的值改变）。
   图111[1]中就显示了某人工智能网络的部分层的激活情况，可以看到，相比于人眼所看到的“轮廓”，人工智能网络看到的更多的是“纹路”
   1. Zeiler M D, Fergus R. Visualizing and understanding convolutional networks[C]//Computer Vision–ECCV 2014: 13th European Conference, Zurich, Switzerland, September 6-12, 2014, Proceedings, Part I 13. Springer International Publishing, 2014: 818-833.
2. 周玉清
   * 白盒攻击中的所有攻击方法都将输入图像直接提供给机器学习模型。但是在使用摄像头、麦克风或其他传感器接收信号作为输入的情况下是否都是通过生成物理世界对抗对象来攻击这些系统吗？
   * 当然可以，这里以摄像头举例，所有能在物理世界攻击的攻击都会将摄像头捕获的图片作为输入而不是直接人工编辑的图片
   如果只能以电子世界精细调整的图片作为攻击样本，那这攻击也未免太不实用了。
   举个例子，像图121[1]中的攻击，就是在人的腰上放了一个板子，让照片中的图片依然可以稳定达成攻击。
   更有甚者，即使在柔软的织物上（图122），人在咳嗽，坐下，跑步时仍能较为稳定的达成攻击。
   在这些较为不稳定的环境下达成的攻击都有较高的攻击成功率，应该已经可以证明图像识别的攻击并不是纸上谈兵。
   1. Thys S, Van Ranst W, Goedemé T. Fooling automated surveillance cameras: adversarial patches to attack person detection[C]//Proceedings of the IEEE/CVF conference on computer vision and pattern recognition workshops. 2019: 0-0.
   2. Xu K, Zhang G, Liu S, et al. Adversarial t-shirt! evading person detectors in a physical world[C]//Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part V 16. Springer International Publishing, 2020: 665-681.
### 课后采纳：
1. 石雨宸
   1. 
2. 张凯博
3. 易琦
4. 耿瀚飞
5. 高帆
### 小闭环助教采纳：
1. 黄兆辉
2. 石雨宸
3. 倪柯书
4. 孙佳辰
5. 周玉清
### 大闭环自选：
1. 易琦
2. 杜其原
3. 苏奕晗
4. 张君宇
5. 张哲
6. 王彦豪
7. 剩下的与小闭环助教采纳重合
