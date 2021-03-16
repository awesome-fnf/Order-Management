# -*- coding: utf-8 -*-
import json
import logging
import random

logger = logging.getLogger()

def handler(event, context):
    order_ids = []
    # generate order ids. maybe the ids should get from rds.
    seed = random.randint(2, 4)
    for num in range(seed):
        order_id = "order_%s" % num
        logger.info("get canceled order id:" + order_id)
        order_ids.append(order_id)


    return json.dumps({'order_ids': order_ids})
