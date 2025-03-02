# 子 logger 有自己的 handler，父 logger 有自己的 handler，那么会输出两个信息吗？


import logging

logger = logging.getLogger('parent')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

child_logger = logging.getLogger('parent.child')
child_logger.setLevel(logging.DEBUG)

child_handler = logging.StreamHandler()
child_handler.setLevel(logging.DEBUG)
child_formatter = logging.Formatter('%(asctime)s - %(name)s(in child) - %(levelname)s - %(message)s')
child_handler.setFormatter(child_formatter)
child_logger.addHandler(child_handler)

child_logger.addHandler(child_handler)

logger.info('This is a test message')
child_logger.info('This is a child test message')

# 2025-03-02 11:38:16,567 - parent - INFO - This is a test message
# 2025-03-02 11:38:16,567 - parent.child(in child) - INFO - This is a child test message
# 2025-03-02 11:38:16,567 - parent.child - INFO - This is a child test message