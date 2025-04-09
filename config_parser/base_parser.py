# @Author: DennisShaw
# @Email: cyan.lab.ai@gmail.com
from abc import ABC, abstractmethod

class BaseParser(ABC):
    @abstractmethod
    def parse(self, lines):
        pass
