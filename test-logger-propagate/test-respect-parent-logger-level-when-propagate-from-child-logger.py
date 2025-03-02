import logging

# 创建父 logger
parent_logger = logging.getLogger('parent')
parent_logger.setLevel(logging.WARNING)  # 设置父 logger 的日志级别为 WARNING

# 创建父 logger 的处理器和格式化器
parent_handler = logging.StreamHandler()
parent_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
parent_handler.setFormatter(parent_formatter)
parent_logger.addHandler(parent_handler)

# 创建子 logger
child_logger = logging.getLogger('parent.child')
child_logger.setLevel(logging.INFO)  # 设置子 logger 的日志级别为 DEBUG

child_handler = logging.StreamHandler()
child_formatter = logging.Formatter('%(asctime)s - %(name)s(in child) - %(levelname)s - %(message)s')
child_handler.setFormatter(child_formatter)
child_logger.addHandler(child_handler)

# 测试日志
child_logger.debug('这是一条 DEBUG 级别的日志，不会出现在子 logger 中，也不会出现在父 logger 中')
child_logger.info('这是一条 INFO 级别的日志，也会出现在父 logger 中')
child_logger.warning('这是一条 WARNING 级别的日志，也会出现在父 logger 中')
child_logger.error('这是一条 ERROR 级别的日志，也会出现在父 logger 中')
child_logger.critical('这是一条 CRITICAL 级别的日志，也会出现在父 logger 中')

# 2025-03-02 11:47:12,643 - parent.child(in child) - INFO - 这是一条 INFO 级别的日志，也会出现在父 logger 中
# 2025-03-02 11:47:12,643 - parent.child - INFO - 这是一条 INFO 级别的日志，也会出现在父 logger 中
# 2025-03-02 11:47:12,643 - parent.child(in child) - WARNING - 这是一条 WARNING 级别的日志，也会出现在父 logger 中
# 2025-03-02 11:47:12,643 - parent.child - WARNING - 这是一条 WARNING 级别的日志，也会出现在父 logger 中
# 2025-03-02 11:47:12,644 - parent.child(in child) - ERROR - 这是一条 ERROR 级别的日志，也会出现在父 logger 中
# 2025-03-02 11:47:12,644 - parent.child - ERROR - 这是一条 ERROR 级别的日志，也会出现在父 logger 中
# 2025-03-02 11:47:12,644 - parent.child(in child) - CRITICAL - 这是一条 CRITICAL 级别的日志，也会出现在父 logger 中
# 2025-03-02 11:47:12,644 - parent.child - CRITICAL - 这是一条 CRITICAL 级别的日志，也会出现在父 logger 中