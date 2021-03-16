# 简介
本示例展示如何使用 Serverless 工作流 + 函数计算完成一个订单退货系统。

具体场景：
定时任务触发 -> 任务1（查询订单库，获取需要取消的订单列表）-> 任务2（遍历订单列表，对每一个待取消的订单分别执行下述流程）：
     任务3 （判断订单是否已付款）
            任务4 -> 如果订单已付款 -> 任务5 （进行退款流程）-> 进入任务 6
            任务 4.1 -> 如果订单未付款 -> 进入任务 6
     任务 6 整理订单库存 -> 任务 7 完成任务

### 示例场景简介
在这里面，我们将第 2 步、第 4 步 及第 6 步使用函数计算实现，其相互间的调用顺序由工作流编排。
判断订单是否已付款步骤在步骤 4 中实现，即进入步骤 4 之后进行判断。

注意：
1. 为了方便演示，函数实现以打印 log 的方式完成。

### 工程部署

请确保您已开通阿里云函数计算、serverless 工作流服务。
我们目前已支持使用 fun 工具进行部署。如果您对 fun 工具较为熟悉，想获得一致性的用户体验，请执行以下命令：
```
$ fun package -t fun.yaml
$ fun deploy --use-ros --stack-name xxx -t template.packaged.yml
```

上述命令将会创建如下资源：

| LogicalResourceId                        | ResourceType         | Action | Property |
| ---------------------------------------- | -------------------- | ------ | -------- |
| RAMRole                                  | ALIYUN::RAM::Role    | Add    |          |
| demo-order-management                    | ALIYUN::FC::Service  | Add    |          |
| demo-order-managementget-canceled-orders | ALIYUN::FC::Function | Add    |          |
| demo-order-managementstock-management    | ALIYUN::FC::Function | Add    |          |
| demo-order-managementrefund              | ALIYUN::FC::Function | Add    |          |
| demo-order-management-flow               | ALIYUN::FNF::Flow    | Add    |          |

### 工程演示

确保资源部署完成后，进入[函数工作流控制台](<https://fnf.console.aliyun.com/fnf/cn-beijing/flows>)，选择刚创建的流程，点击开始执行。您可以在控制台查看执行结果。

![result](<https://github.com/awesome-fnf/Order-Management/blob/master/result.gif>)
