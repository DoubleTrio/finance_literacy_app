class FinancialSubmodule:
  def __init__(self, module_name: str, path: str):
    self.module_name = module_name
    self.path = path
    self.completed = False
    
class FinancialCategory:
  def __init__(self, name: str, submodules: list[FinancialSubmodule]):
    self.name = name
    self.submodules = submodules

  def all_completed(self):
    completed = True
    for module in self.submodules:
      if not module.completed:
        completed = False
    return completed


