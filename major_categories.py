class FinancialSubmodule:
  def __init__(self, module_name: str, info: str, path=""):
    self.module_name = module_name
    self.info = info
    self.path = path

    
class FinancialCategory:
  def __init__(self, name: str, submodules: list[FinancialSubmodule]):
    self.name = name
    self.submodules = submodules