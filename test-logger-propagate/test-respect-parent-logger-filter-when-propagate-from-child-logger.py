import logging

# 创建父 logger
parent_logger = logging.getLogger('parent')
parent_logger.setLevel(logging.DEBUG)

# 创建父 logger 的处理器和格式化器
parent_handler = logging.StreamHandler()
parent_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
parent_handler.setFormatter(parent_formatter)
parent_logger.addHandler(parent_handler)

# 创建父 logger 的过滤器，丢弃包含 "拒绝" 的日志
class RejectFilter(logging.Filter):
    def filter(self, record):
        return "拒绝" not in record.getMessage()

parent_logger.addFilter(RejectFilter())

# 创建子 logger
child_logger = logging.getLogger('parent.child')
child_logger.setLevel(logging.DEBUG)

child_handler = logging.StreamHandler()
child_formatter = logging.Formatter('%(asctime)s - %(name)s(in child) - %(levelname)s - %(message)s')
child_handler.setFormatter(child_formatter)
child_logger.addHandler(child_handler)

# 测试日志
child_logger.info('这是一条正常的 INFO 级别的日志，会被 父 logger 正常输出')
child_logger.info('这是一条包含 "拒绝" 的 INFO 级别的日志，会被父 logger 的正常输出')


# 2025-03-02 11:48:31,625 - parent.child(in child) - INFO - 这是一条正常的 INFO 级别的日志，会被 父 logger 正常输出
# 2025-03-02 11:48:31,625 - parent.child - INFO - 这是一条正常的 INFO 级别的日志，会被 父 logger 正常输出
# 2025-03-02 11:48:31,626 - parent.child(in child) - INFO - 这是一条包含 "拒绝" 的 INFO 级别的日志，会被父 logger 的正常输出
# 2025-03-02 11:48:31,626 - parent.child - INFO - 这是一条包含 "拒绝" 的 INFO 级别的日志，会被父 logger 的正常输出