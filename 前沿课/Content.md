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
   * 是不是只有发生过攻击我们才能针对特定的攻击方法进行补充的安全性措施？
   我们是否可以主动预防攻击，如通过某些处理增加图像识别的鲁棒性，使得攻击无效或减弱它的效果？
   * 是的，对于没有出现过的攻击，我们几乎无法防御。因为很多行为只有最后它真的造成了误分类甚至是严重后归才会被人研究，
   就如同那句谚语所说，人类唯一能学到的教训，就是人类从不从历史中吸取教训。
   因为硬要说，每一个错误分类的图片都可以学习并克隆从而达成新的攻击。
   同时基于CIA(Confidentiality, Integrity, Accessibility)原则，在模型inference的过程中，有太多可以动手脚的地方。
   而且因为人工智能的可解释性较差，它并不能像密码学一样做到只将密钥保密，加密手段公开的攻击手段。
   所以基本现在的攻防就是道高一尺魔高一丈的游戏。即使所谓的“Certified Defenses”，也有很苛刻的前提条件，而攻击者并不一定遵守。
   * 我们可以主动预防攻击，部分减弱几乎所有攻击的效果，
   但是需要注意的是，识别准确率如果并没有在训练阶段进行针对性训练，那么其本身的准确率也会下降。
   具体手段包括但不限于：拉伸，旋转[1]，反转，调整亮度等。
   像图211[2]中的就是一个将图片部分像素进行微调从而防御攻击的例子，虽然该文章针对的是Adversarial Perturbation，
   但是其实它的核心思想是通过模型自己的鲁棒性来防御攻击，因为通常来说攻击对perturbation不具有鲁棒性。
   但是这也一样会陷入到道高一尺魔高一丈的内卷中去————已经有很多攻击可以适应大量的perturbation。
   所以一个简单好用而又有效的主动防御并不存在。
   1. Wu T, Wang T, Sehwag V, et al. Just Rotate it: Deploying Backdoor Attacks via Rotation Transformation[J]. arXiv preprint arXiv:2207.10825, 2022.
   2. Prakash A, Moran N, Garber S, et al. Deflecting adversarial attacks with pixel deflection[C]//Proceedings of the IEEE conference on computer vision and pattern recognition. 2018: 8571-8580.

2. 张凯博
   * 请问有没有什么攻击可以既不用修改模型，又可以在部分时刻激活攻击而不是像Adversarial Patch那样一直激活攻击？
   * 这是一个很宏大的梦想，但是目前看来不太可能实现。
   具体实现的时候会有以下几个难点：
      * 不能修改模型意味着我们只能从图片上下手，而图像本身的信息非常有限，现在的识别实际用的图像大小也就224*224，
     若要从中取得足够多的信息量来达成攻击是不那么容易的
      * 更何况我们要达成的并不是像Adversarial Patch那样固定目标类的攻击，即吸引注意力（将模型的注意力吸引到某一个类）类的攻击，
     而是条件攻击，即像Backdoor attack那样需要随时控制出发与否的，这难上加难
      * 是否打算在物理世界实现？如果打算在物理世界实现，则信息量还会大幅进一步削减，因为电子世界到物理世界的信息衰减很严重
   * 综上所述，如果真的出现了这样的攻击，我会觉得很不可思议
3. 易琦
   * 目前对于机器学习算法的防御攻击能力，有哪些指标可以评估？
   * 首先模型本身有Clean Accuracy，用于衡量有多少图片被正确分类到其目标分类。 
   其次还有Attack Success Rate，用以衡量有多少图片被分类到攻击者想要其分类到的目标分类
   但是为什么这两个要单独列出来呢？因为像backdoor这样分状态的攻击可以保持Clean Accuracy很高的同时Attack Success Rate也很高，
   像AP这种不改模型的通常Clean Accuracy就不变，
   特殊的就是针对各自攻击的调整，backdoor的poisoning ratio，trigger size，AP的patch size等。 
   通常来说，在攻击的case下，一般不考虑latency和空间占用
4. 耿瀚飞
   * 防御方现在为了进行Verification会在训练过程中加入Adversarial Data，因此也大大增加了训练成本。
   在现在的Adversarial Training 中，训练成本和同数据集的正常训练相比，会高出多少倍？
   * 这至少取决于你加入了多少Adversarial Data，因为首先训练时间会因为数据量的增多而增长，
   同时因为有了Adversarial Training，它的收敛速度通常会更慢，所以它的训练时间会进一步增长。
   但是最近也有一些工作宣称其可以和训练普通模型的速度几乎一样快。
   它们的核心思想是在一次反向传播的过程中同时更新模型参数和图像的扰动。
   在反向传播后，使用恶意扰动过的图片让模型进行继续训练。
   但是文中并没有出现训练loss随时间下降的图片，
   因此可能虽然其训练速度相较之前的Adversarial Training 有所提高，但是并不一定真的能和训练普通模型一样快
   1. Shafahi A, Najibi M, Ghiasi M A, et al. Adversarial training for free![J]. Advances in Neural Information Processing Systems, 2019, 32.

