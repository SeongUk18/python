from abc import ABC, abstractmethod


# ABC 정의
class Plugin(ABC):
    @abstractmethod
    def execute(self):
        pass


# 레거시 클래스 정의 (ABC를 상속받지 않음)
class LegacyPlugin:
    def execute(self):
        return "Executing legacy plugin"


# 가상 서브클래스로 등록
Plugin.register(LegacyPlugin)

# 테스트
print(issubclass(LegacyPlugin, Plugin))  # 출력: True

legacy_plugin = LegacyPlugin()
print(isinstance(legacy_plugin, Plugin))  # 출력: True
print(legacy_plugin.execute())  # 출력: Executing legacy plugin
