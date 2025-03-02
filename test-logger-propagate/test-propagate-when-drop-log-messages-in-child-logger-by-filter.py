import logging

# 创建父 logger
parent_logger = logging.getLogger('parent')
parent_logger.setLevel(logging.DEBUG)

# 创建父 logger 的处理器和格式化器
parent_handler = logging.StreamHandler()
parent_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
parent_handler.setFormatter(parent_formatter)
parent_logger.addHandler(parent_handler)

# 创建子 logger
child_logger = logging.getLogger('parent.child')
child_logger.setLevel(logging.DEBUG)

# 创建子 logger 的过滤器，丢弃级别为 INFO 的日志
class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno != logging.INFO

child_logger.addFilter(InfoFilter())

child_handler = logging.StreamHandler()
child_handler.setLevel(logging.DEBUG)

child_formatter = logging.Formatter('%(asctime)s - %(name)s(in child) - %(levelname)s - %(message)s')
child_handler.setFormatter(child_formatter)
child_logger.addHandler(child_handler)

print(f'parent_logger.propagate is {parent_logger.propagate}')
print(f'child_logger.propagate is {child_logger.propagate}')

# 测试日志
parent_logger.debug('这是一条 DEBUG 级别的日志，应该出现在父 logger 中')
parent_logger.info('这是一条 INFO 级别的日志，应该出现在父 logger 中')
child_logger.debug('这是一条 DEBUG 级别的日志，应该出现在父和子 logger 中')
child_logger.info('这是一条 INFO 级别的日志，不应该出现在子 logger 中，也不会出现在父 logger 中')


# parent_logger.propagate is True
# child_logger.propagate is True
# 2025-03-02 11:40:20,226 - parent - DEBUG - 这是一条 DEBUG 级别的日志，应该出现在父 logger 中
# 2025-03-02 11:40:20,226 - parent - INFO - 这是一条 INFO 级别的日志，应该出现在父 logger 中
# 2025-03-02 11:40:20,226 - parent.child(in child) - DEBUG - 这是一条 DEBUG 级别的日志，应该出现在父和子 logger 中
# 2025-03-02 11:40:20,226 - parent.child - DEBUG - 这是一条 DEBUG 级别的日志，应该出现在父和子 logger 中