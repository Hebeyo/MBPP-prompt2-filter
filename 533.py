def remove_datatype(test_tuple, data_type):
  return [ele for ele in test_tuple if not isinstance(ele, data_type)]
