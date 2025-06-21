from typing import List, Dict, Set, Tuple, Union, Optional, Any

# 数据类型
# 1、List
list_1: List[int | str] = [1, 2, 3, "s", "a"] # List[int | str]这可以有多种数据类型
print(list_1) # list中的值可以重复

# 2、Dict
dict_1: Dict[str, int] = {"a": 1, "b": 2}
print(dict_1)

# 3、Set
set_1: Set[int] = {1, 2, 3} # set中的值不能重复
print(set_1)

# 4、Tuple
tuple_1: Tuple[int, str] = (1, "a") # 元组中数据定义后不可修改
print(tuple_1)

# 5、Union
union_1: Union[int, str] = 1, "2" # Union[int, str]可以多种数据类型
print(union_1)

# 6、Optional
optional_1: Optional[int] = None # Optional[int]可以多种数据类型
print(optional_1)

# 7、Any
any_1: Any = 1 # Any可以多种数据类型
print(any_1)
