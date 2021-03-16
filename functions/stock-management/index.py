# -*- coding: utf-8 -*-
import json
import logging

logger = logging.getLogger()

def handler(event, context):
    evt = json.loads(event)
    order_id = evt["order_id"]
    # 1. 如果有其他逻辑可以在这里面进行，比如访问数据库查看该订单是否已付款
    # 2. 调用其他接口实现退款。如果退款流程涉及多个步骤，可以将本函数改为子流程，在子流程中处理退款逻辑。
    logger.info("refund order succeeded, id:" + order_id)
    return json.dumps({"stockingManagement": "succeeded"})