5. 高帆
   * 现在的发展情况中，攻击方和防御方哪个整体上更占优势？
   * 通常来说，在大部分计算机方面的攻防中，都是攻击方更占优势，图像识别领域也不例外。
     * 攻击者可以想出新的攻击方式，而防御者几乎只能在新的攻击方式出现之后再进行防御
     * 攻击者攻击成功之后拿到的数据和信息的价值很大，而防御者则没有什么明确的收益
     * 即使防御者真的防御住了某些攻击，他们可能也不知道自己防御了某些攻击，因而难以衡量自己的收益
     * 在有人汇报被攻击之前，攻击者的方法就是零时漏洞，可以随意攻击
     * 攻击者只需要找出一种能用的攻击方式即可，而防御者需要应对诸多可能的攻击
### 大闭环助教采纳：
1. 黄兆辉
   * 防御图像识别攻击是否会对识别速度和资源消耗产生影响？如何平衡安全性和性能之间的关系？
   * 会，防御图像识别攻击会对识别速度产生较大的影响（比如PatchCleanse[1]，需要至少inference一张图片九次，很明显速度会变慢许多）
   需要注意的是，并不只是识别速度会变慢，像训练时也会变慢
   （如果模型部署者希望模型具有防御攻击的能力，那么他们就需要进行Adversarial Training，也会慢很多）
   系统性的说，针对图像识别的防御可以分为模型侧和图像侧。
   而模型侧不可避免的会需要model retraining，无论是Fine-Tune[3]还是重训练最后一层[2]，都会有更多的时间需求。
   图像侧可以通过preprocessing[5]，神经元控制[4]等手段来处理图片，而这些操作都是每一张图片都需要操作的，其单次操作时间通常不长，但是会按比例的减慢速度。
   1. Xiang C, Mahloujifar S, Mittal P. {PatchCleanser}: Certifiably Robust Defense against Adversarial Patches for Any Image Classifier[C]//31st USENIX Security Symposium (USENIX Security 22). 2022: 2065-2082.
   2. Liu K, Dolan-Gavitt B, Garg S. Fine-pruning: Defending against backdooring attacks on deep neural networks[C]//Research in Attacks, Intrusions, and Defenses: 21st International Symposium, RAID 2018, Heraklion, Crete, Greece, September 10-12, 2018, Proceedings 21. Springer International Publishing, 2018: 273-294.
   3. Wu D, Wang Y. Adversarial neuron pruning purifies backdoored deep models[J]. Advances in Neural Information Processing Systems, 2021, 34: 16913-16925.
   4. Chen B, Carvalho W, Baracaldo N, et al. Detecting backdoor attacks on deep neural networks by activation clustering[J]. arXiv preprint arXiv:1811.03728, 2018.
   5. Villarreal-Vasquez M, Bhargava B. Confoc: Content-focus protection against trojan attacks on neural networks[J]. arXiv preprint arXiv:2007.00711, 2020.
2. 石雨宸
   * 请问图像识别系统的防御是否可以通过模型训练来实现？迁移学习、集成学习和强化学习等技术是否可以应用于图像识别的防御？
   * 可以，有通过对模型神经元微调来实现的针对后门攻击的防御[1]，也有重新训练部分模型的防御方法。
   但需要注意的是，这些方法通常只被用于防御Backdoor Attack，因为Adversarial Patch并没有修改模型，通过修改模型来防御一个不修改模型的攻击是不常见的。
   而且在重新训练模型的时候几乎都要求需要有一小部分人工验看过的“clean dataset”，但是人工验看也不能保证dataset一定无毒，因为有不需要修改标签的攻击手段[2]。
   图221中显示了一种通过调整模型来防御后门攻击的方法，将原始被攻击过的模型通过干净的数据微调后得到一个教师模型，而后将教师模型和学生模型通过神经元蒸馏合并，
   这样既可以确保模型中的已知后门被消除，也可以保证Clean Accuracy。
   
   1. Li Y, Lyu X, Koren N, et al. Neural attention distillation: Erasing backdoor triggers from deep neural networks[J]. arXiv preprint arXiv:2101.05930, 2021.
   2. Turner A, Tsipras D, Madry A. Label-consistent backdoor attacks[J]. arXiv preprint arXiv:1912.02771, 2019.

3. 倪柯书
   * 如何利用集成和多样化的模型架构来提高深度学习模型对抗后门攻击的安全性？
   * [1]中对模型的结构进行了详细的调研
   1. Su D, Zhang H, Chen H, et al. Is Robustness the Cost of Accuracy?--A Comprehensive Study on the Robustness of 18 Deep Image Classification Models[C]//Proceedings of the European conference on computer vision (ECCV). 2018: 631-648.
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
