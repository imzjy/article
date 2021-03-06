上拉电阻和下拉电阻
==================

在折腾Arduino或者树莓派信号输入的时候，时常听到的就是上拉电阻和下拉电阻，如果这个设置的不对，或者连线不对你是没法达到你期望的效果的。

### 为什么不能直连？

直接将5v电压加在in上这个方案为什么不行？我们来看看电路图：

```text
[5v]-----[switch]------[in]
```
行，但是不会得到你想要的结果。当开关闭合时候，这时候没有问题，in会得到固定的高电平。但是当开关打开的时候，in会受到外界环境因素的影响，会有很小的电流输入，时而有电流输入变成高电平，时而没有电流输入变成低电平，这就是我们说的floating状态，这是一种不稳定状态。 floating发生的原因：
> What you have is called a Floating pin. Digital Input pins are very sensitive to change, and unless positively driven to one state or another (High or Low), will pick up stray capacitance from nearby sources, like breadboards, human fingers, or even the air. Any wire connected to it will act like a little antenna and cause the input state to change. 


### 上拉电阻

先看一下上拉电阻(Pull up resistor)，他的作用就是将输入端保持在高电平。电路图如下：

```text
[5v]-----[pull up resistor]---------[in]
                               |
                            [switch]
                               |
                             [GND]
```
如果switch的状态是Open，那么5v电压经过一个resistor然后到in，in当前的状态是高电平。就是说：
> switch open == high input

当switch闭合的时候，5v电压经过一个resistor，直接短接到GND，这时候in的状态是低电平。换个说法就是：
> swith close == low input

当我们没有这个电阻（pull up resistor）会发生什么？

当开关是open的时候5v电压直接连到in，这时候是in是高电平或者短路。如果开关闭合，那么直接5v到GND造成短路。也就是说没有这个电阻这个电路就是有问题的，不稳定的。

### 下拉电阻

下拉电阻(pushdown resistor)刚好和上拉电阻相反，它的作用是将输入in保持在低电平。看看电路图：

```text
[5v]-----[switch]------------------[in]
                          |
                 [push down resistor]
                          |
                        [GND]
```

当开关open的时候，in没有任何电压输入，所以状态是电平：
> switch open == low input

当开关是close闭合状态时，5v电压因为电阻的牵制，不会直接到GND，而是作为in的输入，当前in的状态为高电平：
> switch close == high input

当我们拿掉下拉电阻会发生什么呢？如果开关open，断路，in没有任何输入。而开关close呢，短路直接到GND，in仍然没有输入。

### 总结

上拉电阻和下拉电阻是防止短路，同时因为电阻的存在让输入不可能直接到GND，从而：1，不会短路。2，使得in端有稳定(固定)的输入。

通常板卡中已经集成了上拉和下拉电阻，可以通过设置pin的工作状态来打开或者关闭pin的集成上拉电阻或者下拉电阻，比如Arduino集成了上拉电阻，可以通过下面的代码来设置：

```c
void setup(){
  pinMode(2, INPUT_PULLUP);
}
```

而树莓派同时集成了上拉电阻和下拉电阻，可以同过下面代码来设置下拉电阻（下拉电阻通常更符合直觉，即开关闭合状态1，关闭状态0）：

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
```
