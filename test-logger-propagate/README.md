本仓库主要用来验证几个问题

- 子 logger 有自己的 handler，父 logger 有自己的 handler，那么会输出两个信息吗？
  - 会。当然前提是这两个 handler 分别是要输出内容的 + 子 logger 中没有修改 propagate 为 false，默认是 true
  - [代码](./test-is-duplicated-if-child-parent-logger-has-own-handler.py)

- 子 logger 的 filter 导致丢弃了 log 信息，那么这个信息还会不会传导到父 logger 中？
  - 不会。
  - [代码](./test-propagate-when-drop-log-messages-in-child-logger-by-filter.py)

- 子 logger 的 log level 导致丢弃了 log 信息，那么这个信息还会不会传导到父 logger 中？
  - 不会。
  - [代码](./test-propagate-when-drop-log-messages-in-child-logger-by-level.py)

- 子 logger 的 handler 中的 filter 导致丢失了 log 信息，那么这个信息还会不会传导到父 logger 中？
  - 会。其实这是因为子 logger 没有在其本身 filter 掉这条信息，只是在其 handler 中 filter 掉这条信息，这就意味着他会自动往上传播
  - 并且如果子 logger 没有被 handler 的 filter 导致丢失这条信息，那么子 logger 和父 logger 会输出两个分别信息（就像第一个实验那样）
  - [代码](./test-propagate-when-drop-log-messages-in-child-logger-by-handler-filter.py)

- 子 logger 的 log 信息传导到父 logger 中时，还遵不遵守父 logger 的 log level ？
  - 不遵守！！！！！！
  - [代码](./test-respect-parent-logger-level-when-propagate-from-child-logger.py)

- 子 logger 的 log 信息传导到父 logger 中时，还遵不遵守父 logger 的 filter ？
  - 不遵守 ！！！！！
  - [代码](./test-respect-parent-logger-filter-when-propagate-from-child-logger.py)

- 子 logger 的 log 信息传导到父 logger 中时，还遵不遵守父 logger 的 handler 中的 filter ？
  - 遵从
  - [代码](./test-respect-parent-logger-handler-filter-when-propagate-from-child-logger.py)


几个记忆点：

- 只要子 logger 的输出信息没有被自己 filter 丢弃（使用 log level 丢弃等同于 filter 丢弃）（无论自己的 handler 是否丢弃，都不算是被子logger 的 filter 丢弃），并且 propagate 为 true（默认为true），就会被父 logger 接收到。

- 被父 logger 接受到的 log 信息，不会遵从父 logger 的 log level，不会遵从父 logger 的 filter，但是会遵从父 logger 的 handler 中的 filter。

- 如果可以的话，不要在子 logger 中设置任何的 handler 和 filter，以免忘记上述的原则，导致使用 logging 出现问题
  - 这些问题或者说建议来自 [Modern Python logging (youtube.com)](https://www.youtube.com/watch?v=9L77QExPmI0)
