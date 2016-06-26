上拉电阻和下拉电阻
==================

在折腾Arduino或者树莓派信号输入的时候，时常听到的就是上拉电阻和下拉电阻，如果这个设置的不对，或者连线不对你是没法达到你期望的效果的。

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
switch open == high input

当switch闭合的时候，5v电压经过一个resistor，直接短接到GND，这时候in的状态是低电平。换个说法就是：
swith close == low input
